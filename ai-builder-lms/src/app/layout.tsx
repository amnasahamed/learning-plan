import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: '30-Day AI Systems Builder',
  description: 'Transform from automation beginner to AI systems architect in 30 days',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
