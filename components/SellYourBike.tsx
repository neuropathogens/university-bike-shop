import Link from "next/link";
import { facebookAccounts, facebookRatingCount } from "@/config/reviews";
import styles from "./SellYourBike.module.css";

export default function SellYourBike() {
  return (
    <section id="sell-your-bike" className={styles.section}>
      <h1>Sell Your Bike</h1>
      <p>
        We can help you consign your road, gravel, or triathlon bike at a
        commission rate of 10%. We will inspect, clean, and tune-up your
        bike, and do all of the messaging for you. Our Facebook Marketplace
        seller accounts have {facebookRatingCount} buyer ratings between them
        (rated{" "}
        {new Intl.ListFormat("en").format(
          facebookAccounts.map((a) => a.rating.toFixed(1)),
        )}{" "}
        stars;
        see our{" "}
        <Link href="/reviews" className={styles.link}>
          reviews
        </Link>
        ), and we will promise that same quality to you.
      </p>
      <p>
        Please message (650) 656-6807 or email universitybikeshop@gmail.com
        with photos, specs, and details of your bike if you are interested.
      </p>
    </section>
  );
}
