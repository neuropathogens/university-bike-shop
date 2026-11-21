import {
  facebookAccounts,
  facebookAsOf,
  facebookRatingCount,
  reviews,
  type Review,
} from "@/config/reviews";
import styles from "./Reviews.module.css";

const MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

const LANGUAGES: Record<string, string> = { zh: "Chinese" };

function formatDate(date: string) {
  const [year, month] = date.split("-");
  return month ? `${MONTHS[Number(month) - 1]} ${year}` : year;
}

function Stars({ rating }: { rating: number }) {
  const full = Math.round(rating);
  return (
    <span className={styles.stars} role="img" aria-label={`${rating} out of 5 stars`}>
      {"★".repeat(full)}
      {"☆".repeat(5 - full)}
    </span>
  );
}

function ReviewItem({ review }: { review: Review }) {
  const meta = [
    review.account,
    review.date && formatDate(review.date),
    review.notable && `Notable: ${review.notable.join(", ")}`,
  ].filter(Boolean);
  const language = review.lang && LANGUAGES[review.lang.split("-")[0]];

  return (
    <li className={styles.review}>
      <figure>
        {review.rating !== undefined && <Stars rating={review.rating} />}
        <blockquote lang={review.lang}>
          <p>&ldquo;{review.quote}&rdquo;</p>
        </blockquote>
        {review.translation && (
          <p className={styles.translation}>
            {language ? `Translated from ${language}: ` : "Translation: "}
            &ldquo;{review.translation}&rdquo;
          </p>
        )}
        <figcaption>
          <span className={styles.name}>{review.name}</span>
          {review.detail && <>, {review.detail}</>}
          {meta.length > 0 && <span className={styles.meta}>{meta.join(" · ")}</span>}
          {review.link && (
            <a className={styles.meta} href={review.link} target="_blank" rel="noopener noreferrer">
              See the original post
            </a>
          )}
        </figcaption>
      </figure>
    </li>
  );
}

export default function Reviews() {
  const facebook = reviews.filter((r) => r.source === "facebook");
  const instagram = reviews.filter((r) => r.source === "instagram");

  return (
    <section id="reviews" className={styles.section}>
      <h1>Reviews</h1>
      <p className={styles.intro}>
        What customers have said about buying bikes from us, from our Facebook
        Marketplace seller accounts and the riders we&apos;ve featured on
        Instagram.
      </p>

      <h2>Facebook Marketplace</h2>
      <p className={styles.intro}>
        We sell through several Facebook Marketplace seller accounts. Together
        they have {facebookRatingCount} buyer ratings (as of{" "}
        {formatDate(facebookAsOf)}):
      </p>
      <ul className={styles.accounts}>
        {facebookAccounts.map((account) => (
          <li key={account.name}>
            <span className={styles.name}>{account.name}</span>{" "}
            <span aria-hidden="true">★</span> {account.rating.toFixed(1)} out
            of 5 ({account.count} ratings)
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
      <ul className={styles.list}>
        {facebook.map((review) => (
          <ReviewItem key={`${review.name}-${review.quote.slice(0, 24)}`} review={review} />
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
      <ul className={styles.list}>
        {instagram.map((review) => (
          <ReviewItem key={`${review.name}-${review.quote.slice(0, 24)}`} review={review} />
        ))}
      </ul>

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
