import type { Metadata } from "next";
import LocationHours from "@/components/LocationHours";

export const metadata: Metadata = {
  title: "Location & Hours - Crescent Park, Palo Alto",
  description:
    "University Bike Shop is an appointment-only workshop in Crescent Park, Palo Alto, CA. Text (650) 656-6807 to book. Sponsored club members can use the workshop Saturdays and Sundays 10-3 with 48 hours notice.",
  alternates: { canonical: "/location-hours" },
};

export default function LocationHoursPage() {
  return <LocationHours />;
}
