"use client"

import { useState } from "react"
import Image from "next/image"
import Link from "next/link"
import { MapPin, Phone, Mail, Calendar, Users, Clock } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import { useToast } from "@/hooks/use-toast"
import { HeaderImage } from "@/app/components/header-image"

export default function ContactPage() {
  const { toast } = useToast()
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    eventType: "private",
    eventDate: "",
    guestCount: "",
    message: "",
  })

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSelectChange = (name, value) => {
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(formData)
    toast({
      title: "Form submitted!",
      description: "We'll get back to you as soon as possible.",
    })
    setFormData({
      name: "",
      email: "",
      phone: "",
      eventType: "private",
      eventDate: "",
      guestCount: "",
      message: "",
    })
  }

  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section with corrected header image */}
      <HeaderImage title="Contact Us" subtitle="Book us for your next event or get in touch with any questions" />

      {/* Rest of the contact page content remains the same */}
      {/* Contact Information */}
      <section className="py-16 px-4 md:px-6">
        <div className="container mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
            <Card>
              <CardContent className="p-6 flex flex-col items-center text-center">
                <Phone className="h-10 w-10 text-orange-600 mb-4" />
                <h3 className="text-xl font-bold mb-2">Call Us</h3>
                <p className="text-muted-foreground">(646) 879-0914</p>
                <p className="text-muted-foreground">Mon-Fri: 9am-5pm</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6 flex flex-col items-center text-center">
                <Mail className="h-10 w-10 text-orange-600 mb-4" />
                <h3 className="text-xl font-bold mb-2">Email Us</h3>
                <p className="text-muted-foreground">onyelv@gmail.com</p>
                <p className="text-muted-foreground">onyelv@gmail.com</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6 flex flex-col items-center text-center">
                <MapPin className="h-10 w-10 text-orange-600 mb-4" />
                <h3 className="text-xl font-bold mb-2">Find Us</h3>
                <p className="text-muted-foreground">Check our locations at NYC street markets</p>
                <Link href="/#locations" className="text-orange-600 hover:underline">
                  View Locations
                </Link>
              </CardContent>
            </Card>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
            {/* Booking Form */}
            <div>
              <h2 className="text-3xl font-bold mb-6">Book Us for Your Event</h2>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-2">
                    <Label htmlFor="name">Full Name</Label>
                    <Input
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      placeholder="Your name"
                      required
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="email">Email</Label>
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      value={formData.email}
                      onChange={handleChange}
                      placeholder="Your email"
                      required
                    />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="phone">Phone Number</Label>
                  <Input
                    id="phone"
                    name="phone"
                    type="tel"
                    value={formData.phone}
                    onChange={handleChange}
                    placeholder="Your phone number"
                    required
                  />
                </div>
                <div className="space-y-2">
                  <Label>Event Type</Label>
                  <RadioGroup
                    defaultValue="private"
                    value={formData.eventType}
                    onValueChange={(value) => handleSelectChange("eventType", value)}
                    className="flex flex-col space-y-1"
                  >
                    <div className="flex items-center space-x-2">
                      <RadioGroupItem value="private" id="private" />
                      <Label htmlFor="private">Private Event</Label>
                    </div>
                    <div className="flex items-center space-x-2">
                      <RadioGroupItem value="corporate" id="corporate" />
                      <Label htmlFor="corporate">Corporate Event</Label>
                    </div>
                    <div className="flex items-center space-x-2">
                      <RadioGroupItem value="wedding" id="wedding" />
                      <Label htmlFor="wedding">Wedding</Label>
                    </div>
                    <div className="flex items-center space-x-2">
                      <RadioGroupItem value="other" id="other" />
                      <Label htmlFor="other">Other</Label>
                    </div>
                  </RadioGroup>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-2">
                    <Label htmlFor="eventDate">Event Date</Label>
                    <div className="relative">
                      <Calendar className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
                      <Input
                        id="eventDate"
                        name="eventDate"
                        type="date"
                        value={formData.eventDate}
                        onChange={handleChange}
                        className="pl-10"
                        required
                      />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="guestCount">Number of Guests</Label>
                    <div className="relative">
                      <Users className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
                      <Select
                        value={formData.guestCount}
                        onValueChange={(value) => handleSelectChange("guestCount", value)}
                      >
                        <SelectTrigger className="pl-10">
                          <SelectValue placeholder="Select guest count" />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="1-10">1-10 guests</SelectItem>
                          <SelectItem value="11-25">11-25 guests</SelectItem>
                          <SelectItem value="26-50">26-50 guests</SelectItem>
                          <SelectItem value="51-100">51-100 guests</SelectItem>
                          <SelectItem value="100+">100+ guests</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="message">Additional Information</Label>
                  <Textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    placeholder="Tell us more about your event, dietary requirements, or any questions you have."
                    className="min-h-[120px]"
                  />
                </div>
                <Button type="submit" className="w-full bg-orange-600 hover:bg-orange-700">
                  Submit Inquiry
                </Button>
              </form>
            </div>

            {/* FAQ */}
            <div>
              <h2 className="text-3xl font-bold mb-6">Frequently Asked Questions</h2>
              <div className="space-y-6">
                <div>
                  <h3 className="text-xl font-bold mb-2">How far in advance should I book?</h3>
                  <p className="text-muted-foreground">
                    We recommend booking at least 2-3 weeks in advance for small events and 4-6 weeks for larger events
                    to ensure availability.
                  </p>
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">Do you offer delivery?</h3>
                  <p className="text-muted-foreground">
                    Yes, we offer delivery within NYC for catering orders. Delivery fees vary based on location and
                    order size.
                  </p>
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">Can you accommodate dietary restrictions?</h3>
                  <p className="text-muted-foreground">
                    We offer vegetarian, vegan, and gluten-free options. Please let us know about any allergies or
                    dietary requirements when booking.
                  </p>
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">What's included in the catering package?</h3>
                  <p className="text-muted-foreground">
                    Our standard catering packages include food, serving utensils, plates, and napkins. We can also
                    provide staff for an additional fee.
                  </p>
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">Do you offer tastings?</h3>
                  <p className="text-muted-foreground">
                    Yes, we offer tastings for events with 50+ guests. There is a small fee that will be credited toward
                    your final booking.
                  </p>
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2">What is your cancellation policy?</h3>
                  <p className="text-muted-foreground">
                    Cancellations made 7+ days before the event receive a full refund. Cancellations within 3-6 days
                    receive a 50% refund. Cancellations with less than 48 hours notice are non-refundable.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* NYC Locations Map */}
      <section id="locations" className="py-16 px-4 md:px-6 bg-orange-50">
        <div className="container mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">Our NYC Locations</h2>
          <div className="relative w-full h-[400px] rounded-lg overflow-hidden shadow-xl">
            <Image
              src="/placeholder.svg?height=800&width=1600"
              alt="Map of NYC Locations"
              fill
              className="object-cover"
            />
            {/* This would be replaced with an actual map component in a real implementation */}
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
            <Card>
              <CardContent className="p-6">
                <div className="flex items-start space-x-4">
                  <MapPin className="h-6 w-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg font-bold mb-2">Uptown Night Market</h3>
                    <p className="text-muted-foreground mb-2">12th Avenue & 125th Street, Harlem, NY 10027</p>
                    <div className="flex items-center text-sm text-muted-foreground">
                      <Clock className="h-4 w-4 mr-2" />
                      <span>Thursdays, 5pm - 11pm</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6">
                <div className="flex items-start space-x-4">
                  <MapPin className="h-6 w-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg font-bold mb-2">Bronx Night Market</h3>
                    <p className="text-muted-foreground mb-2">Fordham Plaza, Bronx, NY 10458</p>
                    <div className="flex items-center text-sm text-muted-foreground">
                      <Clock className="h-4 w-4 mr-2" />
                      <span>Saturdays, 12pm - 7pm</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-6">
                <div className="flex items-start space-x-4">
                  <MapPin className="h-6 w-6 text-orange-600 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-lg font-bold mb-2">Queens Night Market</h3>
                    <p className="text-muted-foreground mb-2">Flushing Meadows Corona Park, Queens, NY 11368</p>
                    <div className="flex items-center text-sm text-muted-foreground">
                      <Clock className="h-4 w-4 mr-2" />
                      <span>Saturdays, 5pm - 12am</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Rest of the contact page content remains the same */}
    </div>
  )
}
