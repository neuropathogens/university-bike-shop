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
//      If someone else posted it, set `instagramAccount` (default
//      "universitybikes") so the embed is labeled with the right account.

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
  instagramAccount?: string;
};

export const events: ShopEvent[] = [
  {
    title: "Free Winter Safety Inspections",
    date: "2026-11-15",
    when: "November 15 – December 31, 2026",
    location: "Crescent Park, Palo Alto",
    role: "Organizer",
    description:
      "It gets dark by 5 now and the roads are wet, so we're offering free bike safety inspections for the rest of the year. We also put together Winter Commuting 101, a quick field guide for non-cyclists covering lights, visibility, braking on wet roads, riding in traffic, the ABC check (air, brakes, chain), and winter gear. Appointment only: DM us or call (650) 656-6807 to book.",
    instagram: "https://www.instagram.com/p/Dfyd5CMlefu/",
    // Long caption: sized to fit with no gap at phone and desktop widths.
    instagramSize: { media: 0.89, extra: 812 },
  },
  {
    title: "Paly Math Club Partnership",
    date: "2026-11-11",
    when: "November 2026",
    location: "Palo Alto High School",
    role: "Partner",
    description:
      "We partnered with Paly Math Club. Members get 15% off at University Bike Shop, plus free inspections and light tune-ups all school year with a valid student ID.",
    instagram: "https://www.instagram.com/p/Dfof5IMh5cO/",
    // Long caption: sized to fit with no gap at phone and desktop widths.
    instagramSize: { media: 1.07, extra: 425 },
    instagramAccount: "palymathclub",
  },
  {
    title: 'Featured in C Magazine\'s "Start It Up"',
    date: "2026-11-10",
    when: "November 2026",
    location: "C Magazine",
    role: "Press feature",
    description:
      'C Magazine featured University Bike Shop in its "Start It Up" series. Thank you to Derek Chen and Archer Sherry for telling our story.',
    instagram: "https://www.instagram.com/p/DfjdJRsxyGK/",
    instagramSize: { media: 1.25 },
  },
  {
    title: "300 Bikes Sold",
    date: "2026-11-01",
    when: "November 2026",
    location: "Palo Alto, CA",
    role: "Milestone",
    description:
      "We passed 300 bikes sold. Our first-ever sale was a Peloton, and our first bike went to Meghna S., a daily commuter who still rides it to school every day.",
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
    title: "PAUSD Back to School Bike Repair Events",
    date: "2026-08-01",
    when: "August 2026",
    location: "PAUSD middle and high schools",
    role: "Volunteer mechanics",
    description:
      "We volunteered with the Silicon Valley Bike Exchange at PAUSD's back-to-school bike repair events, giving students free tune-ups so their bikes were safe and ready for the commute to school. We went to every PAUSD middle and high school campus (Paly, Gunn, Fletcher, Greene, and JLS), with at least one of our team members at each event. The post below is from the first one, at Palo Alto High School.",
    instagram: "https://www.instagram.com/p/Db8xjcpGFNM/",
  },
  {
    title: "Free Tune-Up Week",
    date: "2026-06-02",
    when: "June 2–6, 2026",
    location: "Palo Alto, CA",
    role: "Organizer",
    description:
      "To kick off summer, we ran a week of free bike repairs and tune-ups for anyone who messaged us.",
    instagram: "https://www.instagram.com/p/DZELIMwB8PI/",
    // A reel, but Instagram's embed shows it cropped to 4:5.
    instagramSize: { media: 1.25 },
  },
];
