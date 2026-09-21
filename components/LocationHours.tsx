import styles from "./LocationHours.module.css";

export default function LocationHours() {
  return (
    <section id="location-hours" className={styles.section}>
      <p>
        We are located in Crescent Park, Our address can be obtained through
        emailing us. This way, we can have added security (which also helps
        us keep costs low).
      </p>
      <p>
        We are appointment only, but if you are a member of any of our
        sponsored clubs, our workshop is available from 10-3pm on Saturdays
        and Sundays. However, please text us (650) 656-6807 to give us notice
        at least 48 hours beforehand.
      </p>
    </section>
  );
}
