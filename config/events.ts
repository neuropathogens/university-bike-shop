// Past events shown on /events, newest first.
//
// To add an event:
//   1. Put its photos in public/events/<slug>/ (e.g. public/events/paly-repair-2026/1.jpg).
//   2. Add an entry below. `date` is YYYY-MM-DD and only used for sorting;
//      `when` is what visitors see ("August 2026", "June 15-19, 2026", ...).
//   3. Photo paths start with "/" and are relative to public/.

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
};

export const events: ShopEvent[] = [
  {
    title: "University Bike Shop Summer Camp",
    date: "2026-07-01",
    when: "Summer 2026",
    location: "Palo Alto, CA",
    role: "Organizer",
    description:
      "A 5-day bike camp we ran with our own curriculum. Campers learned hands-on bike maintenance and repair: adjusting derailleurs, truing and cleaning wheels, and washing and tuning their own bikes.",
    photos: [
      { src: "/summer-camp-group.jpg", alt: "Summer camp campers with their bikes" },
      { src: "/summer-camp-wheel.jpg", alt: "Camper adjusting a rear derailleur" },
      { src: "/summer-camp-tent.jpg", alt: "Campers gathered under a canopy" },
      { src: "/summer-camp-spray.jpg", alt: "Camper using a pressure washer on a bike" },
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
      "We volunteered as mechanics at Paly's back-to-school bike repair event, getting students' bikes safe and ready for the commute to school.",
  },
];
