import type { NextConfig } from "next";

// The site is fully static: `next build` writes plain files to out/, which
// Cloudflare Pages serves. Response headers live in public/_headers (static
// exports cannot set them here). Pages serves public/**/index.html at its
// folder URL on its own, so the unlisted pages under public/secret/ need no
// rewrites.
const nextConfig: NextConfig = {
  output: "export",
};

export default nextConfig;
