import type { Metadata } from "next";
import Reviews from "@/components/Reviews";

export const metadata: Metadata = {
  title: "Reviews - What Our Customers Say",
  description:
    "Customer reviews of University Bike Shop in Palo Alto, from our Facebook Marketplace seller accounts and Instagram.",
  alternates: { canonical: "/reviews" },
};

export default function ReviewsPage() {
  return <Reviews />;
}
