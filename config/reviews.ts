// What /reviews shows: our Facebook Marketplace seller ratings and the
// Rider Spotlight posters from our Instagram.
//
// When you change anything here, set `lastUpdated` to the current time
// (ISO 8601 with the Pacific offset, e.g. "2026-11-21T09:24:00-08:00").
//
// Facebook ratings: copy each seller account's star rating and count from its
// Marketplace profile. Sell Your Bike reads the totals from here too.
//
// Rider Spotlights: export the Instagram poster, convert it to WebP (1080 px
// wide for 4:5 posts) into public/spotlights/<slug>.webp, and add an entry
// below. `alt` carries the poster's words for screen readers.

export const lastUpdated = "2026-11-21T09:24:00-08:00";

export type SellerAccount = {
  name: string;
  rating: number;
  count: number;
  note?: string;
  strengths?: { label: string; count: number }[];
};

export const facebookAccounts: SellerAccount[] = [
  { name: "Talon Zhang", rating: 4.9, count: 151 },
  {
    name: "Paul Wang",
    rating: 4.9,
    count: 56,
    strengths: [
      { label: "Communication", count: 27 },
      { label: "Punctuality", count: 21 },
      { label: "Item description", count: 14 },
      { label: "Pricing", count: 8 },
    ],
  },
  { name: "Kai Russel", rating: 4.6, count: 42 },
  {
    name: "Everett Keninger",
    rating: 4.9,
    count: 30,
    note: "account no longer active",
  },
];

export const facebookRatingCount = facebookAccounts.reduce(
  (sum, account) => sum + account.count,
  0,
);

export type Spotlight = {
  src: string;
  width: number;
  height: number;
  alt: string;
};

export const spotlights: Spotlight[] = [
  {
    src: "/spotlights/dennis.webp",
    width: 1080,
    height: 1350,
    alt: "Rider Spotlight, five stars: “It's a great bike, especially because I could order my size (XXS) at a discount. It's been super good and fast, and takes me to work every day! The staff at University Bikes have also been super kind and nice to work with!” Dennis F., 2026 Liv Avail AR 2, bought in August through our Giant Guangzhou program.",
  },
  {
    src: "/spotlights/ming.webp",
    width: 1350,
    height: 1000,
    alt: "Rider Spotlight, in Chinese: “My first impression of this bike is that it's fast and stable. The frame is nicely stiff, and it responds directly when you accelerate. It stays stable on fast descents and through corners.” Ming, 2026 Giant Propel Advanced 2, bought in August.",
  },
  {
    src: "/spotlights/meghna.webp",
    width: 1080,
    height: 1350,
    alt: "Rider Spotlight, five stars: “University Bikes sold me a great bike at a very generous price. I ride it to school every single day and it hasn't failed me once. It's extremely smooth, and I'm so grateful!” Meghna S., daily commuter, our very first bike sale.",
  },
  {
    src: "/spotlights/ryan.webp",
    width: 1080,
    height: 1350,
    alt: "Rider Spotlight, five stars: “University Bikes found this bike rusting on the side of a street and rebuilt it from scratch. Now it's my daily commuter, and they donated it to me for free!” Ryan S., UC Berkeley student.",
  },
];
