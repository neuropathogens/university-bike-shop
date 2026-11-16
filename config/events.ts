// Past events shown on /events, newest first.
//
// To add an event:
//   1. Put its photos in public/events/<slug>/ (e.g. public/events/paly-repair-2026/1.jpg).
//   2. Add an entry below. `date` is YYYY-MM-DD and only used for sorting;
//      `when` is what visitors see ("August 2026", "June 15-19, 2026", ...).
//   3. Photo paths start with "/" and are relative to public/.
//   4. Optional: `instagram` is a post URL (https://www.instagram.com/p/<code>/)
//      embedded below the event.

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
};

export const events: ShopEvent[] = [
  {
    title: "3D-Printable Mountain Bike Launch",
    date: "2026-10-29",
    when: "October 2026",
    location: "Online",
    role: "Launch & promotion",
    description:
      "We teamed up with designer Kai Russel to launch his 3D-printable mountain bike: 29 printable parts, including a working suspension fork, linkage, and shock. We produced the launch reels and released the STL file for $4.99.",
    instagram: "https://www.instagram.com/p/DfFw0xSSEdE/",
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
