import Link from "next/link";
import styles from "./Hero.module.css";

export default function Hero() {
  return (
    <section className={styles.hero}>
      <h1>University Bike Shop</h1>
      <p className={styles.tagline}>
        Used road, gravel &amp; triathlon bikes in Palo Alto - run by local
        high schoolers
      </p>
      <p>
        We sell quality used bikes at student-friendly prices, and our
        workshop handles repairs, tune-ups, and $99 bike fits. We are
        appointment only, located in Crescent Park, Palo Alto.
      </p>
      <nav className={styles.links} aria-label="Popular pages">
        <Link href="/inventory">Current inventory</Link>
        <Link href="/service">Repair prices</Link>
        <Link href="/bike-fits">Bike fits</Link>
        <Link href="/sell-your-bike">Sell your bike</Link>
      </nav>
    </section>
  );
}
