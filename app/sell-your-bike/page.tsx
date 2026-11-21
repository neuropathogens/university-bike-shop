import type { Metadata } from "next";
import SellYourBike from "@/components/SellYourBike";
import { facebookRatingCount } from "@/config/reviews";

export const metadata: Metadata = {
  title: "Sell Your Bike - 10% Consignment",
  description: `Consign your road, gravel, or triathlon bike with University Bike Shop in Palo Alto for a 10% commission. We inspect, clean, tune, and sell it for you, backed by ${facebookRatingCount} Facebook Marketplace buyer ratings.`,
  alternates: { canonical: "/sell-your-bike" },
};

export default function SellYourBikePage() {
  return <SellYourBike />;
}
