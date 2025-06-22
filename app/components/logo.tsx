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
    sm: { width: 80, height: 32 },
    md: { width: 120, height: 48 },
    lg: { width: 160, height: 64 },
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
        src="/images/jollof-main-logo.png"
        alt="The Jollof Guys Logo"
        width={sizeMap[size].width}
        height={sizeMap[size].height}
        className="object-contain"
        onError={() => setImageError(true)}
        priority={true}
      />
    </div>
  )
}
