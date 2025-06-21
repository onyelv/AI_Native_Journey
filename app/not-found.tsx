import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Mountain } from "lucide-react"

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-orange-50 px-4 text-center">
      <Mountain className="h-16 w-16 text-orange-600 mb-6" />
      <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-4">404</h1>
      <h2 className="text-2xl md:text-3xl font-semibold text-gray-800 mb-6">Page Not Found</h2>
      <p className="text-lg text-gray-600 max-w-md mb-8">
        The page you're looking for doesn't exist or has been moved.
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <Button asChild size="lg" className="bg-orange-600 hover:bg-orange-700">
          <Link href="/">Return Home</Link>
        </Button>
        <Button asChild size="lg" variant="outline" className="border-orange-600 text-orange-600 hover:bg-orange-50">
          <Link href="/menu">View Our Menu</Link>
        </Button>
      </div>
    </div>
  )
}
