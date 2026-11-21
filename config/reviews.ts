// Customer reviews shown on /reviews.
//
// To add a review:
//   1. Copy the reviewer's words exactly (fix nothing but obvious typos).
//   2. `name` is what the review shows: first name + last initial
//      ("Meghna S."), or the first name alone when that's all we have.
//      Never a full name.
//   3. `source` is where the review was left. For Facebook Marketplace,
//      set `account` only if you know which seller account it is on, and copy
//      the review's "Notable" tags into `notable`.
//   4. `date` is YYYY-MM-DD or YYYY-MM if known; visitors see month + year.
//   5. A review not in English goes in `quote` with `lang` set (e.g. "zh-CN");
//      put the English in `translation`.
//   6. Optional: `link` points to the public post the review is from.
//
// To update the Facebook ratings, copy each seller account's star rating and
// count from its Marketplace profile into `facebookAccounts` and set
// `facebookAsOf` to that day. Sell Your Bike reads the totals from here too.

export type ReviewSource = "facebook" | "instagram";

export type Review = {
  quote: string;
  lang?: string;
  translation?: string;
  name: string;
  detail?: string;
  source: ReviewSource;
  account?: string;
  notable?: string[];
  rating?: number;
  date?: string;
  link?: string;
};

export type SellerAccount = {
  name: string;
  rating: number;
  count: number;
  strengths?: { label: string; count: number }[];
};

export const facebookAsOf = "2026-11-21";

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
];

export const facebookRatingCount = facebookAccounts.reduce(
  (sum, account) => sum + account.count,
  0,
);

export const reviews: Review[] = [
  {
    quote:
      "Excellent experience. Seller was friendly, communicative, and punctual. Bike was exactly as described — smooth and easy transaction.",
    name: "Giovanni",
    source: "facebook",
    notable: ["Communication", "Pricing", "Item Description"],
    rating: 5,
    date: "2026-04-02",
  },
  {
    quote: "Knowledgeable and helpful",
    name: "Ulises",
    source: "facebook",
    notable: ["Punctuality", "Communication", "Pricing", "Item Description"],
    rating: 5,
    date: "2026-08-30",
  },
  {
    quote:
      "It's a great bike, especially because I could order my size (XXS) at a discount. It's been super good and fast, and takes me to work every day! The staff at University Bikes have also been super kind and nice to work with!",
    name: "Dennis F.",
    detail:
      "2026 Liv Avail AR 2, bought in August through our Giant Guangzhou program",
    source: "instagram",
    rating: 5,
  },
  {
    quote:
      "这款车给人的第一印象就是快速而稳定。车架具有良好的刚性，加速响应直接。在高速下坡和弯道中表现稳定。",
    lang: "zh-CN",
    translation:
      "My first impression of this bike is that it's fast and stable. The frame is nicely stiff, and it responds directly when you accelerate. It stays stable on fast descents and through corners.",
    name: "Ming",
    detail: "2026 Giant Propel Advanced 2, bought in August",
    source: "instagram",
  },
  {
    quote:
      "University Bikes sold me a great bike at a very generous price. I ride it to school every single day and it hasn't failed me once. It's extremely smooth, and I'm so grateful!",
    name: "Meghna S.",
    detail: "Daily commuter, our very first bike sale",
    source: "instagram",
    rating: 5,
  },
  {
    quote:
      "University Bikes found this bike rusting on the side of a street and rebuilt it from scratch. Now it's my daily commuter, and they donated it to me for free!",
    name: "Ryan S.",
    detail: "UC Berkeley student",
    source: "instagram",
    rating: 5,
  },
];
