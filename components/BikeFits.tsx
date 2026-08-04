import styles from "./BikeFits.module.css";

export default function BikeFits() {
  return (
    <section id="bike-fits" className={styles.section}>
      <p>
        University Bikes has our own in house, computer powered fitting
        program.
      </p>
      <p>
        This take approximately 1.5 hours, and costs just $99. We will start
        by analyzing form, drag, and other details.
      </p>
      <p>
        We first will take physical measurements before moving onto
        flexibility. From there, you will cycle on your bike on a roller
        trainer in our store.
      </p>
      <p>
        We will use front and side cameras to record data, and use a
        computer vision and analysis model to recommend changes. We will
        recommend changes on seat post height, saddle angle, saddle
        position, stem length, and stem angle.
      </p>
      <p>Please reserve a time by texting 650-812-9305.</p>
      <p>We are open Saturday 10-3 and Sundays 10-3 for bike fits.</p>
    </section>
  );
}
