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

export type InventoryGroup = {
  title: string;
  note?: string;
  bikes: Bike[];
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
