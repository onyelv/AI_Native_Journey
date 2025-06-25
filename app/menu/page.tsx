import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Star } from "lucide-react"

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
              <Card>
                <div className="h-48 bg-gradient-to-br from-orange-400 to-red-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Classic Chicken Jollof</h3>
                    <Badge variant="secondary">$12</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    Traditional jollof rice with tender chicken pieces, cooked with authentic West African spices,
                    tomatoes, and aromatic herbs.
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

              <Card>
                <div className="h-48 bg-gradient-to-br from-red-400 to-pink-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Beef Jollof</h3>
                    <Badge variant="secondary">$14</Badge>
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

              <Card>
                <div className="h-48 bg-gradient-to-br from-blue-400 to-purple-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Seafood Jollof</h3>
                    <Badge variant="secondary">$15</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    Premium jollof rice with fresh shrimp, fish, and calamari, bringing the coastal flavors of West
                    Africa to your plate.
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

              <Card>
                <div className="h-48 bg-gradient-to-br from-green-400 to-blue-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Vegetarian Jollof</h3>
                    <Badge variant="secondary">$10</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    Plant-based jollof rice with mixed vegetables, maintaining all the traditional flavors without
                    compromising on taste.
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

              <Card>
                <div className="h-48 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Mixed Protein Jollof</h3>
                    <Badge variant="secondary">$16</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    The ultimate jollof experience with chicken, beef, and shrimp combined in one delicious,
                    protein-packed dish.
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

              <Card>
                <div className="h-48 bg-gradient-to-br from-purple-400 to-red-500 rounded-t-lg"></div>
                <CardContent className="p-6">
                  <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-semibold">Spicy Jollof</h3>
                    <Badge variant="destructive">Hot</Badge>
                    <Badge variant="secondary">$13</Badge>
                  </div>
                  <p className="text-muted-foreground mb-4">
                    For those who love heat! Our classic chicken jollof with extra scotch bonnet peppers and spicy
                    seasonings.
                  </p>
                  <div className="flex items-center">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current" />
                      ))}
                    </div>
                    <span className="ml-2 text-sm text-muted-foreground">(4.7)</span>
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
