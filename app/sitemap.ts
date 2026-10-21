import type { MetadataRoute } from "next";

const BASE_URL = "https://universitybikeshop.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = [
    "",
    "/inventory",
    "/sell-your-bike",
    "/service",
    "/bike-fits",
    "/summer-camp",
    "/sponsorships",
    "/about-us",
    "/location-hours",
  ];

  return routes.map((route) => ({
    url: `${BASE_URL}${route}`,
    lastModified: new Date(),
    changeFrequency: route === "/inventory" ? "daily" : "weekly",
    priority: route === "" ? 1 : 0.8,
  }));
}
