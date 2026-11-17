import styles from "./SummerCamp.module.css";

const stats = [
  { value: "22", label: "kids signed up" },
  { value: "15", label: "campers" },
  { value: "$0", label: "cost to families" },
  { value: "15", label: "free bikes given away" },
];

const photos = [
  { src: "/camp-photos/camp-01.jpg", alt: "Camper degreasing a chain, seen through the spokes of a Schwinn" },
  { src: "/camp-photos/camp-02.jpg", alt: "Camper adjusting a derailleur cable while a mentor watches" },
  { src: "/camp-photos/camp-03.jpg", alt: "Camper scrubbing a chainring with a brush" },
  { src: "/camp-photos/camp-04.jpg", alt: "Camper crouched beside a bike, cleaning the drivetrain" },
  { src: "/camp-photos/camp-05.jpg", alt: "Mentor and camper working on a bike in the repair stand" },
  { src: "/camp-photos/camp-06.jpg", alt: "Mentor smiling behind a wheel in the repair stand" },
  { src: "/camp-photos/camp-07.jpg", alt: "Camper with two mentors and the Trek hybrid they went home with" },
  { src: "/camp-photos/camp-08.jpg", alt: "Camper with two mentors and the bike they went home with" },
  { src: "/camp-photos/camp-09.jpg", alt: "Camper with two mentors and the mountain bike they went home with" },
  { src: "/camp-photos/camp-10.jpg", alt: "Campers with a golden retriever who stopped by camp" },
];

export default function SummerCamp() {
  return (
    <section id="summer-camp" className={styles.section}>
      <h1>Summer Camp</h1>
      <h2 className={styles.caption}>Summer Camp 2026: Free Bikes, Real Skills</h2>

      <dl className={styles.stats}>
        {stats.map((stat) => (
          <div key={stat.label}>
            <dt>{stat.value}</dt>
            <dd>{stat.label}</dd>
          </div>
        ))}
      </dl>

      <div className={styles.copy}>
        <p>
          In August 2026 we ran a <strong>completely free</strong> five-day
          bike camp in Palo Alto. Demand blew past what we planned for: 22 kids
          signed up for 15 spots. Our student mechanics worked side by side with
          every camper. They degreased chains, scrubbed drivetrains, adjusted
          derailleurs, and tuned bikes in a real repair stand with real shop
          tools.
        </p>
        <p>
          And at the end of the week, <strong>every single camper went home
          with a free bike.</strong> That means 15 kids now have their own bike,
          plus the know-how to keep it running.
        </p>
        <p>
          A huge thank you to everyone who donated bikes. You made this
          possible, and every one of those bikes is now out on the road with a
          new rider.
        </p>
        <p>
          This is just the start. We&apos;re planning more free workshops like
          this soon. Follow{" "}
          <a
            href="https://www.instagram.com/universitybikes"
            target="_blank"
            rel="noopener noreferrer"
          >
            @universitybikes
          </a>{" "}
          to hear when sign-ups open.
        </p>
      </div>

      <div className={styles.gallery}>
        {photos.map((photo) => (
          <img key={photo.src} src={photo.src} alt={photo.alt} loading="lazy" />
        ))}
      </div>
    </section>
  );
}
