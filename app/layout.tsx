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
  title: "universitybikeshop.com",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={ibmPlexMono.variable}>
      <body>
        <Nav />
        <SalesNotice />
        {children}
        <Contact />
      </body>
    </html>
  );
}
