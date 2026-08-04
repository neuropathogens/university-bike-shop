import styles from "./SummerCamp.module.css";

const SUMMER_CAMP_FORM_URL =
  "https://docs.google.com/forms/d/e/1FAIpQLSdGRsJiKwvP-GkmaVtn3V9d-V5tar8fRVUBs1tZikZn7Vq3wA/viewform?embedded=true";

export default function SummerCamp() {
  return (
    <section id="summer-camp" className={styles.section}>
      <iframe src={SUMMER_CAMP_FORM_URL} className={styles.iframe} title="Summer Camp Registration">
        Loading…
      </iframe>
    </section>
  );
}
