import Link from "next/link";
import { events } from "@/config/events";
import InstagramEmbed from "./InstagramEmbed";
import styles from "./Events.module.css";

export default function Events() {
  const sorted = [...events].sort((a, b) => b.date.localeCompare(a.date));

  return (
    <section id="events" className={styles.section}>
      <h1>Events</h1>
      <p className={styles.intro}>
        Camps, repair days, and community events University Bike Shop has run
        or volunteered at.
      </p>

      {sorted.length === 0 ? (
        <p className={styles.intro}>Past events will be posted here soon.</p>
      ) : (
        <ol className={styles.list}>
          {sorted.map((event) => (
            <li key={`${event.date}-${event.title}`} className={styles.event}>
              <h2>{event.title}</h2>
              <p className={styles.meta}>
                {[event.when, event.location, event.role]
                  .filter(Boolean)
                  .join(" · ")}
              </p>
              <p>{event.description}</p>
              {event.photos && event.photos.length > 0 && (
                <div className={styles.gallery}>
                  {event.photos.map((photo) => (
                    <img
                      key={photo.src}
                      src={photo.src}
                      alt={photo.alt}
                      loading="lazy"
                    />
                  ))}
                </div>
              )}
              {event.link && (
                <Link href={event.link.href} className={styles.link}>
                  {event.link.label}
                </Link>
              )}
              {event.instagram && <InstagramEmbed url={event.instagram} />}
            </li>
          ))}
        </ol>
      )}
    </section>
  );
}
