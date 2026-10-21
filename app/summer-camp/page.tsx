import type { Metadata } from "next";
import SummerCamp from "@/components/SummerCamp";

export const metadata: Metadata = {
  title: "Summer Bike Camp in Palo Alto",
  description:
    "Photos and highlights from this year's University Bike Shop summer camp in Palo Alto, where campers learn bike maintenance and repair hands-on.",
  alternates: { canonical: "/summer-camp" },
};

export default function SummerCampPage() {
  return <SummerCamp />;
}
