import type { Metadata } from "next";
import Hero from "@/components/Hero";

export const metadata: Metadata = {
  title: {
    absolute:
      "University Bike Shop | Used Road, Gravel & Triathlon Bikes in Palo Alto",
  },
  description:
    "Student-run bike shop in Palo Alto, CA selling quality used road, gravel, triathlon, and mountain bikes at low prices. Repairs, tune-ups, $99 bike fits, and bike consignment. By appointment in Crescent Park.",
  alternates: { canonical: "/" },
};

export default function Home() {
  return <Hero />;
}
