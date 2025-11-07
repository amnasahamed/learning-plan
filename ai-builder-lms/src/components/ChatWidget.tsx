'use client'

import { useEffect, useState } from 'react'
import Script from 'next/script'

export default function ChatWidget() {
  const [scriptLoaded, setScriptLoaded] = useState(false)

  useEffect(() => {
    // Only initialize if script is loaded and chat hasn't been created yet
    if (scriptLoaded && typeof window !== 'undefined') {
      // @ts-ignore
      if (window.createChat && !window.chatInitialized) {
        try {
          // @ts-ignore
          window.createChat({
            webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat',
            initialMessages: ['Hi! I can help you with questions about the AI Systems Builder course.'],
            i18n: {
              en: {
                title: 'AI Learning Assistant',
                subtitle: 'Ask me anything about the course',
                footer: '',
                getStarted: 'Start Chat',
                inputPlaceholder: 'Type your message...',
              },
            },
          })
          // @ts-ignore
          window.chatInitialized = true
          console.log('n8n chat widget initialized successfully')
        } catch (error) {
          console.error('Failed to initialize n8n chat widget:', error)
        }
      }
    }
  }, [scriptLoaded])

  return (
    <Script
      id="n8n-chat-script"
      src="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js"
      strategy="afterInteractive"
      onLoad={() => {
        console.log('n8n chat script loaded')
        setScriptLoaded(true)
      }}
      onError={(e) => {
        console.error('Failed to load n8n chat script:', e)
      }}
    />
  )
}
