import Image from "next/image"
import Link from "next/link"

import { Button } from "@/components/ui/button"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Card, CardContent } from "@/components/ui/card"
import { HeaderImage } from "@/app/components/header-image"

export default function MenuPage() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section with corrected header image */}
      <HeaderImage title="Our Menu" subtitle="Authentic West African flavors made with love" />

      {/* Rest of the menu page content remains the same */}
      {/* Menu Tabs */}
      <section className="py-16 px-4 md:px-6">
        <div className="container mx-auto">
          <Tabs defaultValue="main" className="w-full">
            <TabsList className="grid w-full grid-cols-4 mb-12">
              <TabsTrigger value="main">Main Dishes</TabsTrigger>
              <TabsTrigger value="sides">Side Dishes</TabsTrigger>
              <TabsTrigger value="drinks">Drinks</TabsTrigger>
              <TabsTrigger value="desserts">Desserts</TabsTrigger>
            </TabsList>

            {/* Main Dishes */}
            <TabsContent value="main">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Classic Jollof Rice"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Classic Jollof Rice</h3>
                      <p className="font-semibold text-orange-600">$12.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Our signature dish made with long-grain rice, tomatoes, peppers, and our secret spice blend.
                    </p>
                    <p className="text-sm text-muted-foreground">Vegetarian option available</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Jollof Rice with Grilled Chicken"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Jollof Rice with Grilled Chicken</h3>
                      <p className="font-semibold text-orange-600">$16.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Our classic jollof rice served with perfectly seasoned grilled chicken.
                    </p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Jollof Rice with Beef"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Jollof Rice with Beef</h3>
                      <p className="font-semibold text-orange-600">$17.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Our classic jollof rice served with tender, slow-cooked beef.
                    </p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Seafood Jollof Rice"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Seafood Jollof Rice</h3>
                      <p className="font-semibold text-orange-600">$19.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      A luxurious version of our jollof rice with shrimp, calamari, and fish.
                    </p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Vegetable Jollof Rice"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Vegetable Jollof Rice</h3>
                      <p className="font-semibold text-orange-600">$14.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Our classic jollof rice loaded with seasonal vegetables.
                    </p>
                    <p className="text-sm text-muted-foreground">Vegan & gluten-free</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Party Size Jollof Rice"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Party Size Jollof Rice</h3>
                      <p className="font-semibold text-orange-600">$39.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      A large portion of our classic jollof rice, perfect for sharing with 4-6 people.
                    </p>
                    <p className="text-sm text-muted-foreground">Add protein for additional cost</p>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>

            {/* Side Dishes */}
            <TabsContent value="sides">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Fried Plantains"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Fried Plantains</h3>
                      <p className="font-semibold text-orange-600">$5.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">Sweet plantains, fried to golden perfection.</p>
                    <p className="text-sm text-muted-foreground">Vegetarian & gluten-free</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Moin Moin" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Moin Moin</h3>
                      <p className="font-semibold text-orange-600">$6.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">Steamed bean pudding with peppers, onions, and spices.</p>
                    <p className="text-sm text-muted-foreground">Vegetarian & gluten-free</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Coleslaw" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">African Coleslaw</h3>
                      <p className="font-semibold text-orange-600">$4.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Fresh cabbage, carrots, and our special dressing with a West African twist.
                    </p>
                    <p className="text-sm text-muted-foreground">Vegetarian & gluten-free</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Suya" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Suya (Beef Skewers)</h3>
                      <p className="font-semibold text-orange-600">$8.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Grilled beef skewers seasoned with our special suya spice blend.
                    </p>
                    <p className="text-sm text-muted-foreground">Gluten-free</p>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>

            {/* Drinks */}
            <TabsContent value="drinks">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Zobo" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Zobo</h3>
                      <p className="font-semibold text-orange-600">$3.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Traditional Nigerian hibiscus drink, sweet and refreshing.
                    </p>
                    <p className="text-sm text-muted-foreground">Vegan & gluten-free</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Chapman" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Chapman</h3>
                      <p className="font-semibold text-orange-600">$4.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      A popular West African cocktail made with Fanta, Sprite, and a splash of grenadine.
                    </p>
                    <p className="text-sm text-muted-foreground">Non-alcoholic</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Ginger Beer"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Homemade Ginger Beer</h3>
                      <p className="font-semibold text-orange-600">$3.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">Spicy and refreshing homemade ginger beer.</p>
                    <p className="text-sm text-muted-foreground">Vegan & gluten-free</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image
                      src="/placeholder.svg?height=300&width=300"
                      alt="Soft Drinks"
                      fill
                      className="object-cover"
                    />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Soft Drinks</h3>
                      <p className="font-semibold text-orange-600">$2.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Assorted soft drinks including Coke, Diet Coke, Sprite, and Fanta.
                    </p>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>

            {/* Desserts */}
            <TabsContent value="desserts">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Puff Puff" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Puff Puff</h3>
                      <p className="font-semibold text-orange-600">$5.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">
                      Deep-fried sweet dough balls, served with a dusting of powdered sugar.
                    </p>
                    <p className="text-sm text-muted-foreground">Vegetarian</p>
                  </CardContent>
                </Card>

                <Card className="flex overflow-hidden">
                  <div className="relative w-1/3">
                    <Image src="/placeholder.svg?height=300&width=300" alt="Chin Chin" fill className="object-cover" />
                  </div>
                  <CardContent className="w-2/3 p-6">
                    <div className="flex justify-between items-start mb-2">
                      <h3 className="text-xl font-bold">Chin Chin</h3>
                      <p className="font-semibold text-orange-600">$4.99</p>
                    </div>
                    <p className="text-muted-foreground mb-4">Crunchy, sweet fried pastry snack.</p>
                    <p className="text-sm text-muted-foreground">Vegetarian</p>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>
          </Tabs>
        </div>
      </section>

      {/* Rest of the menu page content remains the same */}
      {/* Catering Menu */}
      <section className="py-16 px-4 md:px-6 bg-orange-50">
        <div className="container mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-6">Catering Menu</h2>
          <p className="text-xl text-center text-muted-foreground max-w-3xl mx-auto mb-12">
            We offer catering services for events of all sizes. Contact us for custom menus and pricing.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <Card className="p-6">
              <h3 className="text-2xl font-bold mb-4">Small Party Package</h3>
              <p className="text-lg mb-2">Serves 10-15 people</p>
              <ul className="list-disc list-inside space-y-2 mb-6 text-muted-foreground">
                <li>2 large trays of Jollof Rice (choice of protein)</li>
                <li>1 tray of Fried Plantains</li>
                <li>1 tray of African Coleslaw</li>
                <li>Assorted drinks (20 cans)</li>
              </ul>
              <p className="text-xl font-bold text-orange-600 mb-4">Starting at $249.99</p>
              <Button asChild className="w-full bg-orange-600 hover:bg-orange-700">
                <Link href="/contact">Inquire Now</Link>
              </Button>
            </Card>

            <Card className="p-6">
              <h3 className="text-2xl font-bold mb-4">Large Party Package</h3>
              <p className="text-lg mb-2">Serves 25-30 people</p>
              <ul className="list-disc list-inside space-y-2 mb-6 text-muted-foreground">
                <li>4 large trays of Jollof Rice (choice of protein)</li>
                <li>2 trays of Fried Plantains</li>
                <li>2 trays of African Coleslaw</li>
                <li>1 tray of Moin Moin</li>
                <li>Assorted drinks (40 cans)</li>
                <li>Dessert platter (Puff Puff & Chin Chin)</li>
              </ul>
              <p className="text-xl font-bold text-orange-600 mb-4">Starting at $499.99</p>
              <Button asChild className="w-full bg-orange-600 hover:bg-orange-700">
                <Link href="/contact">Inquire Now</Link>
              </Button>
            </Card>
          </div>
          <div className="text-center mt-12">
            <p className="text-muted-foreground mb-6">
              Custom packages available for corporate events, weddings, and special occasions.
            </p>
            <Button asChild size="lg" className="bg-orange-600 hover:bg-orange-700">
              <Link href="/contact">Contact Us for Custom Quotes</Link>
            </Button>
          </div>
        </div>
      </section>
    </div>
  )
}
