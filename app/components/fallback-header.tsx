import { Button } from "@/components/ui/button"
import Link from "next/link"

interface FallbackHeaderProps {
  title: string
  subtitle?: string
}

export function FallbackHeader({ title, subtitle }: FallbackHeaderProps) {
  return (
    <section className="relative w-full h-[80vh] bg-gradient-to-r from-orange-700 to-orange-500 overflow-hidden">
      <div className="absolute inset-0 flex flex-col items-center justify-center text-center px-4 md:px-6">
        <h1 className="text-4xl md:text-6xl font-bold text-white mb-4">{title}</h1>
        {subtitle && <p className="text-xl md:text-2xl text-white max-w-2xl mb-8">{subtitle}</p>}
        <div className="flex flex-col sm:flex-row gap-4">
          <Button asChild size="lg" className="bg-white text-orange-600 hover:bg-white/90">
            <Link href="/menu">View Our Menu</Link>
          </Button>
          <Button asChild size="lg" className="bg-white text-orange-600 hover:bg-white/90">
            <Link href="/contact">Book Catering</Link>
          </Button>
        </div>
      </div>
    </section>
  )
}
