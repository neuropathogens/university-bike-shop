// stdin: JSON [[tex, display], ...]  stdout: JSON [html, ...]
const katex = require("katex");
let buf = "";
process.stdin.on("data", d => buf += d);
process.stdin.on("end", () => {
  const items = JSON.parse(buf);
  const out = items.map(([tex, display]) =>
    katex.renderToString(tex, { displayMode: display, throwOnError: true, strict: "error", output: "htmlAndMathml" }));
  process.stdout.write(JSON.stringify(out));
});
