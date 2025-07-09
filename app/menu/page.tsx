import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Star } from "lucide-react"
import Image from "next/image"

export default function Menu() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[400px] flex items-center justify-center text-white">
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{
            backgroundImage: `url('https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Headerimagejollof.png-H0vElsDz6upxDMzm7moF5AmgNoRxY3.jpeg')`,
          }}
        />
        <div className="absolute inset-0 bg-black/40" />
        <div className="relative z-10 text-center px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">Our Menu</h1>
          <p className="text-xl md:text-2xl">Authentic West African Flavors</p>
        </div>
      </section>

      {/* Menu Content */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-6xl">
          {/* Jollof Rice Section */}
          <div className="mb-16">
            <h2 className="text-3xl font-bold mb-8 text-center">Jollof Rice Varieties</h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
              <Card className="overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="h-48 relative rounded-t-lg overflow-hidden bg-gradient-to-br from-orange-100 to-orange-50">
                  <Image
                    src="/images/classic-jollof-rice-new.jpeg"
                    alt="Classic Chicken Jollof with fried chicken, plantains and coleslaw"
                    width={400}
                    height={300}
                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                    style={{
                      objectFit: "cover",
                      objectPosition: "center 30%",
                      filter: "brightness(1.05) contrast(1.1) saturate(1.1)",
                    }}
                    priority
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/10 to-transparent"></div>
                </div>
                <CardContent className="p-6 bg-white">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold text-gray-900">Classic Chicken Jollof</h3>
                    <Badge variant="secondary" className="bg-orange-100 text-orange-800 font-semibold">
                      $16.99
                    </Badge>
                  </div>
                  <p className="text-muted-foreground mb-4 leading-relaxed">
                    Traditional jollof rice with tender chicken pieces, cooked with authentic West African spices,
                    tomatoes, and aromatic herbs.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current drop-shadow-sm" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground font-medium">(4.9)</span>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <div className="h-48 relative rounded-t-lg overflow-hidden bg-gray-100">
                  <Image
                    src="/images/fried-rice.jpeg"
                    alt="Fried Rice with grilled fish and mixed vegetables"
                    width={400}
                    height={300}
                    className="w-full h-full object-cover"
                    style={{ objectFit: "cover" }}
                  />
                </div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Chicken Fried Rice</h3>
                    <Badge variant="secondary">$16.99</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    Delicious chicken fried rice with mixed vegetables, green beans, carrots, and tender chicken pieces,
                    seasoned with authentic West African spices.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground">(4.9)</span>
                  </div>
                </CardContent>
              </Card>

              <Card className="overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="h-48 relative rounded-t-lg overflow-hidden bg-gradient-to-br from-green-100 to-orange-50">
                  <Image
                    src="/images/vegetarian-jollof.jpeg"
                    alt="Vegetarian Jollof Rice with mixed vegetables, corn, peas and fried plantains"
                    width={400}
                    height={300}
                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                    style={{
                      objectFit: "cover",
                      objectPosition: "center center",
                      filter: "brightness(1.05) contrast(1.1) saturate(1.1)",
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/10 to-transparent"></div>
                </div>
                <CardContent className="p-6 bg-white">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold text-gray-900">Vegetarian Jollof</h3>
                    <Badge variant="secondary" className="bg-green-100 text-green-800 font-semibold">
                      $13.99
                    </Badge>
                  </div>
                  <p className="text-muted-foreground mb-4 leading-relaxed">
                    Plant-based jollof rice with mixed vegetables, maintaining all the traditional flavors without
                    compromising on taste.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current drop-shadow-sm" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground font-medium">(4.8)</span>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <div className="h-48 bg-gradient-to-br from-red-400 to-pink-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Beef Jollof</h3>
                    <Badge variant="secondary">$18.99</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    Rich and hearty jollof rice with tender beef chunks, slow-cooked to perfection with traditional
                    spices and seasonings.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground">(4.8)</span>
                  </div>
                </CardContent>
              </Card>

              <Card className="overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="h-48 relative rounded-t-lg overflow-hidden bg-gradient-to-br from-yellow-100 to-orange-50">
                  <Image
                    src="/images/jollof-fried-egg.jpeg"
                    alt="Jollof Rice topped with perfectly fried egg"
                    width={400}
                    height={300}
                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                    style={{
                      objectFit: "cover",
                      objectPosition: "center 40%",
                      filter: "brightness(1.05) contrast(1.1) saturate(1.1)",
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/10 to-transparent"></div>
                </div>
                <CardContent className="p-6 bg-white">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold text-gray-900">Jollof and Fried Egg</h3>
                    <Badge variant="secondary" className="bg-yellow-100 text-yellow-800 font-semibold">
                      $9.99
                    </Badge>
                  </div>
                  <p className="text-muted-foreground mb-4 leading-relaxed">
                    Classic comfort food combination featuring our signature jollof rice topped with a perfectly fried
                    egg, creating the ultimate satisfying meal.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current drop-shadow-sm" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground font-medium">(4.9)</span>
                  </div>
                </CardContent>
              </Card>

              <Card className="overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="h-48 relative rounded-t-lg overflow-hidden bg-gradient-to-br from-red-100 to-orange-50">
                  <Image
                    src="/images/spicy-jollof.jpeg"
                    alt="Spicy Jollof Rice with grilled chicken, plantains and moi moi"
                    width={400}
                    height={300}
                    className="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
                    style={{
                      objectFit: "cover",
                      objectPosition: "center 20%",
                      filter: "brightness(1.05) contrast(1.1) saturate(1.1)",
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/10 to-transparent"></div>
                </div>
                <CardContent className="p-6 bg-white">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Spicy Jollof</h3>
                    <Badge variant="secondary" className="bg-red-100 text-red-800 font-semibold">
                      $24.99
                    </Badge>
                  </div>
                  <p className="text-muted-foreground mb-4 leading-relaxed">
                    For those who love heat! Our classic chicken jollof with extra scotch bonnet peppers, spicy
                    seasonings, served with grilled chicken, plantains, and traditional moi moi.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current drop-shadow-sm" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground font-medium">(4.7)</span>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>

          {/* Sides & Extras */}
          <div className="mb-16">
            <h2 className="text-3xl font-bold mb-8 text-center">Sides & Extras</h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Plantains</h3>
                  <p className="text-sm text-muted-foreground mb-2">Sweet fried plantains</p>
                  <Badge variant="outline">$4</Badge>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Coleslaw</h3>
                  <p className="text-sm text-muted-foreground mb-2">Fresh cabbage salad</p>
                  <Badge variant="outline">$3</Badge>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Extra Protein</h3>
                  <p className="text-sm text-muted-foreground mb-2">Additional chicken/beef</p>
                  <Badge variant="outline">$5</Badge>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Pepper Sauce</h3>
                  <p className="text-sm text-muted-foreground mb-2">Homemade hot sauce</p>
                  <Badge variant="outline">$2</Badge>
                </CardContent>
              </Card>
            </div>
          </div>

          {/* Beverages */}
          <div>
            <h2 className="text-3xl font-bold mb-8 text-center">Beverages</h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Hibiscus Tea</h3>
                  <p className="text-sm text-muted-foreground mb-2">Traditional zobo drink</p>
                  <Badge variant="outline">$3</Badge>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Ginger Beer</h3>
                  <p className="text-sm text-muted-foreground mb-2">Spicy ginger drink</p>
                  <Badge variant="outline">$3</Badge>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Palm Wine</h3>
                  <p className="text-sm text-muted-foreground mb-2">Traditional fermented drink</p>
                  <Badge variant="outline">$4</Badge>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-4 text-center">
                  <h3 className="font-semibold mb-2">Soft Drinks</h3>
                  <p className="text-sm text-muted-foreground mb-2">Coke, Sprite, etc.</p>
                  <Badge variant="outline">$2</Badge>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
