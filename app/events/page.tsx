import type { Metadata } from "next";
import Events from "@/components/Events";

export const metadata: Metadata = {
  title: "Past Events - Camps & Community Repair Days",
  description:
    "Past events from University Bike Shop in Palo Alto: our student-run summer bike camp, back-to-school bike repair days, and other community cycling events.",
  alternates: { canonical: "/events" },
};

export default function EventsPage() {
  return <Events />;
}
