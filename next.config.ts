import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Unlisted static pages under public/secret/ (served at a clean URL, kept out of search engines).
  async rewrites() {
    return [
      {
        source: "/secret/climbing/holds",
        destination: "/secret/climbing/holds/index.html",
      },
      {
        source: "/secret/climbing/gauge",
        destination: "/secret/climbing/gauge/index.html",
      },
      {
        source: "/secret/claude-audit",
        destination: "/secret/claude-audit/index.html",
      },
      {
        source: "/secret/directory",
        destination: "/secret/directory/index.html",
      },
    ];
  },
  async headers() {
    return [
      {
        source: "/secret/:path*",
        headers: [{ key: "X-Robots-Tag", value: "noindex, nofollow, noarchive" }],
      },
    ];
  },
};

export default nextConfig;
