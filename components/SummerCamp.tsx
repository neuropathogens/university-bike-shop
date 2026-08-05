import styles from "./SummerCamp.module.css";

const SUMMER_CAMP_FORM_URL =
  "https://docs.google.com/forms/d/e/1FAIpQLSdGRsJiKwvP-GkmaVtn3V9d-V5tar8fRVUBs1tZikZn7Vq3wA/viewform?embedded=true";

export default function SummerCamp() {
  return (
    <section id="summer-camp" className={styles.section}>
      <div className={styles.blurb}>
        <p>
          University Bikes summer camp is a 3-day camp meant to teach campers
          about bikes, and how to fix one. Students will learn to construct a
          bike from scratch, and build a bike on the last day of camp. All
          tools will be provided, and
        </p>
        <p>
          The address will be sent after registration. We are located in
          Crescent Park.
        </p>
      </div>
      <iframe src={SUMMER_CAMP_FORM_URL} className={styles.iframe} title="Summer Camp Registration">
        Loading…
      </iframe>
    </section>
  );
}
