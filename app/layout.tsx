import type { Metadata } from "next";
import { IBM_Plex_Mono } from "next/font/google";
import Nav from "@/components/Nav";
import SalesNotice from "@/components/SalesNotice";
import Contact from "@/components/Contact";
import "./globals.css";

const ibmPlexMono = IBM_Plex_Mono({
  variable: "--font-ibm-plex-mono",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://universitybikeshop.com"),
  title: {
    default:
      "University Bike Shop | Used Road, Gravel & Triathlon Bikes in Palo Alto",
    template: "%s | University Bike Shop",
  },
  description:
    "Student-run bike shop in Palo Alto, CA selling quality used road, gravel, triathlon, and mountain bikes at low prices. Repairs, tune-ups, $99 bike fits, and bike consignment. By appointment in Crescent Park.",
  openGraph: {
    type: "website",
    siteName: "University Bike Shop",
    url: "https://universitybikeshop.com",
  },
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
  sameAs: ["https://www.instagram.com/universitybikes"],
  description:
    "Student-run bike shop in Palo Alto, CA selling used road, gravel, triathlon, and mountain bikes, with repairs, tune-ups, and bike fits by appointment.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={ibmPlexMono.variable}>
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
