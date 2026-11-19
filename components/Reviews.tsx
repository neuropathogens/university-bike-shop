import { reviews, sourceLabels, type Review } from "@/config/reviews";
import styles from "./Reviews.module.css";

const MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

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

function sourceLine(review: Review) {
  const parts = [sourceLabels[review.source]];
  if (review.account) parts[0] += ` (${review.account})`;
  if (review.date) parts.push(formatDate(review.date));
  return parts.join(" · ");
}

export default function Reviews() {
  const rated = reviews.filter((r) => r.rating !== undefined);
  const average =
    rated.length > 0
      ? rated.reduce((sum, r) => sum + (r.rating ?? 0), 0) / rated.length
      : undefined;

  return (
    <section id="reviews" className={styles.section}>
      <h1>Reviews</h1>
      <p className={styles.intro}>
        What customers have said about buying, selling, and fixing bikes with
        us, collected from our Facebook Marketplace seller accounts and our
        Instagram.
      </p>
      {average !== undefined && (
        <p className={styles.summary}>
          <Stars rating={average} /> {average.toFixed(1)} average across{" "}
          {rated.length} {rated.length === 1 ? "review" : "reviews"} shown here
        </p>
      )}

      <ul className={styles.list}>
        {reviews.map((review) => (
          <li key={`${review.name}-${review.quote.slice(0, 24)}`} className={styles.review}>
            <figure>
              {review.rating !== undefined && <Stars rating={review.rating} />}
              <blockquote>
                <p>&ldquo;{review.quote}&rdquo;</p>
              </blockquote>
              <figcaption>
                <span className={styles.name}>{review.name}</span>
                {review.detail && <>, {review.detail}</>}
                <span className={styles.source}>
                  {review.link ? (
                    <a href={review.link} target="_blank" rel="noopener noreferrer">
                      {sourceLine(review)}
                    </a>
                  ) : (
                    sourceLine(review)
                  )}
                </span>
              </figcaption>
            </figure>
          </li>
        ))}
      </ul>

      <p className={styles.more}>
        Bought or sold a bike with us?{" "}
        <a href="https://www.instagram.com/universitybikes" target="_blank" rel="noopener noreferrer">
          Tag us on Instagram
        </a>{" "}
        or email universitybikeshop@gmail.com and we may add your review here.
      </p>
    </section>
  );
}
