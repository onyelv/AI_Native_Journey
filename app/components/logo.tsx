"use client"

import { useState } from "react"

interface LogoProps {
  className?: string
  size?: "sm" | "md" | "lg"
}

export function Logo({ className = "", size = "md" }: LogoProps) {
  const [imageError, setImageError] = useState(false)

  const sizeClasses = {
    sm: "h-8 w-auto",
    md: "h-10 w-auto",
    lg: "h-16 w-auto",
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
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src="/images/jollof-logo-black.png"
        alt="The Jollof Guys Logo"
        className={`${sizeClasses[size]} object-contain`}
        onError={() => setImageError(true)}
        onLoad={() => console.log("Logo loaded successfully")}
      />
    </div>
  )
}
