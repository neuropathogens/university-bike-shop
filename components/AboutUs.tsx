import styles from "./AboutUs.module.css";

const TEAM = [
  { name: "Paul Wang", role: "Manager" },
  { name: "Kai Russel", role: "Lead Mechanic" },
  { name: "Kevin Fong", role: "Mechanic & Web" },
  { name: "Asher Wong", role: "Mechanic" },
  { name: "Leilani Chen", role: "Marketing" },
  { name: "Wyatt Edson", role: "Outreach & Marketing" },
  { name: "Everett Keninger", role: "Sourcing" },
  { name: "David Fridshtand", role: "Web" },
  { name: "Ethan Zhang", role: "Web" },
  { name: "Albert Xu", role: "Web" },
  { name: "Gavin Lin", role: "Outreach" },
  { name: "Lachlan Taylor", role: "Intern" },
  { name: "Orlando Jimenez", role: "Intern" },
];

export default function AboutUs() {
  return (
    <section id="about-us" className={styles.section}>
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
        {TEAM.map(({ name, role }) => (
          <li key={name}>
            {name}
            {role ? ` - ${role}` : ""}
          </li>
        ))}
      </ul>
      <h2>Media</h2>
    </section>
  );
}
