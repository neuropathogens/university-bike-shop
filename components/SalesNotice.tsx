import styles from "./SalesNotice.module.css";

export default function SalesNotice() {
  return (
    <aside className={styles.notice}>
      <p>
        <strong>We won&apos;t be checking Facebook as often right now.</strong>{" "}
        Until January 15, 2027, please send all sales inquiries to Talon Zhang,
        our lead sales representative (WeChat: 15219418). Repairs are still
        open.
      </p>
    </aside>
  );
}
