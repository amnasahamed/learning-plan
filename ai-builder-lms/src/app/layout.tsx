import type { Metadata } from 'next'
import './globals.css'
import { AuthProvider } from '@/context/AuthContext'
import Script from 'next/script'

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
      <head>
        <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
      </head>
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
        <Script
          src="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js"
          strategy="afterInteractive"
          onLoad={() => {
            // @ts-ignore
            if (window.createChat) {
              // @ts-ignore
              window.createChat({
                webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat'
              });
            }
          }}
        />
      </body>
    </html>
  )
}
