// grip-lab gauge: BLE protocol + analysis. Pure functions are unit-tested by test.mjs;
// keep the UUIDs in sync with firmware/gauge/src/protocol.h.

export const SERVICE = "7a1e0001-6c2b-4b8e-9d1a-67726970c0de";
export const FORCE = "7a1e0002-6c2b-4b8e-9d1a-67726970c0de";
export const COMMAND = "7a1e0003-6c2b-4b8e-9d1a-67726970c0de";
export const G = 9.81;

/** Decode one 8-byte notification: float32 kg, uint32 ms (little-endian). */
export function parsePacket(view) {
  return { kg: view.getFloat32(0, true), t: view.getUint32(4, true) };
}

/** Highest force in a list of {kg, t} samples (0 for none). */
export function peak(samples) {
  return samples.reduce((m, s) => Math.max(m, s.kg), 0);
}

/** Rate of force development: the steepest rise over any `windowMs` (kg/s). */
export function rfd(samples, windowMs = 100) {
  let best = 0;
  let j = 0;
  for (let i = 0; i < samples.length; i++) {
    while (j < samples.length && samples[j].t - samples[i].t < windowMs) j++;
    if (j >= samples.length) break;
    const dt = (samples[j].t - samples[i].t) / 1000;
    if (dt > 0) best = Math.max(best, (samples[j].kg - samples[i].kg) / dt);
  }
  return best;
}

/** Split a stream into efforts: on above `onKg`, off below `offKg` (hysteresis). */
export function efforts(samples, onKg = 3, offKg = 1.5) {
  const out = [];
  let cur = null;
  for (const s of samples) {
    if (!cur && s.kg >= onKg) cur = [s];
    else if (cur && s.kg <= offKg) {
      out.push(summarise(cur));
      cur = null;
    } else if (cur) cur.push(s);
  }
  if (cur && cur.length > 1) out.push(summarise(cur));
  return out;
}

function summarise(samples) {
  const start = samples[0].t;
  const end = samples[samples.length - 1].t;
  return { start, end, seconds: (end - start) / 1000, peakKg: peak(samples), rfdKgS: rfd(samples) };
}

/** Repeaters: consecutive efforts with their rest gaps (seconds). */
export function repeaters(list) {
  return list.map((e, i) => ({ ...e, restBefore: i ? (e.start - list[i - 1].end) / 1000 : null }));
}

export function toCsv(samples) {
  return "t_ms,force_kg\n" + samples.map((s) => `${s.t},${s.kg.toFixed(3)}`).join("\n") + "\n";
}

/** Connect over Web Bluetooth; calls onSample({kg, t}) per notification. */
export async function connect(onSample, onDisconnect) {
  const device = await navigator.bluetooth.requestDevice({ filters: [{ services: [SERVICE] }] });
  device.addEventListener("gattserverdisconnected", () => onDisconnect && onDisconnect());
  const server = await device.gatt.connect();
  const service = await server.getPrimaryService(SERVICE);
  const force = await service.getCharacteristic(FORCE);
  const command = await service.getCharacteristic(COMMAND);
  force.addEventListener("characteristicvaluechanged", (e) => onSample(parsePacket(e.target.value)));
  await force.startNotifications();
  const send = (text) => command.writeValue(new TextEncoder().encode(text));
  return { device, send, disconnect: () => device.gatt.disconnect() };
}
