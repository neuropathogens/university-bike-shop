import styles from "./SalesNotice.module.css";

export default function SalesNotice() {
  return (
    <aside className={styles.notice}>
      <p>
        <strong>We are closed for sales on Facebook until November 1.</strong>{" "}
        All sales are going through Talon Zhang, our lead sales representative
        (WeChat: 15219418). Repairs are still open.
      </p>
    </aside>
  );
}
