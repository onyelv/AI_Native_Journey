import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Star, MapPin, Clock } from "lucide-react"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[400px] sm:h-[500px] md:h-[600px] flex items-center justify-center text-white">
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{
            backgroundImage: `url('https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Headerimagejollof.png-H0vElsDz6upxDMzm7moF5AmgNoRxY3.jpeg')`,
          }}
        />
        <div className="absolute inset-0 bg-black/40" />
        <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
          <h1 className="text-2xl sm:text-4xl md:text-5xl lg:text-6xl font-bold mb-4">
            Authentic West African Jollof Rice
          </h1>
          <p className="text-base sm:text-lg md:text-xl lg:text-2xl mb-6 sm:mb-8">
            Experience the rich, aromatic flavors of traditional jollof rice in the heart of NYC
          </p>
          <div className="flex justify-center">
            <Button size="lg" className="bg-orange-600 hover:bg-orange-700 w-full sm:w-auto">
              <Link href="/menu">View Our Menu</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-12 sm:py-16 px-4">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-8 sm:mb-12">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">About The Jollof Guys</h2>
            <p className="text-base sm:text-lg text-muted-foreground max-w-3xl mx-auto">
              We bring the authentic taste of West African jollof rice to New York City's vibrant street food scene. Our
              recipes have been passed down through generations, ensuring every grain is perfectly seasoned with
              traditional spices and cooked to perfection.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
            <Card>
              <CardContent className="p-4 sm:p-6 text-center">
                <div className="w-12 h-12 sm:w-16 sm:h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-xl sm:text-2xl">🍚</span>
                </div>
                <h3 className="text-lg sm:text-xl font-semibold mb-2">Authentic Recipes</h3>
                <p className="text-sm sm:text-base text-muted-foreground">
                  Traditional West African recipes passed down through generations
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 sm:p-6 text-center">
                <div className="w-12 h-12 sm:w-16 sm:h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-xl sm:text-2xl">🌶️</span>
                </div>
                <h3 className="text-lg sm:text-xl font-semibold mb-2">Fresh Ingredients</h3>
                <p className="text-sm sm:text-base text-muted-foreground">
                  Only the finest spices and freshest ingredients in every dish
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 sm:p-6 text-center">
                <div className="w-12 h-12 sm:w-16 sm:h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-xl sm:text-2xl">❤️</span>
                </div>
                <h3 className="text-lg sm:text-xl font-semibold mb-2">Made with Love</h3>
                <p className="text-sm sm:text-base text-muted-foreground">
                  Every dish is prepared with care and passion for authentic flavors
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Menu Preview */}
      <section className="py-12 sm:py-16 bg-orange-50">
        <div className="container mx-auto max-w-6xl px-4">
          <div className="text-center mb-8 sm:mb-12">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">Our Signature Dishes</h2>
            <p className="text-base sm:text-lg text-muted-foreground">Taste the authentic flavors of West Africa</p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
            <Card>
              <div className="h-40 sm:h-48 bg-gradient-to-br from-orange-400 to-red-500 rounded-t-lg"></div>
              <CardContent className="p-4 sm:p-6">
                <div className="flex justify-between items-start mb-2">
                  <h3 className="text-lg sm:text-xl font-semibold">Classic Jollof Rice</h3>
                  <Badge variant="secondary">$12</Badge>
                </div>
                <p className="text-sm sm:text-base text-muted-foreground mb-4">
                  Traditional jollof rice with tender chicken, perfectly seasoned with authentic West African spices
                </p>
                <div className="flex items-center">
                  <div className="flex text-yellow-400">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="w-3 h-3 sm:w-4 sm:h-4 fill-current" />
                    ))}
                  </div>
                  <span className="ml-2 text-xs sm:text-sm text-muted-foreground">(4.9)</span>
                </div>
              </CardContent>
            </Card>

            <Card>
              <div className="h-40 sm:h-48 bg-gradient-to-br from-green-400 to-blue-500 rounded-t-lg"></div>
              <CardContent className="p-4 sm:p-6">
                <div className="flex justify-between items-start mb-2">
                  <h3 className="text-lg sm:text-xl font-semibold">Vegetarian Jollof</h3>
                  <Badge variant="secondary">$10</Badge>
                </div>
                <p className="text-sm sm:text-base text-muted-foreground mb-4">
                  Plant-based jollof rice with mixed vegetables, maintaining all the traditional flavors
                </p>
                <div className="flex items-center">
                  <div className="flex text-yellow-400">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="w-3 h-3 sm:w-4 sm:h-4 fill-current" />
                    ))}
                  </div>
                  <span className="ml-2 text-xs sm:text-sm text-muted-foreground">(4.8)</span>
                </div>
              </CardContent>
            </Card>

            <Card className="sm:col-span-2 lg:col-span-1">
              <div className="h-40 sm:h-48 bg-gradient-to-br from-purple-400 to-pink-500 rounded-t-lg"></div>
              <CardContent className="p-4 sm:p-6">
                <div className="flex justify-between items-start mb-2">
                  <h3 className="text-lg sm:text-xl font-semibold">Seafood Jollof</h3>
                  <Badge variant="secondary">$15</Badge>
                </div>
                <p className="text-sm sm:text-base text-muted-foreground mb-4">
                  Premium jollof rice with fresh shrimp and fish, a coastal West African favorite
                </p>
                <div className="flex items-center">
                  <div className="flex text-yellow-400">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="w-3 h-3 sm:w-4 sm:h-4 fill-current" />
                    ))}
                  </div>
                  <span className="ml-2 text-xs sm:text-sm text-muted-foreground">(4.9)</span>
                </div>
              </CardContent>
            </Card>
          </div>

          <div className="text-center mt-8 sm:mt-12">
            <Button size="lg" className="bg-orange-600 hover:bg-orange-700 w-full sm:w-auto">
              <Link href="/menu">View Full Menu</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Locations */}
      <section className="py-12 sm:py-16">
        <div className="container mx-auto max-w-6xl px-4">
          <div className="text-center mb-8 sm:mb-12">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">Find Us at NYC Markets</h2>
            <p className="text-base sm:text-lg text-muted-foreground">Visit us at these popular NYC locations</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
            <Card>
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-start gap-3 sm:gap-4">
                  <MapPin className="w-5 h-5 sm:w-6 sm:h-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg sm:text-xl font-semibold mb-2">Queens Night Market</h3>
                    <p className="text-sm sm:text-base text-muted-foreground mb-2">47-01 111th St, Corona, NY 11368</p>
                    <div className="flex items-center gap-4 text-xs sm:text-sm text-muted-foreground">
                      <div className="flex items-center gap-1">
                        <Clock className="w-3 h-3 sm:w-4 sm:h-4" />
                        <span>Sat 6PM-12AM</span>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-start gap-3 sm:gap-4">
                  <MapPin className="w-5 h-5 sm:w-6 sm:h-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg sm:text-xl font-semibold mb-2">Uptown Night Market</h3>
                    <p className="text-sm sm:text-base text-muted-foreground mb-2">
                      West 181st St & Broadway, New York, NY 10033
                    </p>
                    <div className="flex items-center gap-4 text-xs sm:text-sm text-muted-foreground">
                      <div className="flex items-center gap-1">
                        <Clock className="w-3 h-3 sm:w-4 sm:h-4" />
                        <span>Thu 6PM-11PM</span>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-start gap-3 sm:gap-4">
                  <MapPin className="w-5 h-5 sm:w-6 sm:h-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg sm:text-xl font-semibold mb-2">Bronx Night Market</h3>
                    <p className="text-sm sm:text-base text-muted-foreground mb-2">
                      East Fordham Rd & Grand Concourse, Bronx, NY 10458
                    </p>
                    <div className="flex items-center gap-4 text-xs sm:text-sm text-muted-foreground">
                      <div className="flex items-center gap-1">
                        <Clock className="w-3 h-3 sm:w-4 sm:h-4" />
                        <span>Sat 6PM-11PM</span>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 sm:p-6">
                <div className="flex items-start gap-3 sm:gap-4">
                  <MapPin className="w-5 h-5 sm:w-6 sm:h-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg sm:text-xl font-semibold mb-2">Grand Bazaar NYC</h3>
                    <p className="text-sm sm:text-base text-muted-foreground mb-2">100 W 77th St, New York, NY 10024</p>
                    <div className="flex items-center gap-4 text-xs sm:text-sm text-muted-foreground">
                      <div className="flex items-center gap-1">
                        <Clock className="w-3 h-3 sm:w-4 sm:h-4" />
                        <span>Sun 10AM-5:30PM</span>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-12 sm:py-16 bg-orange-50">
        <div className="container mx-auto max-w-6xl px-4">
          <div className="text-center mb-8 sm:mb-12">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">What Our Customers Say</h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
            <Card>
              <CardContent className="p-4 sm:p-6">
                <div className="flex text-yellow-400 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 sm:w-5 sm:h-5 fill-current" />
                  ))}
                </div>
                <p className="text-sm sm:text-base text-muted-foreground mb-4">
                  "The most authentic jollof rice I've had outside of Lagos! The flavors are incredible and remind me of
                  home."
                </p>
                <div className="font-semibold text-sm sm:text-base">- Adaora K.</div>
              </CardContent>
            </Card>

            <Card>
              <CardContent className="p-4 sm:p-6">
                <div className="flex text-yellow-400 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 sm:w-5 sm:h-5 fill-current" />
                  ))}
                </div>
                <p className="text-sm sm:text-base text-muted-foreground mb-4">
                  "Amazing food and great service! The Jollof Guys have become my go-to for authentic West African
                  cuisine."
                </p>
                <div className="font-semibold text-sm sm:text-base">- Marcus T.</div>
              </CardContent>
            </Card>

            <Card className="md:col-span-2 lg:col-span-1 md:mx-auto md:max-w-md lg:max-w-none">
              <CardContent className="p-4 sm:p-6">
                <div className="flex text-yellow-400 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 sm:w-5 sm:h-5 fill-current" />
                  ))}
                </div>
                <p className="text-sm sm:text-base text-muted-foreground mb-4">
                  "Perfect for our office catering event. Everyone loved the food and kept asking where we ordered
                  from!"
                </p>
                <div className="font-semibold text-sm sm:text-base">- Sarah M.</div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-12 sm:py-16 bg-orange-600 text-white">
        <div className="container mx-auto max-w-4xl px-4 text-center">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">Ready to Experience Authentic Jollof?</h2>
          <p className="text-base sm:text-lg md:text-xl mb-6 sm:mb-8">
            Book us for your next event or visit us at one of our market locations
          </p>
          <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center">
            <Button size="lg" className="bg-white text-orange-600 hover:bg-gray-100 w-full sm:w-auto">
              <Link href="/contact">Book Catering</Link>
            </Button>
            <Button size="lg" className="bg-white text-orange-600 hover:bg-gray-100 w-full sm:w-auto">
              <Link href="/contact">Contact Us</Link>
            </Button>
          </div>
        </div>
      </section>
    </div>
  )
}
