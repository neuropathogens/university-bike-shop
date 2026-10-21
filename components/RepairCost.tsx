import { SHEET_URLS } from "@/config/sheets";
import styles from "./SheetEmbed.module.css";

export default function RepairCost() {
  return (
    <section id="repair-cost" className={styles.section}>
      <h1>Bike Repair &amp; Service Prices in Palo Alto</h1>
      <p>
        Our Crescent Park workshop services road, gravel, triathlon, and
        mountain bikes, including Shimano and SRAM electronic shifting
        (Di2, AXS, eTap). Text (650) 656-6807 to book a repair.
      </p>

      <h2>Tune-Ups</h2>
      <ul>
        <li>Basic Tune-Up - $89</li>
        <li>Standard Tune-Up - $149</li>
        <li>Premium Tune-Up (Full Overhaul) - $299</li>
      </ul>

      <h2>Drivetrain Service</h2>
      <ul>
        <li>Derailleur Adjustment (Shimano or SRAM mechanical) - $25</li>
        <li>Full Drivetrain Service (mechanical) - $60</li>
        <li>Di2 / AXS / eTap Setup &amp; Pairing - $45</li>
        <li>Full Di2 / AXS Service - $85</li>
      </ul>

      <h2>Brakes</h2>
      <ul>
        <li>Mechanical Brake Adjustment - $20</li>
        <li>Hydraulic Brake Bleed - $45</li>
        <li>Brake Pad Replacement (labor) - $15</li>
      </ul>

      <h2>Wheels</h2>
      <ul>
        <li>Wheel True - Minor - $20</li>
        <li>Wheel True - Major - $40</li>
        <li>Wheel Build (customer supplied parts) - $75</li>
        <li>Flat Repair / Tube Change - $15</li>
      </ul>

      <h2>Drivetrain &amp; Components</h2>
      <ul>
        <li>Chain Replacement (labor) - $10</li>
        <li>Cassette Replacement (labor) - $10</li>
        <li>Headset Service - $25</li>
        <li>Bottom Bracket Service - $25</li>
        <li>Bar Tape / Grip Install - $10</li>
      </ul>

      <h2>Bike Builds</h2>
      <ul>
        <li>Basic Assembly (box bike) - $125</li>
        <li>Full Custom Build - $200</li>
      </ul>

      <p className={styles.note}>
        Live price sheet below. Campagnolo is not serviced.
      </p>
      {SHEET_URLS.repairCost ? (
        <iframe
          src={SHEET_URLS.repairCost}
          className={styles.iframe}
          title="Repair Cost"
        />
      ) : (
        <p className={styles.fallback}>spreadsheet not yet connected</p>
      )}
    </section>
  );
}
