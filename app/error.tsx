"use client"

import { useEffect } from "react"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { AlertTriangle } from "lucide-react"

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-orange-50 px-4 text-center">
      <AlertTriangle className="h-16 w-16 text-orange-600 mb-6" />
      <h2 className="text-2xl md:text-3xl font-semibold text-gray-800 mb-6">Something went wrong!</h2>
      <p className="text-lg text-gray-600 max-w-md mb-8">
        We apologize for the inconvenience. Please try again or return to the homepage.
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <Button onClick={reset} size="lg" className="bg-orange-600 hover:bg-orange-700">
          Try Again
        </Button>
        <Button asChild size="lg" variant="outline" className="border-orange-600 text-orange-600 hover:bg-orange-50">
          <Link href="/">Return Home</Link>
        </Button>
      </div>
    </div>
  )
}
