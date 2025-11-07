import type { Metadata } from 'next'
import './globals.css'
import { AuthProvider } from '@/context/AuthContext'
import ChatWidget from '@/components/ChatWidget'

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
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
        <ChatWidget />
      </body>
    </html>
  )
}
