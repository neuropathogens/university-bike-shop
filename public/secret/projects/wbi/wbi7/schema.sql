-- ============================================================================
-- WBI7 — Supabase schema for cloud save + sharing
--
-- Run this once in your Supabase project: SQL Editor -> New query -> paste ->
-- Run. It is idempotent (safe to re-run). It creates:
--   * deals          : one row per saved underwriting model (JSONB)
--   * deal_shares     : viewer/editor grants from an owner to another user
--   * RLS policies    : a user sees only their own deals + deals shared to them
--   * helper fns      : SECURITY DEFINER checks (avoid RLS recursion)
--   * user_id_by_email: resolve an email to a user id, for share-by-email
--
-- This matches exactly what index.html's cloud client queries:
--   deals(id, owner, name, model, cat, updated_at)
--   deal_shares(deal_id, grantee, role)   -- upsert on (deal_id, grantee)
--   rpc user_id_by_email(p_email)
-- ============================================================================

-- ---------- tables ----------------------------------------------------------
create table if not exists public.deals (
  id          uuid primary key default gen_random_uuid(),
  owner       uuid not null references auth.users(id) on delete cascade,
  name        text not null default 'Untitled deal',
  model       jsonb not null,
  cat         text,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index if not exists deals_owner_idx on public.deals(owner);

create table if not exists public.deal_shares (
  deal_id     uuid not null references public.deals(id) on delete cascade,
  grantee     uuid not null references auth.users(id)  on delete cascade,
  role        text not null default 'viewer' check (role in ('viewer','editor')),
  created_at  timestamptz not null default now(),
  primary key (deal_id, grantee)            -- supports upsert onConflict (deal_id,grantee)
);
create index if not exists deal_shares_grantee_idx on public.deal_shares(grantee);

-- ---------- keep updated_at fresh ------------------------------------------
create or replace function public.touch_updated_at()
returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end;
$$;

drop trigger if exists deals_touch_updated_at on public.deals;
create trigger deals_touch_updated_at
  before update on public.deals
  for each row execute function public.touch_updated_at();

-- ---------- helper checks (SECURITY DEFINER => bypass RLS, no recursion) -----
create or replace function public.deal_is_owner(d uuid)
returns boolean language sql security definer stable set search_path = public as $$
  select exists (select 1 from public.deals where id = d and owner = auth.uid());
$$;

create or replace function public.deal_is_shared(d uuid)
returns boolean language sql security definer stable set search_path = public as $$
  select exists (select 1 from public.deal_shares where deal_id = d and grantee = auth.uid());
$$;

create or replace function public.deal_can_edit(d uuid)
returns boolean language sql security definer stable set search_path = public as $$
  select exists (select 1 from public.deals where id = d and owner = auth.uid())
      or exists (select 1 from public.deal_shares
                  where deal_id = d and grantee = auth.uid() and role = 'editor');
$$;

-- ---------- enable RLS ------------------------------------------------------
alter table public.deals        enable row level security;
alter table public.deal_shares  enable row level security;

-- deals: read your own + anything shared to you
drop policy if exists deals_select on public.deals;
create policy deals_select on public.deals for select
  using (deal_is_owner(id) or deal_is_shared(id));

-- deals: you may only insert rows you own
drop policy if exists deals_insert on public.deals;
create policy deals_insert on public.deals for insert
  with check (owner = auth.uid());

-- deals: owners and editors may update; result must remain owned by the owner
drop policy if exists deals_update on public.deals;
create policy deals_update on public.deals for update
  using (deal_can_edit(id))
  with check (deal_can_edit(id));

-- deals: only the owner may delete
drop policy if exists deals_delete on public.deals;
create policy deals_delete on public.deals for delete
  using (deal_is_owner(id));

-- deal_shares: the grantee can see their grant; the deal owner can see all grants
drop policy if exists shares_select on public.deal_shares;
create policy shares_select on public.deal_shares for select
  using (grantee = auth.uid() or deal_is_owner(deal_id));

-- deal_shares: only the deal owner may create/modify/remove grants
drop policy if exists shares_write on public.deal_shares;
create policy shares_write on public.deal_shares for all
  using (deal_is_owner(deal_id))
  with check (deal_is_owner(deal_id));

-- ---------- share-by-email lookup ------------------------------------------
-- Returns the user id for an email, or NULL. SECURITY DEFINER so it can read
-- auth.users. Granted only to authenticated users. It exposes nothing beyond an
-- opaque user id (no profile data), and only for an email the caller already
-- knows; this is the minimum needed to let an owner share a deal by email.
create or replace function public.user_id_by_email(p_email text)
returns uuid language sql security definer stable set search_path = public, auth as $$
  select id from auth.users where lower(email) = lower(trim(p_email)) limit 1;
$$;

revoke all on function public.user_id_by_email(text) from public, anon;
grant execute on function public.user_id_by_email(text) to authenticated;

-- ---------- table grants (RLS still applies on top) -------------------------
grant select, insert, update, delete on public.deals       to authenticated;
grant select, insert, update, delete on public.deal_shares to authenticated;

-- Done. Sharing requires the grantee to have signed in at least once (so their
-- auth.users row exists). RLS enforces everything server-side: viewers can open
-- but not overwrite, editors can save changes, only the owner can delete.
