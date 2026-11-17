// Service price list shown on /service. Copied from the former Google Sheet
// embed (Repair Cost); edit here to change prices.

export type ServiceItem = {
  name: string;
  price: string;
  note?: string;
};

export type ServiceGroup = {
  title: string;
  items: ServiceItem[];
};

export const serviceGroups: ServiceGroup[] = [
  {
    title: "Tune-Ups",
    items: [
      { name: "Basic Tune-Up", price: "$89" },
      { name: "Standard Tune-Up", price: "$149" },
      { name: "Premium Tune-Up (Full Overhaul)", price: "$299" },
    ],
  },
  {
    title: "Shimano Drivetrain (Mechanical)",
    items: [
      { name: "Derailleur Adjustment", price: "$25" },
      { name: "Full Drivetrain Service", price: "$60" },
    ],
  },
  {
    title: "Shimano Di2 (Electronic)",
    items: [
      { name: "Setup / Pairing", price: "$45" },
      { name: "Full Di2 Service", price: "$85" },
    ],
  },
  {
    title: "SRAM Drivetrain (Mechanical)",
    items: [
      { name: "Derailleur Adjustment", price: "$25" },
      { name: "Full Drivetrain Service", price: "$60" },
    ],
  },
  {
    title: "SRAM AXS / eTap (Electronic)",
    items: [
      { name: "Setup / Pairing", price: "$45" },
      { name: "Full AXS Service", price: "$85" },
    ],
  },
  {
    title: "Campagnolo",
    items: [{ name: "Not Serviced", price: "N/A" }],
  },
  {
    title: "Brakes",
    items: [
      { name: "Mechanical Brake Adjustment", price: "$20" },
      { name: "Hydraulic Brake Bleed", price: "$45" },
      { name: "Brake Pad Replacement (Labor)", price: "$15" },
    ],
  },
  {
    title: "Wheels",
    items: [
      { name: "Wheel True - Minor", price: "$20" },
      { name: "Wheel True - Major", price: "$40" },
      {
        name: "Wheel Build (Customer Supplied Parts)",
        price: "$75",
        note: "per wheel",
      },
      { name: "Flat Repair / Tube Change", price: "$15" },
    ],
  },
  {
    title: "Drivetrain & Components",
    items: [
      { name: "Chain Replacement (Labor)", price: "$10" },
      { name: "Cassette Replacement (Labor)", price: "$10" },
      { name: "Headset Service", price: "$25" },
      { name: "Bottom Bracket Service", price: "$25" },
      { name: "Bar Tape / Grip Install", price: "$10" },
    ],
  },
  {
    title: "Bike Builds",
    items: [
      { name: "Basic Assembly (Box Bike)", price: "$125" },
      { name: "Full Custom Build", price: "$200" },
    ],
  },
];
