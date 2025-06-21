"use client"

import Link from "next/link"
import Image from "next/image"
import { ChevronRight, MapPin, Star } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { HeaderImage } from "@/app/components/header-image"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section with corrected header image */}
      <HeaderImage
        title="The Jollof Guys"
        subtitle="Authentic West African Jollof Rice with a Modern flare in the Heart of New York City"
        height="h-[80vh]"
      >
        <div className="flex flex-col sm:flex-row gap-4">
          <Button asChild size="lg" className="bg-orange-600 hover:bg-orange-700">
            <Link href="/menu">View Our Menu</Link>
          </Button>
          <Button asChild size="lg" className="bg-orange-600 hover:bg-orange-700">
            <Link href="/contact">Book Catering</Link>
          </Button>
        </div>
      </HeaderImage>

      {/* Featured Dishes */}
      <section className="py-16 px-4 md:px-6 bg-orange-50">
        <div className="container mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">Our Signature Dishes</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card className="overflow-hidden border-none shadow-lg">
              <div className="relative h-64">
                <Image
                  src="/placeholder.svg?height=400&width=600"
                  alt="Classic Jollof Rice"
                  fill
                  className="object-cover"
                />
              </div>
              <CardContent className="p-6">
                <h3 className="text-xl font-bold mb-2">Classic Jollof Rice</h3>
                <p className="text-muted-foreground mb-4">
                  Our signature dish made with long-grain rice, tomatoes, peppers, and our secret spice blend.
                </p>
                <p className="font-semibold text-orange-600">$12.99</p>
              </CardContent>
            </Card>
            <Card className="overflow-hidden border-none shadow-lg">
              <div className="relative h-64">
                <Image
                  src="/placeholder.svg?height=400&width=600"
                  alt="Jollof Rice with Grilled Chicken"
                  fill
                  className="object-cover"
                />
              </div>
              <CardContent className="p-6">
                <h3 className="text-xl font-bold mb-2">Jollof Rice with Grilled Chicken</h3>
                <p className="text-muted-foreground mb-4">
                  Our classic jollof rice served with perfectly seasoned grilled chicken.
                </p>
                <p className="font-semibold text-orange-600">$16.99</p>
              </CardContent>
            </Card>
            <Card className="overflow-hidden border-none shadow-lg">
              <div className="relative h-64">
                <Image
                  src="/placeholder.svg?height=400&width=600"
                  alt="Seafood Jollof Rice"
                  fill
                  className="object-cover"
                />
              </div>
              <CardContent className="p-6">
                <h3 className="text-xl font-bold mb-2">Seafood Jollof Rice</h3>
                <p className="text-muted-foreground mb-4">
                  A luxurious version of our jollof rice with shrimp, calamari, and fish.
                </p>
                <p className="font-semibold text-orange-600">$19.99</p>
              </CardContent>
            </Card>
          </div>
          <div className="text-center mt-12">
            <Button asChild className="bg-orange-600 hover:bg-orange-700">
              <Link href="/menu">
                View Full Menu <ChevronRight className="ml-2 h-4 w-4" />
              </Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Rest of the home page content remains the same */}
      {/* Locations */}
      <section className="py-16 px-4 md:px-6">
        <div className="container mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">Find Us at NYC Street Markets</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card>
              <CardContent className="p-6 flex flex-col items-center text-center">
                <MapPin className="h-10 w-10 text-orange-600 mb-4" />
                <h3 className="text-xl font-bold mb-2">Uptown Night Market</h3>
                <p className="text-muted-foreground">Thursdays, 5pm - 11pm</p>
                <p className="text-muted-foreground">12th Avenue & 125th Street, Harlem</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6 flex flex-col items-center text-center">
                <MapPin className="h-10 w-10 text-orange-600 mb-4" />
                <h3 className="text-xl font-bold mb-2">Bronx Night Market</h3>
                <p className="text-muted-foreground">Saturdays, 12pm - 7pm</p>
                <p className="text-muted-foreground">Fordham Plaza, Bronx</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6 flex flex-col items-center text-center">
                <MapPin className="h-10 w-10 text-orange-600 mb-4" />
                <h3 className="text-xl font-bold mb-2">Queens Night Market</h3>
                <p className="text-muted-foreground">Saturdays, 5pm - 12am</p>
                <p className="text-muted-foreground">Flushing Meadows Corona Park</p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-16 px-4 md:px-6 bg-orange-50">
        <div className="container mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">What Our Customers Say</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card className="border-none shadow-lg">
              <CardContent className="p-6">
                <div className="flex items-center mb-4">
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                </div>
                <p className="text-muted-foreground mb-4">
                  "The best jollof rice I've had outside of West Africa! Authentic flavors and generous portions. Will
                  definitely be back!"
                </p>
                <div className="flex items-center">
                  <div className="relative w-10 h-10 rounded-full overflow-hidden mr-3">
                    <Image src="/placeholder.svg?height=100&width=100" alt="Customer" fill className="object-cover" />
                  </div>
                  <div>
                    <p className="font-semibold">Sarah Johnson</p>
                    <p className="text-sm text-muted-foreground">New York, NY</p>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card className="border-none shadow-lg">
              <CardContent className="p-6">
                <div className="flex items-center mb-4">
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                </div>
                <p className="text-muted-foreground mb-4">
                  "The Jollof Guys catered my birthday party and everyone was blown away! The food was amazing and the
                  service was top-notch."
                </p>
                <div className="flex items-center">
                  <div className="relative w-10 h-10 rounded-full overflow-hidden mr-3">
                    <Image src="/placeholder.svg?height=100&width=100" alt="Customer" fill className="object-cover" />
                  </div>
                  <div>
                    <p className="font-semibold">Michael Thompson</p>
                    <p className="text-sm text-muted-foreground">Brooklyn, NY</p>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card className="border-none shadow-lg">
              <CardContent className="p-6">
                <div className="flex items-center mb-4">
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                  <Star className="h-5 w-5 text-yellow-500 fill-yellow-500" />
                </div>
                <p className="text-muted-foreground mb-4">
                  "I discovered The Jollof Guys at Smorgasburg and I've been hooked ever since. Their seafood jollof
                  rice is to die for!"
                </p>
                <div className="flex items-center">
                  <div className="relative w-10 h-10 rounded-full overflow-hidden mr-3">
                    <Image src="/placeholder.svg?height=100&width=100" alt="Customer" fill className="object-cover" />
                  </div>
                  <div>
                    <p className="font-semibold">Aisha Williams</p>
                    <p className="text-sm text-muted-foreground">Queens, NY</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 px-4 md:px-6 bg-orange-600 text-white">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Experience Authentic Jollof Rice?</h2>
          <p className="text-xl mb-8 max-w-2xl mx-auto">
            Book us for your next event or visit us at one of our locations around NYC.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button
              size="lg"
              className="bg-white text-orange-600 hover:bg-orange-100 hover:text-orange-700 font-semibold border-2 border-white shadow-lg"
              onClick={() => (window.location.href = "/contact")}
            >
              Book Catering
            </Button>
            <Button asChild size="lg" className="bg-white text-orange-600 hover:bg-white/90">
              <Link href="/menu">View Our Menu</Link>
            </Button>
          </div>
        </div>
      </section>
    </div>
  )
}
