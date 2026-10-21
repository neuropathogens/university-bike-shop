import styles from "./Sponsorships.module.css";

export default function Sponsorships() {
  return (
    <section id="sponsorships" className={styles.section}>
      <h1>Sponsorships</h1>
      <p>We currently sponsor the following:</p>
      <ul>
        <li>Paly Cycling Club</li>
        <li>
          <a
            href="https://stanfordclubsports.com/sports/cycling"
            target="_blank"
            rel="noopener noreferrer"
          >
            Stanford Cycling
          </a>
        </li>
      </ul>
      <p>We also volunteered at:</p>
      <ul>
        <li>Paly Back to School Bike Repair Events</li>
      </ul>
    </section>
  );
}
