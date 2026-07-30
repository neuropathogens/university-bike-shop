import { SHEET_URLS } from "@/config/sheets";
import styles from "./SheetEmbed.module.css";

export default function RepairCost() {
  return (
    <section id="repair-cost" className={styles.section}>
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
