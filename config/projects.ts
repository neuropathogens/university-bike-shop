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
    title: "University Bike Fits",
    tagline: "Video bike-fit analysis software",
    status: "Built; validating against real fit sessions",
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
    links: [{ href: "/bike-fits", label: "Book a $99 bike fit" }],
  },
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
    title: "3D-Printable Mountain Bike",
    tagline: "Launch with designer Kai Russel",
    status: "Released October 2026",
    started: "October 2026",
    description:
      "We teamed up with designer Kai Russel to launch his 3D-printable mountain bike: 29 printable parts, including a working suspension fork, linkage, and shock. We produced the launch reels and released the STL file for $4.99.",
    instagram: "https://www.instagram.com/p/DfFw0xSSEdE/",
  },
];
