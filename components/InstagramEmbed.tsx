import styles from "./Events.module.css";

// Embeds an Instagram post with Instagram's own embed page in an iframe.
// No third-party script needed; the iframe height scales with its width.
export default function InstagramEmbed({ url }: { url: string }) {
  const match = url.match(/instagram\.com\/(p|reel)\/([\w-]+)/);
  if (!match) return null;
  const [, kind, code] = match;
  const permalink = `https://www.instagram.com/${kind}/${code}/`;

  return (
    <div className={styles.instagram}>
      <iframe
        src={`${permalink}embed/captioned/`}
        title="Instagram post from @universitybikes"
        loading="lazy"
        scrolling="no"
        allowFullScreen
      />
      <a href={permalink} target="_blank" rel="noopener noreferrer">
        View on Instagram
      </a>
    </div>
  );
}
