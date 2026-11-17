import type { Metadata } from "next";
import Projects from "@/components/Projects";

export const metadata: Metadata = {
  title: "Projects - Bike-Fit Software & Open-Source Parts",
  description:
    "Projects from University Bike Shop in Palo Alto: our own video bike-fit analysis software, an open-source library of 3D-printable bike accessories, and a 3D-printable mountain bike launch.",
  alternates: { canonical: "/projects" },
};

export default function ProjectsPage() {
  return <Projects />;
}
