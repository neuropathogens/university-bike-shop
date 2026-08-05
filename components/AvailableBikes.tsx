import { SHEET_URLS } from "@/config/sheets";
import styles from "./SheetEmbed.module.css";

export default function AvailableBikes() {
  return (
    <section id="available-bikes" className={styles.section}>
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
