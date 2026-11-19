import { inventoryFootnote, inventoryGroups } from "@/config/inventory";
import styles from "./AvailableBikes.module.css";

export default function AvailableBikes() {
  const groups = inventoryGroups.filter(
    (group) => group.note || group.bikes.length > 0,
  );

  return (
    <section id="available-bikes" className={styles.section}>
      <h1>Inventory</h1>

      <div className={styles.groups}>
        {groups.map((group) => (
          <div key={group.title} className={styles.group}>
            <h2>{group.title}</h2>
            {group.note && <p>{group.note}</p>}
            {group.bikes.length > 0 && (
              <ul className={styles.bikes}>
                {group.bikes.map((bike) => (
                  <li
                    key={`${bike.brand}-${bike.model ?? ""}-${bike.size}`}
                    className={styles.bike}
                  >
                    <div className={styles.headline}>
                      <span className={styles.name}>
                        {bike.brand}
                        {bike.model && ` ${bike.model}`}
                      </span>
                      <span className={styles.price}>{bike.price}</span>
                    </div>
                    <p className={styles.specs}>
                      {[
                        `Size ${bike.size}`,
                        `${bike.frame} frame`,
                        bike.speeds,
                        bike.groupset,
                        `${bike.wheels} wheels`,
                      ].join(" · ")}
                    </p>
                    {bike.note && <p className={styles.note}>{bike.note}</p>}
                  </li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </div>

      <p className={styles.footnote}>* {inventoryFootnote}</p>
    </section>
  );
}
