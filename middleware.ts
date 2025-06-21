import { NextResponse } from "next/server"
import type { NextRequest } from "next/server"

export function middleware(request: NextRequest) {
  // Log all requests for debugging
  console.log(`[${new Date().toISOString()}] ${request.method} ${request.nextUrl.pathname}`)

  // Check if the request is for a static asset
  if (request.nextUrl.pathname.startsWith("/images/")) {
    // Add custom headers for images
    const response = NextResponse.next()
    response.headers.set("Cache-Control", "public, max-age=86400, immutable")
    return response
  }

  // Handle potential 404 errors for non-existent pages
  const response = NextResponse.next()

  // Add security headers
  response.headers.set("X-Content-Type-Options", "nosniff")
  response.headers.set("X-Frame-Options", "DENY")
  response.headers.set("X-XSS-Protection", "1; mode=block")

  return response
}

export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    "/((?!_next/static|_next/image|favicon.ico).*)",
  ],
}
