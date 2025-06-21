import Image from "next/image"
import Link from "next/link"

import { Button } from "@/components/ui/button"
import { HeaderImage } from "@/app/components/header-image"

export default function AboutPage() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section with corrected header image */}
      <HeaderImage title="About Us" subtitle="The story behind New York's favorite jollof rice" />

      {/* Rest of the about page content remains the same */}
      {/* Our Story */}
      <section className="py-16 px-4 md:px-6">
        <div className="container mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold mb-6">Our Story</h2>
              <p className="text-lg text-muted-foreground mb-6">
                The Jollof Guys was founded in 2018 by three friends who shared a passion for authentic West African
                cuisine and a desire to introduce New Yorkers to the rich, flavorful world of jollof rice.
              </p>
              <p className="text-lg text-muted-foreground mb-6">
                What started as a small pop-up at local food markets quickly grew into one of the most sought-after food
                vendors in NYC. Our commitment to using traditional recipes, fresh ingredients, and cooking techniques
                passed down through generations has earned us a dedicated following.
              </p>
              <p className="text-lg text-muted-foreground">
                Today, we continue to serve our signature jollof rice at various locations throughout New York City, as
                well as catering private events and celebrations.
              </p>
            </div>
            <div className="relative h-[400px] rounded-lg overflow-hidden shadow-xl">
              <Image
                src="/placeholder.svg?height=800&width=600"
                alt="Founders of The Jollof Guys"
                fill
                className="object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Our Mission */}
      <section className="py-16 px-4 md:px-6 bg-orange-50">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">Our Mission</h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto mb-12">
            To share the rich culinary heritage of West Africa through our authentic jollof rice, creating memorable
            dining experiences that bring people together.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="p-6 bg-white rounded-lg shadow-md">
              <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-8 w-8 text-orange-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-3">Authenticity</h3>
              <p className="text-muted-foreground">
                We stay true to traditional recipes and cooking methods, bringing the real taste of West Africa to New
                York.
              </p>
            </div>
            <div className="p-6 bg-white rounded-lg shadow-md">
              <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-8 w-8 text-orange-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-3">Quality</h3>
              <p className="text-muted-foreground">
                We use only the freshest ingredients and never compromise on the quality of our food.
              </p>
            </div>
            <div className="p-6 bg-white rounded-lg shadow-md">
              <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-8 w-8 text-orange-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                  />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-3">Community</h3>
              <p className="text-muted-foreground">
                We believe food brings people together, and we're proud to be part of the diverse NYC food scene.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Meet the Team */}
      <section className="py-16 px-4 md:px-6">
        <div className="container mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">Meet the Team</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="relative w-48 h-48 rounded-full overflow-hidden mx-auto mb-6">
                <Image src="/placeholder.svg?height=200&width=200" alt="Team Member" fill className="object-cover" />
              </div>
              <h3 className="text-xl font-bold mb-2">Kofi Mensah</h3>
              <p className="text-orange-600 mb-4">Founder & Head Chef</p>
              <p className="text-muted-foreground">
                Born in Ghana, Kofi brings authentic West African cooking techniques and family recipes to The Jollof
                Guys.
              </p>
            </div>
            <div className="text-center">
              <div className="relative w-48 h-48 rounded-full overflow-hidden mx-auto mb-6">
                <Image src="/placeholder.svg?height=200&width=200" alt="Team Member" fill className="object-cover" />
              </div>
              <h3 className="text-xl font-bold mb-2">Ade Ogunleye</h3>
              <p className="text-orange-600 mb-4">Co-Founder & Operations</p>
              <p className="text-muted-foreground">
                With a background in hospitality management, Ade ensures everything runs smoothly from kitchen to
                customer.
              </p>
            </div>
            <div className="text-center">
              <div className="relative w-48 h-48 rounded-full overflow-hidden mx-auto mb-6">
                <Image src="/placeholder.svg?height=200&width=200" alt="Team Member" fill className="object-cover" />
              </div>
              <h3 className="text-xl font-bold mb-2">Maya Johnson</h3>
              <p className="text-orange-600 mb-4">Co-Founder & Marketing</p>
              <p className="text-muted-foreground">
                A New York native with Nigerian roots, Maya handles the brand's growth and community engagement.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 px-4 md:px-6 bg-orange-600 text-white">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">Join Us on Our Journey</h2>
          <p className="text-xl mb-8 max-w-2xl mx-auto">
            Whether you're looking to try our jollof rice for the first time or book us for your next event, we'd love
            to serve you.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button
              asChild
              size="lg"
              variant="outline"
              className="border-white text-white hover:bg-white hover:text-orange-600"
            >
              <Link href="/menu">View Our Menu</Link>
            </Button>
            <Button asChild size="lg" className="bg-white text-orange-600 hover:bg-white/90">
              <Link href="/contact">Contact Us</Link>
            </Button>
          </div>
        </div>
      </section>
    </div>
  )
}
