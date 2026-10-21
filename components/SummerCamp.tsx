import styles from "./SummerCamp.module.css";

export default function SummerCamp() {
  return (
    <section id="summer-camp" className={styles.section}>
      <h1>Summer Camp</h1>
      <h2 className={styles.caption}>This Year&apos;s Summer Camp</h2>
      <img
        src="/summer-camp-group.jpg"
        alt="Summer camp campers with their bikes"
        className={styles.heroImage}
      />
      <div className={styles.gallery}>
        <img src="/summer-camp-wheel.jpg" alt="Camper adjusting a rear derailleur" />
        <img src="/summer-camp-tent.jpg" alt="Campers gathered under a canopy" />
        <img src="/summer-camp-spray.jpg" alt="Camper using a pressure washer on a bike" />
        <img src="/summer-camp-hose.jpg" alt="Camper rinsing a bike wheel" />
      </div>
    </section>
  );
}
