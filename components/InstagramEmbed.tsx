import type { CSSProperties } from "react";
import styles from "./Events.module.css";

// Embeds an Instagram post with Instagram's own embed page in an iframe.
// No third-party script needed; the iframe height scales with its width.
export default function InstagramEmbed({
  url,
  media = 4 / 3,
  extra = 310,
  account = "universitybikes",
}: {
  url: string;
  media?: number;
  extra?: number;
  account?: string;
}) {
  const match = url.match(/instagram\.com\/(p|reel)\/([\w-]+)/);
  if (!match) return null;
  const [, kind, code] = match;
  const permalink = `https://www.instagram.com/${kind}/${code}/`;

  return (
    <div
      className={styles.instagram}
      style={
        { "--ig-media": media, "--ig-extra": `${extra}px` } as CSSProperties
      }
    >
      <iframe
        src={`${permalink}embed/captioned/`}
        title={`Instagram post from @${account}`}
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
