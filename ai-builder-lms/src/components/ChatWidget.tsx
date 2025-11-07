'use client'

import { useEffect } from 'react'

export default function ChatWidget() {
  useEffect(() => {
    // Load the n8n chat CSS
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css'
    document.head.appendChild(link)

    // Load the n8n chat script
    const script = document.createElement('script')
    script.src = 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js'
    script.async = true

    script.onload = () => {
      console.log('✅ n8n chat script loaded')

      // Wait a bit for the script to fully initialize
      setTimeout(() => {
        // @ts-ignore
        if (window.createChat && !window.chatInitialized) {
          try {
            console.log('🚀 Initializing n8n chat...')
            // @ts-ignore
            window.createChat({
              webhookUrl: 'https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat',
              initialMessages: ['Hi! I can help you with questions about the AI Systems Builder course.'],
              i18n: {
                en: {
                  title: 'AI Learning Assistant',
                  subtitle: 'Ask me anything',
                  footer: '',
                  getStarted: 'Start Chat',
                  inputPlaceholder: 'Type your message...',
                },
              },
            })
            // @ts-ignore
            window.chatInitialized = true
            console.log('✅ n8n chat initialized successfully!')
          } catch (error) {
            console.error('❌ Failed to initialize n8n chat:', error)
          }
        } else {
          console.warn('⚠️ window.createChat not available or already initialized')
        }
      }, 1000)
    }

    script.onerror = () => {
      console.error('❌ Failed to load n8n chat script')
    }

    document.body.appendChild(script)

    // Cleanup
    return () => {
      if (script.parentNode) {
        script.parentNode.removeChild(script)
      }
      if (link.parentNode) {
        link.parentNode.removeChild(link)
      }
    }
  }, [])

  return null
}
