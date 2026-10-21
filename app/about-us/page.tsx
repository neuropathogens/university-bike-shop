import type { Metadata } from "next";
import AboutUs from "@/components/AboutUs";

export const metadata: Metadata = {
  title: "About Us",
  description:
    "The student team behind University Bike Shop in Palo Alto: mechanics, sales, outreach, and web - local high schoolers selling used bikes and giving back to the community.",
  alternates: { canonical: "/about-us" },
};

export default function AboutUsPage() {
  return <AboutUs />;
}
