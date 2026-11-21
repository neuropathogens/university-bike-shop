// stdin: JSON [[tex, display], ...]  stdout: JSON [html, ...]
// KaTeX with the mhchem extension (\ce{...} for chemical equations).
const katex = require("katex");
require("katex/contrib/mhchem");
let buf = "";
process.stdin.on("data", d => buf += d);
process.stdin.on("end", () => {
  const items = JSON.parse(buf);
  const out = items.map(([tex, display]) =>
    katex.renderToString(tex, { displayMode: display, throwOnError: true, strict: "ignore", output: "htmlAndMathml" }));
  process.stdout.write(JSON.stringify(out));
});
