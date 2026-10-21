import type { Metadata } from "next";
import AvailableBikes from "@/components/AvailableBikes";

export const metadata: Metadata = {
  title: "Used Bikes for Sale in Palo Alto",
  description:
    "Current inventory of used road, gravel, triathlon/TT, and mountain bikes at University Bike Shop in Palo Alto. Cervelo, Specialized, Scott, Giant, Cannondale, and BMC, inspected and tuned, from $299.",
  alternates: { canonical: "/inventory" },
};

export default function Inventory() {
  return <AvailableBikes />;
}
