import Link from "next/link";
import styles from "./Nav.module.css";

export default function Nav() {
  return (
    <nav className={styles.nav}>
      <Link href="/">Home</Link>
      <Link href="/inventory">Inventory</Link>
      <Link href="/service">Service</Link>
      <Link href="/bike-fits">Bike Fits</Link>
      <Link href="/summer-camp">Summer Camp</Link>
      <Link href="/team">Team</Link>
      <Link href="/about-us">About Us</Link>
      <Link href="/sponsorships">Sponsorships</Link>
    </nav>
  );
}
