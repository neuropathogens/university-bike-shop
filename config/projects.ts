// Projects shown on /projects, in the order listed here.
//
// To add a project, add an entry below. Images go in public/projects/.
// `instagram` / `instagramSize` work the same way as in config/events.ts.

export type ProjectImage = {
  src: string;
  alt: string;
};

export type Project = {
  title: string;
  tagline: string;
  status: string;
  started?: string;
  description: string;
  highlights?: string[];
  images?: ProjectImage[];
  links?: { href: string; label: string }[];
  instagram?: string;
  instagramSize?: { media?: number; extra?: number };
};

export const projects: Project[] = [
  {
    title: "bikeparts",
    tagline: "Open-source 3D-printable bike accessories",
    status: "3 parts designed and passing automated checks; physical testing next",
    started: "November 2026",
    description:
      "An open-source library of bike accessories modeled entirely in code, so every part can be resized for different bikes. Every part prints without supports, comes with a recommended material and print orientation chosen for how it is loaded, and has to pass automated geometry checks, a stress simulation (for parts that carry load), and a physical test before release. Accessories only: nothing in the rider's main load path.",
    highlights: [
      "Ghost tracker spacer: hides an AirTag between the frame and bottle cage",
      "Vault bar-end plug: a wedge-locking handlebar plug that stores a tubeless repair kit",
      "Shop dummy hub: holds the dropouts and keeps the chain running while a bike ships without its rear wheel, for 8 axle standards",
      "Calibration coupon that measures your printer's real tolerances and feeds them into every part",
    ],
    images: [
      { src: "/projects/bikeparts-tracker-spacer.svg", alt: "3D view drawing of the Ghost tracker spacer" },
      { src: "/projects/bikeparts-bar-end-vault.svg", alt: "3D view drawing of the Vault bar-end plug body" },
      { src: "/projects/bikeparts-dummy-hub.svg", alt: "3D view drawing of the shop dummy hub body" },
    ],
    links: [{ href: "https://github.com/neuropathogens/bikeparts", label: "Source on GitHub" }],
  },
  {
    title: "University Bike Fits",
    tagline: "Video bike-fit analysis software",
    status: "V3 in testing; free fits while we validate",
    started: "October 2026",
    description:
      "Our own fit-analysis software. A rider pedals on a smart roller while we film two short passes, one from the side and one from the front. The software tracks the rider's joints in every frame with open-source markerless pose estimation, measures their angles over at least 15 pedal strokes, compares them with target ranges, and produces a fit report with plain-language next steps. It is a tool to support the fitter's judgment, not replace it.",
    highlights: [
      "12 measurements from two camera views: knee, hip, torso, shoulder, elbow and ankle angles, knee travel, pelvic rock, and cadence",
      "Annotated overlay video, PDF report, and before/after comparison: change the saddle, record again, see exactly what moved",
      "Rider profiles and session history; runs locally on one shop laptop, no cloud required",
      "Every target range and suggestion lives in one config file, so the fit protocol can be tuned without touching code",
    ],
    images: [
      { src: "/projects/bike-fits-01.jpg", alt: "Diagram of a rider on a bike with torso, elbow and knee angles marked" },
      { src: "/projects/bike-fits-03.jpg", alt: "List of the 12 measurements from the side and front camera views" },
    ],
    links: [{ href: "/bike-fits", label: "Book a free bike fit (free while we test V3, $99 after)" }],
  },
  {
    title: "3D-Printable Mountain Bike",
    tagline: "Launch with designer Kai Russel",
    status: "Released October 2026",
    started: "October 2026",
    description:
      "We teamed up with designer Kai Russel to launch his 3D-printable mountain bike: 29 printable parts, including a working suspension fork, linkage, and shock. We produced the launch reels and released the STL file for $4.99.",
    instagram: "https://www.instagram.com/p/DfFw0xSSEdE/",
  },
  {
    title: "Rider Spotlight",
    tagline: "Customer reviews, one bike at a time",
    status: "Ongoing",
    started: "November 2026",
    description:
      "A series where customers tell us how their bikes are holding up, months after they bought them. Bike #001 went to Meghna S. in January, and she still rides it to school every day.",
    highlights: [
      "Each post features a real customer, their bike, and their review",
      "Includes riders on bikes from our donation program",
    ],
    instagram: "https://www.instagram.com/p/Df6Zm10MDf6/",
    instagramSize: { media: 1.25, extra: 290 },
  },
  {
    title: "Giant/Liv Direct Import",
    tagline: "New bikes and parts without the US retail markup",
    status: "Active",
    started: "July 2026",
    description:
      "Through our partnership with a Giant/Liv store in Guangzhou, we can order new Giant, Liv, and Look bikes without the usual US retail markup, and high-end Shimano groupsets at 20% off. Albert Xu runs the partnership and also imports parts for the shop. Message us if you're interested in a new bike.",
    instagram: "https://www.instagram.com/p/DafnyugFY-N/",
    instagramSize: { media: 0.5625, extra: 540 },
  },
  {
    title: "Commuter Bike Donations",
    tagline: "Refurbished commuter bikes for people who need a ride",
    status: "Ongoing · 50+ bikes donated",
    description:
      "We source entry-level commuter bikes, refurbish them, and donate them to students and others who need a way to get to school or work. Every bike stays out of the landfill. Our engineers have come up with fixes that make these entry-level bikes sturdier and longer-lasting than when they came in.",
    highlights: [
      "50+ entry-level commuter bikes refurbished and donated so far",
      "Ethan Zhang sources the bikes; Reed Truong designs durability fixes for them",
      "Donated bikes are still on the road: see Ryan's review below",
    ],
    instagram: "https://www.instagram.com/p/Df6ZUdqsEiA/",
    instagramSize: { media: 1.25 },
  },
  {
    title: "Building the Shop",
    tagline: "From storage garage to working bike shop",
    status: "March–April 2026 · Complete",
    description:
      "University Bike Shop started in a garage that was used for storage. Over about 40 hours, Paul, Asher (our first employee), and Kai, with help from Kevin, turned it into a working shop: we built a shed and moved everything stored in the garage into it, bought and built bike and wheel racks, and bought the tools and repair stands a real shop needs.",
    highlights: [
      "About 40 hours of build-out by a crew of three, plus help from Kevin",
      "Built a shed and moved everything stored in the garage into it",
      "Bought and built bike racks and wheel racks",
      "Bought the tools and repair stands for a full working shop",
    ],
    instagram: "https://www.instagram.com/p/De0uf7Tmw2j/",
    // Long caption: sized to fit with no gap at phone and desktop widths.
    instagramSize: { media: 0.69, extra: 808 },
  },
  {
    title: "Bike-Deal Finder",
    tagline: "Real-time alerts for underpriced bikes",
    status: "Running daily",
    started: "February 2026",
    description:
      "An automated system that runs around the clock on our shop PC, watching Craigslist, Facebook Marketplace, and Pinkbike. When an underpriced bike is listed, it alerts the team right away so we can reach the seller first. Faster sourcing is a big part of how the shop grew.",
    highlights: [
      "Watches Craigslist, Facebook Marketplace, and Pinkbike listings in real time",
      "Sends instant alerts to the team when a bike is listed under market value",
      "Built by Ethan Zhang, Albert Xu, and David Fridshtand",
    ],
  },
];
