// Bike inventory shown on /inventory. Copied from the former Google Sheet
// embed (Available Bikes); edit here to change what's listed.
//
// A group with no `note` and no `bikes` is hidden, so "Currently Undergoing
// Repairs" only shows up once a bike is added to it.

export type Bike = {
  brand: string;
  model?: string;
  size: string;
  frame: string;
  speeds: string;
  groupset: string;
  wheels: string;
  price: string;
  note?: string;
};

// New bikes ordered through Giant (2027 line). `price` is ours (15% off
// MSRP); leave both out when the US MSRP isn't posted yet.
export type NewBike = {
  name: string;
  type?: string;
  msrp?: string;
  price?: string;
  // Path under public/; 960x540 product shot cropped from the promo poster.
  photo?: string;
};

export type NewBikeSection = {
  title: string;
  bikes: NewBike[];
};

export type InventoryGroup = {
  title: string;
  note?: string;
  bikes: Bike[];
  newBikes?: NewBikeSection[];
};

export const inventoryGroups: InventoryGroup[] = [
  {
    title: "Commuters",
    note: "$75 each, depends on sizing. Most spec approximately the same. 13 in stock right now.",
    bikes: [],
  },
  {
    title: "New Giant Bikes",
    note: "15% off retail pricing, 1 month turnaround direct from China.",
    bikes: [],
    newBikes: [
      {
        title: "Road",
        bikes: [
          { name: "Giant TCR Advanced Pro Dura-Ace", type: "Race", msrp: "$8,300", price: "$7,055", photo: "/bikes/giant-2027/tcr-advanced-pro-dura-ace.webp" },
          { name: "Giant TCR Advanced Pro 0-AXS", type: "Race", msrp: "$7,000", price: "$5,950", photo: "/bikes/giant-2027/tcr-advanced-pro-0-axs.webp" },
          { name: "Giant Propel Advanced Pro-DA", type: "Aero race", msrp: "$8,000", price: "$6,800", photo: "/bikes/giant-2027/propel-advanced-pro-da.webp" },
          { name: "Giant Propel Advanced Pro 0-AXS", type: "Aero race", msrp: "$7,800", price: "$6,630", photo: "/bikes/giant-2027/propel-advanced-pro-0-axs.webp" },
          { name: "Giant Propel Advanced 1", type: "Aero race", msrp: "$5,300", price: "$4,505", photo: "/bikes/giant-2027/propel-advanced-1.webp" },
          { name: "Giant Propel Advanced 2", type: "Aero race", msrp: "$3,500", price: "$2,975", photo: "/bikes/giant-2027/propel-advanced-2.webp" },
          { name: "Giant Propel Advanced Pro Frameset", type: "Aero race, frameset", msrp: "$3,200", price: "$2,720", photo: "/bikes/giant-2027/propel-advanced-pro-frameset.webp" },
          { name: "Giant Defy Advanced Pro 0-AXS", type: "Endurance", msrp: "$7,700", price: "$6,545", photo: "/bikes/giant-2027/defy-advanced-pro-0-axs.webp" },
          { name: "Giant Defy Advanced 2", type: "Endurance", msrp: "$3,300", price: "$2,805", photo: "/bikes/giant-2027/defy-advanced-2.webp" },
          { name: "Giant Defy Advanced 4", type: "Endurance", msrp: "$2,300", price: "$1,955", photo: "/bikes/giant-2027/defy-advanced-4.webp" },
        ],
      },
      {
        title: "Gravel",
        bikes: [
          { name: "Giant Revolt Advanced SL 0", photo: "/bikes/giant-2027/revolt-advanced-sl-0.webp" },
          { name: "Giant Revolt Advanced SL 1", photo: "/bikes/giant-2027/revolt-advanced-sl-1.webp" },
          { name: "Giant Revolt Advanced SL 2", photo: "/bikes/giant-2027/revolt-advanced-sl-2.webp" },
          { name: "Giant Revolt Advanced SL Frameset", type: "Frameset", photo: "/bikes/giant-2027/revolt-advanced-sl-frameset.webp" },
        ],
      },
      {
        title: "Mountain",
        bikes: [
          { name: "Giant Anthem Advanced SL 2", type: "Cross-country", msrp: "$5,600", price: "$4,760", photo: "/bikes/giant-2027/anthem-advanced-sl-2.webp" },
          { name: "Giant Anthem Advanced Pro", type: "Cross-country", msrp: "$4,000", price: "$3,400", photo: "/bikes/giant-2027/anthem-advanced-pro.webp" },
          { name: "Giant Stance 0", type: "Trail", msrp: "$2,900", price: "$2,465", photo: "/bikes/giant-2027/stance-0.webp" },
        ],
      },
      {
        title: "E-Bike",
        bikes: [
          { name: "Giant Trance Advanced E+ 0", type: "Electric mountain", msrp: "$10,000", price: "$8,500", photo: "/bikes/giant-2027/trance-advanced-e-plus-0.webp" },
          { name: "Giant Trance Advanced E+ 1", type: "Electric mountain", msrp: "$8,000", price: "$6,800", photo: "/bikes/giant-2027/trance-advanced-e-plus-1.webp" },
          { name: "Giant Trance Advanced E+ SE", type: "Electric mountain", msrp: "$6,500", price: "$5,525", photo: "/bikes/giant-2027/trance-advanced-e-plus-se.webp" },
          { name: "Giant Stance E+ 0", type: "Electric mountain", msrp: "$5,500", price: "$4,675", photo: "/bikes/giant-2027/stance-e-plus-0.webp" },
          { name: "Giant Stance E+ 1", type: "Electric mountain", msrp: "$4,500", price: "$3,825", photo: "/bikes/giant-2027/stance-e-plus-1.webp" },
          { name: "Giant Talon E+ 2 EX", type: "Electric mountain", msrp: "$3,300", price: "$2,805", photo: "/bikes/giant-2027/talon-e-plus-2-ex.webp" },
          { name: "Giant Talon E+ 2", type: "Electric mountain", msrp: "$2,950", price: "$2,507.50", photo: "/bikes/giant-2027/talon-e-plus-2.webp" },
        ],
      },
    ],
  },
  {
    title: "Road",
    bikes: [
      {
        brand: "Scott",
        model: "Foil RC 30 Rim",
        size: "52",
        frame: "Carbon",
        speeds: "2x11",
        groupset: "Dura-Ace/Ultegra Di2 mix",
        wheels: "Aluminum",
        price: "$1,699",
      },
      {
        brand: "Cervelo",
        model: "R5 SL 2018 Rim",
        size: "56",
        frame: "Carbon",
        speeds: "2x11",
        groupset: "Ultegra mechanical",
        wheels: "Aluminum",
        price: "$1,499",
      },
      {
        brand: "Cervelo",
        model: "R3 Rim (custom paint)",
        size: "54",
        frame: "Carbon",
        speeds: "2x11",
        groupset: "Ultegra mechanical",
        wheels: "Aluminum",
        price: "$1,199",
      },
      {
        brand: "Specialized",
        model: "S-Works Tarmac Disc",
        size: "52",
        frame: "Carbon",
        speeds: "2x11",
        groupset: "Ultegra Di2",
        wheels: "Carbon (Roval)",
        price: "$3,699",
        note: "Comes with power meter pedals",
      },
      {
        brand: "Cannondale",
        model: "CAAD13 Disc",
        size: "58",
        frame: "Aluminum",
        speeds: "2x11",
        groupset: "105",
        wheels: "Aluminum",
        price: "$1,750",
      },
    ],
  },
  {
    title: "Gravel",
    bikes: [
      {
        brand: "Giant",
        model: "TCX Advanced Pro 0",
        size: "54",
        frame: "Carbon",
        speeds: "1x11",
        groupset: "SRAM Red eTap",
        wheels: "Aluminum?",
        price: "$1,999",
      },
      {
        brand: "Specialized",
        model: "Diverge Comp 2023",
        size: "58",
        frame: "Carbon",
        speeds: "2x12",
        groupset: "105 Di2",
        wheels: "DT Swiss R470",
        price: "$2,499",
      },
    ],
  },
  {
    title: "Tri/TT",
    bikes: [
      {
        brand: "BMC",
        size: "58",
        frame: "Carbon",
        speeds: "2x10",
        groupset: "Ultegra/105 mix",
        wheels: "Aluminum",
        price: "$999",
      },
      {
        brand: "Blue",
        size: "52",
        frame: "Carbon",
        speeds: "2x10",
        groupset: "SRAM Red (Rival brakes)",
        wheels: "Aluminum",
        price: "$1,249",
      },
    ],
  },
  {
    title: "MTB",
    bikes: [
      {
        brand: "Giant",
        model: "Trance 2",
        size: "Large",
        frame: "Aluminum",
        speeds: "3x10",
        groupset: "Deore",
        wheels: "Aluminum",
        price: "$599",
      },
      {
        brand: "Specialized",
        size: "Women's Small",
        frame: "Aluminum",
        speeds: "3x8",
        groupset: "Lowest-end Shimano",
        wheels: "Aluminum",
        price: "$299",
      },
    ],
  },
  {
    title: "Currently Undergoing Repairs",
    bikes: [],
  },
];

export const inventoryFootnote =
  "All bikes with electronic shifting will come with either a charger or a charging adapter (compatible with USB-C).";
