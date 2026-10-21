import { SHEET_URLS } from "@/config/sheets";
import styles from "./SheetEmbed.module.css";

export default function AvailableBikes() {
  return (
    <section id="available-bikes" className={styles.section}>
      <h1>Used Bikes for Sale in Palo Alto</h1>
      <p>
        Our current inventory of used road, gravel, triathlon/TT, and
        mountain bikes. Every bike is inspected, cleaned, and tuned by our
        mechanics before it goes up for sale. Text (650) 656-6807 or email
        universitybikeshop@gmail.com to reserve a bike or book a time to
        see it.
      </p>

      <h2>Current stock</h2>
      <h3>Road</h3>
      <ul>
        <li>Scott Foil RC 30 (rim, 52cm, carbon, Dura-Ace/Ultegra Di2 mix) - $1,699</li>
        <li>Cervelo R5 SL 2018 (rim, 56cm, carbon, Ultegra) - $1,499</li>
        <li>Cervelo R3 custom paint (rim, 54cm, carbon, Ultegra) - $1,199</li>
        <li>Specialized S-Works Tarmac (disc, 52cm, carbon, Ultegra Di2, includes power meter pedals) - $3,699</li>
        <li>Cannondale CAAD13 (disc, 58cm, aluminum, 105) - $1,750</li>
      </ul>
      <h3>Gravel</h3>
      <ul>
        <li>Giant TCX Advanced Pro 0 (54cm, carbon, SRAM Red eTap) - $1,999</li>
        <li>Specialized Diverge Comp 2023 (58cm, carbon, 105 Di2) - $2,499</li>
      </ul>
      <h3>Triathlon / TT</h3>
      <ul>
        <li>BMC (58cm, carbon, Ultegra/105 mix) - $999</li>
        <li>Blue (52cm, carbon, SRAM Red) - $1,249</li>
      </ul>
      <h3>Mountain</h3>
      <ul>
        <li>Giant Trance 2 (aluminum, Deore) - $599</li>
        <li>Specialized (aluminum) - $299</li>
      </ul>
      <p className={styles.note}>
        Stock snapshot from October 21, 2026. Bikes sell fast, and all bikes
        with electronic shifting include a charger or charging adapter.
      </p>

      <h2>Live inventory</h2>
      <p className={styles.note}>
        This spreadsheet is updated every 24 hours.
      </p>
      {SHEET_URLS.availableBikes ? (
        <iframe
          src={SHEET_URLS.availableBikes}
          className={styles.iframe}
          title="Available Bikes"
        />
      ) : (
        <p className={styles.fallback}>spreadsheet not yet connected</p>
      )}
    </section>
  );
}
