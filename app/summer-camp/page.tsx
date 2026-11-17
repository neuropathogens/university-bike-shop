import type { Metadata } from "next";
import SummerCamp from "@/components/SummerCamp";

export const metadata: Metadata = {
  title: "Free Summer Bike Camp in Palo Alto",
  description:
    "University Bike Shop's free five-day summer bike camp in Palo Alto: 15 campers learned hands-on bike repair from student mechanics, and every camper went home with a free donated bike.",
  alternates: { canonical: "/summer-camp" },
};

export default function SummerCampPage() {
  return <SummerCamp />;
}
