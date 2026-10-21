import type { Metadata } from "next";
import Sponsorships from "@/components/Sponsorships";

export const metadata: Metadata = {
  title: "Sponsorships - Paly & Stanford Cycling",
  description:
    "University Bike Shop sponsors the Paly Cycling Club and Stanford Cycling, and volunteers at Paly back-to-school bike repair events in Palo Alto.",
  alternates: { canonical: "/sponsorships" },
};

export default function SponsorshipsPage() {
  return <Sponsorships />;
}
