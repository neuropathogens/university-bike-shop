import { serviceGroups } from "@/config/services";
import styles from "./RepairCost.module.css";

export default function RepairCost() {
  return (
    <section id="repair-cost" className={styles.section}>
      <h1>Service</h1>

      <div className={styles.groups}>
        {serviceGroups.map((group) => (
          <div key={group.title} className={styles.group}>
            <h2>{group.title}</h2>
            <table className={styles.table}>
              <tbody>
                {group.items.map((item) => (
                  <tr key={item.name}>
                    <th scope="row">{item.name}</th>
                    <td>
                      {item.price}
                      {item.note && (
                        <span className={styles.note}> {item.note}</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </div>
    </section>
  );
}
