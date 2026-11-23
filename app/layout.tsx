import type { Metadata, Viewport } from "next";
import localFont from "next/font/local";
import Nav from "@/components/Nav";
import SalesNotice from "@/components/SalesNotice";
import Contact from "@/components/Contact";
import "./globals.css";

// Latin Modern (the LaTeX / Computer Modern look), self-hosted.
const latinModern = localFont({
  variable: "--font-latin-modern",
  display: "swap",
  src: [
    { path: "./fonts/LM-regular.woff2", weight: "400", style: "normal" },
    { path: "./fonts/LM-italic.woff2", weight: "400", style: "italic" },
    { path: "./fonts/LM-bold.woff2", weight: "700", style: "normal" },
    { path: "./fonts/LM-bold-italic.woff2", weight: "700", style: "italic" },
  ],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://universitybikeshop.com"),
  title: {
    default:
      "University Bike Shop | Used Road, Gravel & Triathlon Bikes in Palo Alto",
    template: "%s | University Bike Shop",
  },
  description:
    "Student-run bike shop in Palo Alto, CA selling quality used road, gravel, triathlon, and mountain bikes at low prices. Repairs, tune-ups, bike fits (free while we test V3, $99 after), and bike consignment. By appointment in Crescent Park.",
  openGraph: {
    type: "website",
    siteName: "University Bike Shop",
    url: "https://universitybikeshop.com",
  },
};

export const viewport: Viewport = {
  themeColor: "#000000",
};

const localBusinessJsonLd = {
  "@context": "https://schema.org",
  "@type": "BikeStore",
  name: "University Bike Shop",
  url: "https://universitybikeshop.com",
  email: "universitybikeshop@gmail.com",
  telephone: "+1-650-656-6807",
  address: {
    "@type": "PostalAddress",
    addressLocality: "Palo Alto",
    addressRegion: "CA",
    addressCountry: "US",
  },
  sameAs: [
    "https://www.instagram.com/universitybikes",
    "https://www.linkedin.com/company/144140744/",
  ],
  description:
    "Student-run bike shop in Palo Alto, CA selling used road, gravel, triathlon, and mountain bikes, with repairs, tune-ups, and bike fits by appointment.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={latinModern.variable}>
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(localBusinessJsonLd) }}
        />
        <Nav />
        <SalesNotice />
        {children}
        <Contact />
      </body>
    </html>
  );
}
