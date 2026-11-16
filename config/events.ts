// Past events shown on /events, newest first.
//
// To add an event:
//   1. Put its photos in public/events/<slug>/ (e.g. public/events/paly-repair-2026/1.jpg).
//   2. Add an entry below. `date` is YYYY-MM-DD and only used for sorting;
//      `when` is what visitors see ("August 2026", "June 15-19, 2026", ...).
//   3. Photo paths start with "/" and are relative to public/.
//   4. Optional: `instagram` is a post URL (https://www.instagram.com/p/<code>/)
//      embedded below the event. If the embed is cut off or has blank space
//      at the bottom, set `instagramSize`: `media` is the post's photo/video
//      height ÷ width (default 4/3 for portrait) and `extra` is the pixels of
//      header + caption below it (default 310; raise it for long captions).

export type EventPhoto = {
  src: string;
  alt: string;
};

export type ShopEvent = {
  title: string;
  date: string;
  when: string;
  location?: string;
  role?: string;
  description: string;
  photos?: EventPhoto[];
  link?: { href: string; label: string };
  instagram?: string;
  instagramSize?: { media?: number; extra?: number };
};

export const events: ShopEvent[] = [
  {
    title: "Partnership with Giant/Liv Guangzhou",
    date: "2026-07-07",
    when: "July 2026",
    location: "Guangzhou, China",
    role: "Partnership",
    description:
      "We partnered with a Giant/Liv bike store in Guangzhou, China. Through it we can order new Giant, Liv, and Look bikes without the usual US retail markup, and get high-end Shimano groupsets for 20% off.",
    instagram: "https://www.instagram.com/p/DafnyugFY-N/",
    instagramSize: { media: 0.5625, extra: 540 },
  },
  {
    title: "University Bike Shop Summer Camp",
    date: "2026-08-12",
    when: "August 2026",
    location: "Palo Alto, CA",
    role: "Organizer",
    description:
      "A completely free five-day bike camp we designed and ran ourselves. 22 kids signed up for 15 spots. Campers learned hands-on repair from our student mechanics, cleaning drivetrains, adjusting derailleurs, and tuning bikes, and every camper went home with a free bike, thanks to community bike donations.",
    photos: [
      { src: "/camp-photos/camp-01.jpg", alt: "Camper degreasing a chain, seen through the spokes of a Schwinn" },
      { src: "/camp-photos/camp-08.jpg", alt: "Camper with two mentors and the bike they went home with" },
      { src: "/camp-photos/camp-02.jpg", alt: "Camper adjusting a derailleur cable while a mentor watches" },
    ],
    link: { href: "/summer-camp", label: "More summer camp photos" },
  },
  {
    title: "Paly Back to School Bike Repair Event",
    date: "2026-08-01",
    when: "Back to school",
    location: "Palo Alto High School",
    role: "Volunteer mechanics",
    description:
      "We volunteered with the Silicon Valley Bike Exchange at Paly's back-to-school bike repair event, giving Palo Alto High School students free tune-ups so their bikes were safe and ready for the commute to school.",
    instagram: "https://www.instagram.com/p/Db8xjcpGFNM/",
  },
];
