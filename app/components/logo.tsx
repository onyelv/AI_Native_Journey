"use client"

import { useState } from "react"

interface LogoProps {
  className?: string
  size?: "sm" | "md" | "lg"
}

export function Logo({ className = "", size = "md" }: LogoProps) {
  const [imageError, setImageError] = useState(false)
  const [imageLoaded, setImageLoaded] = useState(false)

  const sizeClasses = {
    sm: "h-8 w-8",
    md: "h-12 w-12",
    lg: "h-16 w-16",
  }

  const textSizeClasses = {
    sm: "text-base",
    md: "text-xl",
    lg: "text-2xl",
  }

  // Show text fallback if image fails to load
  if (imageError) {
    return <span className={`font-bold text-orange-600 ${textSizeClasses[size]} ${className}`}>The Jollof Guys</span>
  }

  return (
    <div className={`flex items-center ${className}`}>
      {/* Show loading state */}
      {!imageLoaded && !imageError && (
        <div className={`${sizeClasses[size]} bg-orange-100 rounded-full flex items-center justify-center`}>
          <span className="text-orange-600 text-xs font-bold">TJG</span>
        </div>
      )}

      {/* Main logo image */}
      <img
        src="/images/jollof-logo-circle.png"
        alt="The Jollof Guys Logo"
        className={`${sizeClasses[size]} object-contain rounded-full ${imageLoaded ? "block" : "hidden"}`}
        onLoad={() => {
          setImageLoaded(true)
          console.log("Logo loaded successfully")
        }}
        onError={() => {
          setImageError(true)
          console.error("Logo failed to load")
        }}
      />
    </div>
  )
}
