import {
  facebookAccounts,
  facebookRatingCount,
  lastUpdated,
  spotlights,
} from "@/config/reviews";
import styles from "./Reviews.module.css";

const updatedLabel = new Intl.DateTimeFormat("en-US", {
  timeZone: "America/Los_Angeles",
  month: "long",
  day: "numeric",
  year: "numeric",
  hour: "numeric",
  minute: "2-digit",
  timeZoneName: "short",
}).format(new Date(lastUpdated));

export default function Reviews() {
  return (
    <section id="reviews" className={styles.section}>
      <h1>Reviews</h1>
      <p className={styles.updated}>
        Last updated <time dateTime={lastUpdated}>{updatedLabel}</time>
      </p>
      <p className={styles.intro}>
        Our buyer ratings on Facebook Marketplace and the riders we&apos;ve
        featured on Instagram.
      </p>

      <h2>Facebook Marketplace</h2>
      <p className={styles.intro}>
        We sell through several Facebook Marketplace seller accounts. Together
        they have {facebookRatingCount} buyer ratings:
      </p>
      <ul className={styles.accounts}>
        {facebookAccounts.map((account) => (
          <li key={account.name}>
            <span className={styles.name}>{account.name}</span>{" "}
            <span aria-hidden="true">★</span> {account.rating.toFixed(1)} out
            of 5 ({account.count} ratings{account.note ? `, ${account.note}` : ""})
            {account.strengths && (
              <span className={styles.meta}>
                Strengths buyers named most:{" "}
                {account.strengths
                  .map((s) => `${s.label.toLowerCase()} (${s.count})`)
                  .join(", ")}
              </span>
            )}
          </li>
        ))}
      </ul>

      <h2>Rider Spotlights</h2>
      <p className={styles.intro}>
        Customers we&apos;ve featured on our Instagram,{" "}
        <a
          className={styles.underline}
          href="https://www.instagram.com/universitybikes"
          target="_blank"
          rel="noopener noreferrer"
        >
          @universitybikes
        </a>
        .
      </p>
      <div className={styles.spotlights}>
        {spotlights.map((spotlight) => (
          <img
            key={spotlight.src}
            src={spotlight.src}
            width={spotlight.width}
            height={spotlight.height}
            alt={spotlight.alt}
            decoding="async"
          />
        ))}
      </div>

      <p className={styles.more}>
        Bought or sold a bike with us?{" "}
        <a
          className={styles.underline}
          href="https://www.instagram.com/universitybikes"
          target="_blank"
          rel="noopener noreferrer"
        >
          Tag us on Instagram
        </a>{" "}
        or email universitybikeshop@gmail.com and we may add your review here.
      </p>
    </section>
  );
}
