import { Inter } from "next/font/google"
import Link from "next/link"

import { ThemeProvider } from "@/components/theme-provider"
import { Logo } from "@/app/components/logo"
import { Button } from "@/components/ui/button"
import "./globals.css"

const inter = Inter({ subsets: ["latin"] })

export const metadata = {
  title: "The Jollof Guys - Authentic West African Jollof Rice in NYC",
  description:
    "The Jollof Guys serve authentic West African jollof rice at NYC street markets and cater private events. Experience the rich flavors of West Africa in New York City.",
  icons: {
    icon: "/favicon.png",
    shortcut: "/favicon.png",
    apple: "/favicon.png",
  },
    generator: 'v0.dev'
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.png" type="image/png" />
        <link rel="shortcut icon" href="/favicon.png" type="image/png" />
        <link rel="apple-touch-icon" href="/favicon.png" />
      </head>
      <body className={inter.className}>
        <ThemeProvider attribute="class" defaultTheme="light">
          <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur">
            <div className="container flex h-24 items-center px-4">
              <Link href="/" className="flex items-center gap-2 sm:gap-3">
                <Logo size="md" />
              </Link>
              <nav className="ml-auto flex items-center gap-2 sm:gap-4 lg:gap-6">
                <Link href="/" className="text-sm font-medium hover:text-orange-600 hover:underline underline-offset-4">
                  Home
                </Link>
                <Link
                  href="/about"
                  className="text-sm font-medium hover:text-orange-600 hover:underline underline-offset-4"
                >
                  About
                </Link>
                <Link
                  href="/menu"
                  className="text-sm font-medium hover:text-orange-600 hover:underline underline-offset-4"
                >
                  Menu
                </Link>
                <Link
                  href="/contact"
                  className="text-sm font-medium hover:text-orange-600 hover:underline underline-offset-4"
                >
                  Contact
                </Link>
                <Button size="sm" className="bg-orange-600 text-white hover:bg-orange-700 ml-1 sm:ml-2">
                  <Link href="/contact" className="text-white">
                    Book Catering
                  </Link>
                </Button>
              </nav>
            </div>
          </header>
          {children}
          <footer className="border-t bg-orange-50">
            <div className="container py-6 sm:py-8 md:py-12 px-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6 sm:gap-8">
                <div className="col-span-1 sm:col-span-2 md:col-span-1">
                  <Link href="/" className="flex items-center gap-2 sm:gap-3 mb-4">
                    <Logo size="sm" />
                  </Link>
                  <p className="text-sm text-muted-foreground">
                    Authentic West African jollof rice in the heart of New York City.
                  </p>
                </div>
                <div>
                  <h3 className="font-semibold mb-4">Quick Links</h3>
                  <ul className="space-y-2">
                    <li>
                      <Link href="/" className="text-sm text-muted-foreground hover:text-orange-600">
                        Home
                      </Link>
                    </li>
                    <li>
                      <Link href="/about" className="text-sm text-muted-foreground hover:text-orange-600">
                        About
                      </Link>
                    </li>
                    <li>
                      <Link href="/menu" className="text-sm text-muted-foreground hover:text-orange-600">
                        Menu
                      </Link>
                    </li>
                    <li>
                      <Link href="/contact" className="text-sm text-muted-foreground hover:text-orange-600">
                        Contact
                      </Link>
                    </li>
                  </ul>
                </div>
                <div>
                  <h3 className="font-semibold mb-4">Contact</h3>
                  <ul className="space-y-2">
                    <li className="text-sm text-muted-foreground">Phone: (646) 879-0914</li>
                    <li className="text-sm text-muted-foreground">Email: onyelv@gmail.com</li>
                  </ul>
                </div>
                <div>
                  <h3 className="font-semibold mb-4">Follow Us</h3>
                  <div className="flex space-x-4">
                    <a
                      href="https://www.instagram.com/thejollofguys"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-muted-foreground hover:text-orange-600"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-5 w-5"
                      >
                        <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                        <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                        <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                      </svg>
                      <span className="sr-only">Instagram</span>
                    </a>
                  </div>
                </div>
              </div>
              <div className="border-t mt-6 sm:mt-8 pt-6 sm:pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p className="text-xs text-muted-foreground text-center md:text-left">
                  &copy; {new Date().getFullYear()} The Jollof Guys. All rights reserved.
                </p>
                <div className="flex gap-4">
                  <Link href="#" className="text-xs text-muted-foreground hover:text-orange-600">
                    Privacy Policy
                  </Link>
                  <Link href="#" className="text-xs text-muted-foreground hover:text-orange-600">
                    Terms of Service
                  </Link>
                </div>
              </div>
            </div>
          </footer>
        </ThemeProvider>
      </body>
    </html>
  )
}
