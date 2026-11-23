"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./Nav.module.css";

type NavLink = { href: string; label: string };
type NavGroup = { label: string; links: NavLink[] };
type NavItem = (NavLink | NavGroup) & { right?: boolean };

const items: NavItem[] = [
  { href: "/", label: "Home" },
  { href: "/inventory", label: "Inventory" },
  { href: "/sell-your-bike", label: "Sell Your Bike" },
  { href: "/service", label: "Service" },
  { href: "/bike-fits", label: "Bike Fits" },
  {
    label: "Community",
    links: [
      { href: "/events", label: "Events" },
      { href: "/summer-camp", label: "Summer Camp" },
      { href: "/sponsorships", label: "Sponsorships" },
    ],
  },
  {
    label: "About",
    links: [
      { href: "/about-us", label: "About Us" },
      { href: "/projects", label: "Projects" },
      { href: "/reviews", label: "Reviews" },
    ],
  },
  { href: "/location-hours", label: "Location & Hours", right: true },
];

export default function Nav() {
  const pathname = usePathname();
  // Menus are open only on the page where they were opened, so following a
  // link closes them without an effect.
  const [openOn, setOpenOn] = useState<string | null>(null);
  const open = openOn === pathname;
  const [groupOn, setGroupOn] = useState<{ path: string; label: string } | null>(null);
  const openGroup = groupOn?.path === pathname ? groupOn.label : null;

  const link = ({ href, label }: NavLink) => (
    <Link href={href} aria-current={pathname === href ? "page" : undefined}>
      {label}
    </Link>
  );

  return (
    <nav className={styles.nav}>
      <div className={styles.bar}>
        <Link href="/" className={styles.brand}>
          University Bike Shop
        </Link>
        <button
          type="button"
          className={styles.toggle}
          aria-expanded={open}
          aria-controls="site-menu"
          onClick={() => setOpenOn(open ? null : pathname)}
        >
          {open ? "Close" : "Menu"}
        </button>
      </div>
      <ul id="site-menu" className={`${styles.links} ${open ? styles.open : ""}`}>
        {items.map((item) => {
          if (!("links" in item)) {
            return (
              <li key={item.href} className={item.right ? styles.right : undefined}>
                {link(item)}
              </li>
            );
          }
          const expanded = openGroup === item.label;
          const active = item.links.some((l) => l.href === pathname);
          const menuId = `nav-${item.label.toLowerCase()}`;
          return (
            <li
              key={item.label}
              className={`${styles.group} ${expanded ? styles.expanded : ""}`}
              onBlur={(e) => {
                if (!e.currentTarget.contains(e.relatedTarget)) setGroupOn(null);
              }}
              onKeyDown={(e) => {
                if (e.key === "Escape") setGroupOn(null);
              }}
            >
              <button
                type="button"
                className={`${styles.groupButton} ${active ? styles.active : ""}`}
                aria-expanded={expanded}
                aria-controls={menuId}
                onClick={() =>
                  setGroupOn(expanded ? null : { path: pathname, label: item.label })
                }
              >
                {item.label}
                <span aria-hidden="true" className={styles.caret}>
                  ▾
                </span>
              </button>
              <span className={styles.groupLabel}>{item.label}</span>
              <ul id={menuId} className={styles.submenu}>
                {item.links.map((l) => (
                  <li key={l.href}>{link(l)}</li>
                ))}
              </ul>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}
