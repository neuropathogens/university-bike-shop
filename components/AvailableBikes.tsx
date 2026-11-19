import { Fragment } from "react";
import {
  inventoryFootnote,
  inventoryGroups,
  inventoryIntro,
} from "@/config/inventory";
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
  // Hide empty sections, then any group left with nothing to show.
  const groups = inventoryGroups
    .map((group) => ({
      ...group,
      usedBikes: group.usedBikes?.filter((section) => section.bikes.length > 0),
    }))
    .filter(
      (group) =>
        group.note ||
        (group.newBikes?.length ?? 0) > 0 ||
        (group.usedBikes?.length ?? 0) > 0,
    );

  return (
    <section id="available-bikes" className={styles.section}>
      <h1>Inventory</h1>
      <p>{inventoryIntro}</p>

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
                    <li
                      key={bike.name}
                      className={
                        bike.photo
                          ? `${styles.bike} ${styles.withPhoto}`
                          : styles.bike
                      }
                    >
                      {bike.photo && (
                        <img
                          src={bike.photo}
                          alt={bike.name}
                          width={480}
                          height={270}
                          decoding="async"
                          className={styles.photo}
                        />
                      )}
                      <div className={styles.details}>
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
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            ))}

            {group.usedBikes?.map((section) => (
              <div key={section.title} className={styles.subgroup}>
                <h3>{section.title}</h3>
                <ul className={styles.bikes}>
                  {section.bikes.map((bike) => (
                    <li
                      key={`${bike.brand}-${bike.model ?? ""}-${bike.size}`}
                      className={styles.bike}
                    >
                      <div className={styles.headline}>
                        <BikeName
                          text={[bike.brand, bike.model]
                            .filter(Boolean)
                            .join(" ")}
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
              </div>
            ))}
          </div>
        ))}
      </div>

      <p className={styles.footnote}>* {inventoryFootnote}</p>
    </section>
  );
}
