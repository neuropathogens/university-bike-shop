import styles from "./Contact.module.css";

export default function Contact() {
  return (
    <footer id="contact" className={styles.contact}>
      <p>universitybikeshop@gmail.com</p>
      <p>(650) 656-6807</p>
      <p>
        <a
          href="https://www.instagram.com/universitybikes"
          target="_blank"
          rel="noopener noreferrer"
        >
          @universitybikes
        </a>
      </p>
    </footer>
  );
}
