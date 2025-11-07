'use client'

import { useEffect } from 'react'
import Script from 'next/script'

export default function ChatWidget() {
  return (
    <Script
      src="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js"
      strategy="afterInteractive"
      onReady={() => {
        // @ts-ignore
        if (typeof window !== 'undefined' && window.createChat) {
          // @ts-ignore
          window.createChat({
            webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat'
          })
        }
      }}
    />
  )
}
