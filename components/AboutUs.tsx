import styles from "./AboutUs.module.css";

const SENIOR_SPOTLIGHTS = [
  { n: 1, id: "Dew-vMHj4F7" },
  { n: 2, id: "De0uf7Tmw2j" },
  { n: 3, id: "De2oJ59kr2H" },
  { n: 4, id: "De6AqAbG6aT" },
  { n: 5, id: "De8k3HCG7T8" },
  { n: 6, id: "De-73Dlm5yo" },
  { n: 7, id: "DfBnaGZG50x" },
  { n: 8, id: "DfD5yBQGweD" },
];

const TEAM = [
  { name: "Paul Wang", role: "Manager" },
  { name: "Kai Russel", role: "Lead Mechanic" },
  {
    name: "Kevin Fong",
    role: "Mechanic & Web",
    linkedin: "https://www.linkedin.com/in/kevin-fong-722115329/",
  },
  { name: "Asher Wong", role: "Mechanic" },
  { name: "Talon Zhang", role: "Lead Sales Representative (WeChat)" },
  {
    name: "Leilani Chen",
    role: "Marketing",
    linkedin: "https://www.linkedin.com/in/leilani-chen-1769a92b2/",
  },
  { name: "Wyatt Edson", role: "Outreach & Marketing" },
  {
    name: "Jonathan Chen",
    role: "Graphic Designer",
    linkedin: "https://www.linkedin.com/in/jonathan-chen-22aa2b2ab/",
  },
  {
    name: "Everett Keninger",
    role: "Sourcing",
    linkedin: "https://www.linkedin.com/in/everettkeninger/",
  },
  { name: "David Fridshtand", role: "Web" },
  { name: "Ethan Zhang", role: "Web" },
  { name: "Albert Xu", role: "Web" },
  { name: "Gavin Lin", role: "Outreach" },
  { name: "Christopher Lin", role: "Diversity, Equity, Inclusion" },
  { name: "Lachlan Taylor", role: "Intern" },
  { name: "Orlando Jimenez", role: "Intern" },
  { name: "Brandon Zhang", role: "Intern" },
  { name: "Crystal Zhang", role: "Intern" },
  { name: "Reed Truong", role: "Intern" },
];

export default function AboutUs() {
  return (
    <section id="about-us" className={styles.section}>
      <h1>About University Bike Shop</h1>
      <p>
        University Bike Shop started as a side project to provide bikes at a
        discounted rate.
      </p>
      <p>
        Now, it has evolved to a team of over 10+ local high schoolers
        working together to sell bikes, and to also give back to the
        community through our outreach programs, while still maintaining
        the low prices.
      </p>
      <h2>Team Members:</h2>
      <ul>
        {TEAM.map(({ name, role, linkedin }) => (
          <li key={name}>
            {linkedin ? (
              <a href={linkedin} target="_blank" rel="noopener noreferrer">
                {name}
              </a>
            ) : (
              name
            )}
            {role ? ` - ${role}` : ""}
          </li>
        ))}
      </ul>
      <h2>Media</h2>
      <h3>Senior Spotlight</h3>
      {SENIOR_SPOTLIGHTS.map(({ n, id }) => (
        <iframe
          key={id}
          src={`https://www.instagram.com/p/${id}/embed/captioned/`}
          title={`Senior Spotlight ${n}/11 on Instagram`}
          style={{ width: "100%", height: 900, border: 0 }}
          loading="lazy"
          allowFullScreen
        />
      ))}
    </section>
  );
}
