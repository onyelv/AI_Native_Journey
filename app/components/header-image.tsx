import type React from "react"
import Image from "next/image"

interface HeaderImageProps {
  title: string
  subtitle?: string
  height?: string
  children?: React.ReactNode
}

export function HeaderImage({ title, subtitle, height = "h-[50vh]", children }: HeaderImageProps) {
  return (
    <section className={`relative w-full ${height} overflow-hidden`}>
      {/* Image without any color overlay or blend mode */}
      <Image
        src="/images/headerimagejollof.png"
        alt="Delicious Jollof Rice"
        fill
        className="object-cover w-full h-full brightness-50"
        priority
      />
      <div className="absolute inset-0 flex flex-col items-center justify-center text-center px-4 md:px-6">
        <h1 className="text-4xl md:text-6xl font-bold text-white mb-4">{title}</h1>
        {subtitle && <p className="text-xl md:text-2xl text-white max-w-2xl mb-8">{subtitle}</p>}
        {children}
      </div>
    </section>
  )
}
