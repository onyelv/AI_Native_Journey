"use client"

import Image from "next/image"
import { useState } from "react"

interface LogoProps {
  className?: string
  size?: "sm" | "md" | "lg"
}

export function Logo({ className = "", size = "md" }: LogoProps) {
  const [imageError, setImageError] = useState(false)

  const sizeMap = {
    sm: { width: 32, height: 32 },
    md: { width: 48, height: 48 },
    lg: { width: 64, height: 64 },
  }

  const textSizeClasses = {
    sm: "text-base",
    md: "text-xl",
    lg: "text-2xl",
  }

  if (imageError) {
    return <span className={`font-bold text-orange-600 ${textSizeClasses[size]} ${className}`}>The Jollof Guys</span>
  }

  return (
    <div className={`flex items-center ${className}`}>
      <Image
        src="/images/jollof-circle-logo.png"
        alt="The Jollof Guys Logo"
        width={sizeMap[size].width}
        height={sizeMap[size].height}
        className="rounded-full"
        onError={() => setImageError(true)}
        priority={true}
      />
    </div>
  )
}
