import { Card, CardContent } from "@/components/ui/card"

export default function About() {
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
          <h1 className="text-4xl md:text-6xl font-bold mb-4">About The Jollof Guys</h1>
          <p className="text-xl md:text-2xl">Our Story & Heritage</p>
        </div>
      </section>

      {/* Main Content */}
      <section className="py-16 px-4">
        <div className="container mx-auto max-w-4xl">
          <div className="prose prose-lg mx-auto">
            <h2 className="text-3xl font-bold mb-6">Our Story</h2>
            <p className="text-lg text-muted-foreground mb-6">
              The Jollof Guys was born from a passion for sharing the authentic flavors of West Africa with New York
              City. Founded by immigrants who missed the taste of home, we set out to bring traditional jollof rice
              recipes to the diverse food scene of NYC.
            </p>

            <p className="text-lg text-muted-foreground mb-8">
              Our recipes have been passed down through generations, originating from the kitchens of Nigeria, Ghana,
              and Senegal. We believe that food is more than sustenance—it's a bridge between cultures, a way to share
              stories, and a means to bring people together.
            </p>

            <h2 className="text-3xl font-bold mb-6">Our Mission</h2>
            <p className="text-lg text-muted-foreground mb-8">
              To introduce New Yorkers to the rich, complex flavors of authentic West African jollof rice while
              maintaining the traditional cooking methods and spice combinations that make this dish so special. We're
              committed to using only the finest ingredients and time-honored techniques.
            </p>

            <div className="grid md:grid-cols-2 gap-8 my-12">
              <Card>
                <CardContent className="p-6">
                  <h3 className="text-xl font-semibold mb-4">Authentic Recipes</h3>
                  <p className="text-muted-foreground">
                    Every dish is prepared using traditional recipes and cooking methods passed down through generations
                    of West African families.
                  </p>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-6">
                  <h3 className="text-xl font-semibold mb-4">Quality Ingredients</h3>
                  <p className="text-muted-foreground">
                    We source the finest spices, rice, and proteins to ensure every bite delivers the authentic taste
                    and aroma of traditional jollof rice.
                  </p>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-6">
                  <h3 className="text-xl font-semibold mb-4">Cultural Bridge</h3>
                  <p className="text-muted-foreground">
                    Food is our way of sharing West African culture and creating connections between communities in New
                    York City.
                  </p>
                </CardContent>
              </Card>

              <Card>
                <CardContent className="p-6">
                  <h3 className="text-xl font-semibold mb-4">Community Focus</h3>
                  <p className="text-muted-foreground">
                    We're proud to be part of NYC's vibrant street food scene and contribute to the city's incredible
                    culinary diversity.
                  </p>
                </CardContent>
              </Card>
            </div>

            <h2 className="text-3xl font-bold mb-6">Meet the Team</h2>
            <p className="text-lg text-muted-foreground mb-8">
              Our team consists of passionate cooks and food enthusiasts who share a love for West African cuisine. Each
              member brings their own family recipes and cooking traditions, creating a rich tapestry of flavors and
              techniques that make our jollof rice truly special.
            </p>
          </div>
        </div>
      </section>
    </div>
  )
}
