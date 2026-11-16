"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./Nav.module.css";

const links = [
  { href: "/", label: "Home" },
  { href: "/inventory", label: "Inventory" },
  { href: "/sell-your-bike", label: "Sell Your Bike" },
  { href: "/service", label: "Service" },
  { href: "/bike-fits", label: "Bike Fits" },
  { href: "/summer-camp", label: "Summer Camp" },
  { href: "/events", label: "Events" },
  { href: "/sponsorships", label: "Sponsorships" },
  { href: "/about-us", label: "About Us" },
  { href: "/location-hours", label: "Location & Hours", right: true },
];

export default function Nav() {
  const pathname = usePathname();
  // The menu is open only on the page where it was opened, so following a
  // link closes it without an effect.
  const [openOn, setOpenOn] = useState<string | null>(null);
  const open = openOn === pathname;

  return (
    <nav className={styles.nav}>
      <div className={styles.bar}>
        <Link href="/" className={styles.brand}>
          University Bike Shop
        </Link>
        <button
          type="button"
          className={styles.toggle}
          aria-expanded={open}
          aria-controls="site-menu"
          onClick={() => setOpenOn(open ? null : pathname)}
        >
          {open ? "Close" : "Menu"}
        </button>
      </div>
      <ul id="site-menu" className={`${styles.links} ${open ? styles.open : ""}`}>
        {links.map((link) => (
          <li key={link.href} className={link.right ? styles.right : undefined}>
            <Link
              href={link.href}
              aria-current={pathname === link.href ? "page" : undefined}
            >
              {link.label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
