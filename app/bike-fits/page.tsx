import type { Metadata } from "next";
import BikeFits from "@/components/BikeFits";

export const metadata: Metadata = {
  title: "Bike Fits in Palo Alto - Free While We Test V3, $99 After",
  description:
    "Professional bike fitting in Palo Alto, free while we test V3, $99 after. Our in-house, computer-powered fitting program analyzes your form, flexibility, and position with front and side cameras. Saturdays and Sundays 10-3 by text.",
  alternates: { canonical: "/bike-fits" },
};

export default function BikeFitsPage() {
  return <BikeFits />;
}
