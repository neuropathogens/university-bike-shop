import type { Metadata } from "next";
import RepairCost from "@/components/RepairCost";

export const metadata: Metadata = {
  title: "Bike Repair & Tune-Up Prices in Palo Alto",
  description:
    "Bike repair and tune-up prices at University Bike Shop in Palo Alto: tune-ups from $89, derailleur adjustment $25, hydraulic brake bleed $45, wheel truing from $20, Di2 and AXS service, and full custom builds.",
  alternates: { canonical: "/service" },
};

export default function Service() {
  return <RepairCost />;
}
