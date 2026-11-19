// Customer reviews shown on /reviews, in the order listed here.
//
// To add a review:
//   1. Copy the reviewer's words exactly (fix nothing but obvious typos).
//   2. `name` is first name + last initial ("Meghna S."), never a full name.
//   3. `source` is where the review was left. For Facebook Marketplace,
//      `account` is which of our seller accounts it was left on.
//   4. `date` is YYYY-MM or YYYY-MM-DD if known; visitors see month + year.
//   5. Optional: `link` points to the public post (Instagram) the review is from.

export type ReviewSource = "facebook" | "instagram";

export type Review = {
  quote: string;
  name: string;
  detail?: string;
  source: ReviewSource;
  account?: string;
  rating?: number;
  date?: string;
  link?: string;
};

export const sourceLabels: Record<ReviewSource, string> = {
  facebook: "Facebook Marketplace",
  instagram: "Instagram",
};

export const reviews: Review[] = [
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
