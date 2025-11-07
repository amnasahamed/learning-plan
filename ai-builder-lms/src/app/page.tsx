'use client'

import Link from 'next/link'
import { useAuth } from '@/context/AuthContext'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { Rocket, Code, Brain, Zap, CheckCircle2, ArrowRight, Sparkles } from 'lucide-react'

export default function HomePage() {
  const { user, loading } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (!loading && user) {
      router.push('/dashboard')
    }
  }, [user, loading, router])

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
                <Rocket className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">AI Systems Builder</h1>
                <p className="text-xs text-gray-600">30-Day Learning Path</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Link
                href="/login"
                className="text-gray-700 hover:text-blue-600 font-medium transition"
              >
                Login
              </Link>
              <Link
                href="/register"
                className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition font-medium"
              >
                Get Started
              </Link>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center">
          <div className="inline-flex items-center space-x-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-semibold mb-6">
            <Sparkles className="w-4 h-4" />
            <span>Transform Your Career in 30 Days</span>
          </div>

          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            Become an
            <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent"> AI Systems Builder</span>
          </h1>

          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Master n8n automation, AI APIs, and intelligent system design. Build production-ready
            AI solutions in just 30 minutes per day.
          </p>

          <div className="flex items-center justify-center space-x-4">
            <Link
              href="/register"
              className="inline-flex items-center space-x-2 bg-blue-600 text-white px-8 py-4 rounded-lg hover:bg-blue-700 transition font-bold text-lg"
            >
              <span>Start Learning Free</span>
              <ArrowRight className="w-5 h-5" />
            </Link>
            <Link
              href="#features"
              className="inline-flex items-center space-x-2 bg-white text-gray-700 px-8 py-4 rounded-lg hover:bg-gray-50 transition font-bold text-lg border-2 border-gray-200"
            >
              <span>Learn More</span>
            </Link>
          </div>

          <div className="mt-12 flex items-center justify-center space-x-8 text-sm text-gray-600">
            <div className="flex items-center space-x-2">
              <CheckCircle2 className="w-5 h-5 text-green-500" />
              <span>30 Days of Content</span>
            </div>
            <div className="flex items-center space-x-2">
              <CheckCircle2 className="w-5 h-5 text-green-500" />
              <span>Hands-on Projects</span>
            </div>
            <div className="flex items-center space-x-2">
              <CheckCircle2 className="w-5 h-5 text-green-500" />
              <span>No Experience Needed</span>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">What You'll Learn</h2>
          <p className="text-xl text-gray-600">A complete curriculum from basics to advanced AI systems</p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
            <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4">
              <Code className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="text-xl font-bold text-gray-900 mb-3">JavaScript & n8n</h3>
            <p className="text-gray-600 mb-4">
              Master JavaScript fundamentals and n8n automation. Build workflows that connect APIs,
              process data, and automate tasks.
            </p>
            <ul className="space-y-2 text-sm text-gray-600">
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-blue-600 rounded-full"></div>
                <span>Variables, arrays, objects</span>
              </li>
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-blue-600 rounded-full"></div>
                <span>API integration patterns</span>
              </li>
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-blue-600 rounded-full"></div>
                <span>Error handling & debugging</span>
              </li>
            </ul>
          </div>

          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
            <div className="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center mb-4">
              <Brain className="w-6 h-6 text-purple-600" />
            </div>
            <h3 className="text-xl font-bold text-gray-900 mb-3">AI Integration</h3>
            <p className="text-gray-600 mb-4">
              Connect to OpenAI, Claude, and Gemini. Build intelligent agents with memory,
              context, and caching strategies.
            </p>
            <ul className="space-y-2 text-sm text-gray-600">
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-purple-600 rounded-full"></div>
                <span>AI API fundamentals</span>
              </li>
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-purple-600 rounded-full"></div>
                <span>Dynamic prompt engineering</span>
              </li>
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-purple-600 rounded-full"></div>
                <span>Context & memory management</span>
              </li>
            </ul>
          </div>

          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
            <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center mb-4">
              <Zap className="w-6 h-6 text-green-600" />
            </div>
            <h3 className="text-xl font-bold text-gray-900 mb-3">RAG Systems</h3>
            <p className="text-gray-600 mb-4">
              Design and deploy production RAG systems. Learn embeddings, vector search,
              and system architecture.
            </p>
            <ul className="space-y-2 text-sm text-gray-600">
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-green-600 rounded-full"></div>
                <span>Python + n8n integration</span>
              </li>
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-green-600 rounded-full"></div>
                <span>Vector databases & search</span>
              </li>
              <li className="flex items-center space-x-2">
                <div className="w-1.5 h-1.5 bg-green-600 rounded-full"></div>
                <span>Complete RAG deployment</span>
              </li>
            </ul>
          </div>
        </div>
      </section>

      {/* Course Structure */}
      <section className="bg-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">30-Day Learning Path</h2>
            <p className="text-xl text-gray-600">Structured curriculum with hands-on projects</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl p-8 border-2 border-blue-200">
              <div className="text-blue-700 font-bold text-sm mb-2">WEEK 1-2</div>
              <h3 className="text-2xl font-bold text-gray-900 mb-4">Foundations</h3>
              <p className="text-gray-700 mb-6">
                Master JavaScript and n8n automation. Build API workflows, handle errors, and manage data flow.
              </p>
              <div className="bg-white rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-700 mb-2">Projects:</div>
                <ul className="space-y-2 text-sm text-gray-600">
                  <li>• Smart Data Transformer</li>
                  <li>• Weather Alert Bot</li>
                </ul>
              </div>
            </div>

            <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-2xl p-8 border-2 border-purple-200">
              <div className="text-purple-700 font-bold text-sm mb-2">WEEK 3-4</div>
              <h3 className="text-2xl font-bold text-gray-900 mb-4">AI Systems</h3>
              <p className="text-gray-700 mb-6">
                Integrate AI APIs, build intelligent agents, and deploy complete RAG systems with vector search.
              </p>
              <div className="bg-white rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-700 mb-2">Projects:</div>
                <ul className="space-y-2 text-sm text-gray-600">
                  <li>• AI Assistant with Memory</li>
                  <li>• Production RAG System</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl shadow-2xl p-12 text-center text-white">
          <h2 className="text-4xl font-bold mb-4">Ready to Start Your Journey?</h2>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Join hundreds of students learning to build AI systems. Start today with just 30 minutes per day.
          </p>
          <Link
            href="/register"
            className="inline-flex items-center space-x-2 bg-white text-blue-600 px-8 py-4 rounded-lg hover:bg-gray-100 transition font-bold text-lg"
          >
            <Rocket className="w-6 h-6" />
            <span>Start Learning Now</span>
          </Link>
          <div className="mt-6 text-blue-100 text-sm">
            No credit card required • Free forever • Start immediately
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center text-gray-600">
            <p className="font-semibold mb-2">30-Day AI Systems Builder</p>
            <p className="text-sm">Transform from beginner to AI systems architect</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
