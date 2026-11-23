import Link from "next/link";
import { projects } from "@/config/projects";
import InstagramEmbed from "./InstagramEmbed";
import styles from "./Projects.module.css";

export default function Projects() {
  return (
    <section id="projects" className={styles.section}>
      <h1>Projects</h1>
      <p className={styles.intro}>
        Beyond buying, fixing, and selling bikes, we build things: software,
        open-source parts, product launches, and community programs.
      </p>

      <ol className={styles.list}>
        {projects.map((project) => (
          <li key={project.title} className={styles.project}>
            <h2>{project.title}</h2>
            <p className={styles.tagline}>{project.tagline}</p>
            <p className={styles.meta}>
              {[project.started && `Started ${project.started}`, project.status]
                .filter(Boolean)
                .join(" · ")}
            </p>
            <p>{project.description}</p>

            {project.highlights && (
              <ul className={styles.highlights}>
                {project.highlights.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            )}

            {project.images && (
              <div
                className={styles.gallery}
                data-count={project.images.length}
              >
                {project.images.map((image) => (
                  <img
                    key={image.src}
                    src={image.src}
                    alt={image.alt}
                    loading="lazy"
                  />
                ))}
              </div>
            )}

            {project.instagram && (
              <InstagramEmbed
                url={project.instagram}
                media={project.instagramSize?.media}
                extra={project.instagramSize?.extra}
              />
            )}

            {project.links && (
              <p className={styles.links}>
                {project.links.map((link) =>
                  link.href.startsWith("/") ? (
                    <Link key={link.href} href={link.href}>
                      {link.label}
                    </Link>
                  ) : (
                    <a
                      key={link.href}
                      href={link.href}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {link.label}
                    </a>
                  ),
                )}
              </p>
            )}
          </li>
        ))}
      </ol>
    </section>
  );
}
