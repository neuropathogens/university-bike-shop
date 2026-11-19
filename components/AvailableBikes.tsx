import { Fragment } from "react";
import { inventoryFootnote, inventoryGroups } from "@/config/inventory";
import styles from "./AvailableBikes.module.css";

// Wrap only between words, so names like "0-AXS" or "Dura-Ace" never split
// at their hyphen on narrow screens.
function BikeName({ text }: { text: string }) {
  return (
    <span>
      {text.split(" ").map((word, i) => (
        <Fragment key={i}>
          {i > 0 && " "}
          <span className={styles.word}>{word}</span>
        </Fragment>
      ))}
    </span>
  );
}

export default function AvailableBikes() {
  const groups = inventoryGroups.filter(
    (group) =>
      group.note || group.bikes.length > 0 || (group.newBikes?.length ?? 0) > 0,
  );

  return (
    <section id="available-bikes" className={styles.section}>
      <h1>Inventory</h1>

      <div className={styles.groups}>
        {groups.map((group) => (
          <div key={group.title} className={styles.group}>
            <h2>{group.title}</h2>
            {group.note && <p>{group.note}</p>}

            {group.newBikes?.map((section) => (
              <div key={section.title} className={styles.subgroup}>
                <h3>{section.title}</h3>
                <ul className={styles.bikes}>
                  {section.bikes.map((bike) => (
                    <li key={bike.name} className={styles.bike}>
                      <div className={styles.headline}>
                        <BikeName text={bike.name} />
                        <span className={styles.price}>
                          {bike.price ? (
                            <>
                              {bike.msrp && (
                                <>
                                  <s className={styles.msrp} title="MSRP">
                                    {bike.msrp}
                                  </s>{" "}
                                </>
                              )}
                              {bike.price}
                            </>
                          ) : (
                            "DM for price"
                          )}
                        </span>
                      </div>
                      <p className={styles.specs}>
                        {[
                          "2027",
                          bike.type,
                          !bike.msrp && "US MSRP not posted yet",
                        ]
                          .filter(Boolean)
                          .join(" · ")}
                      </p>
                    </li>
                  ))}
                </ul>
              </div>
            ))}

            {group.bikes.length > 0 && (
              <ul className={styles.bikes}>
                {group.bikes.map((bike) => (
                  <li
                    key={`${bike.brand}-${bike.model ?? ""}-${bike.size}`}
                    className={styles.bike}
                  >
                    <div className={styles.headline}>
                      <BikeName
                        text={[bike.brand, bike.model].filter(Boolean).join(" ")}
                      />
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
