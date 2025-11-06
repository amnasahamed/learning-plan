'use client'

import Link from 'next/link'
import { ArrowLeft, ExternalLink, Book, Code, Sparkles } from 'lucide-react'
import courseData from '@/data/courseData.json'

export default function ResourcesPage() {
  const categories = courseData.resources

  const iconMap: Record<string, any> = {
    'JavaScript Learning': Code,
    'n8n Specific': Sparkles,
    'AI & APIs': Book
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <Link
            href="/"
            className="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition mb-4"
          >
            <ArrowLeft className="w-5 h-5" />
            <span className="font-medium">Back to Dashboard</span>
          </Link>
          <h1 className="text-3xl font-bold text-gray-900">Learning Resources</h1>
          <p className="text-gray-600 mt-2">
            Curated resources to support your learning journey
          </p>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Prerequisites */}
        <section className="mb-12 bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Prerequisites</h2>

          {courseData.prerequisites.map((section, i) => (
            <div key={i} className="mb-8 last:mb-0">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">{section.category}</h3>
              <div className="space-y-3">
                {section.items.map((item, j) => (
                  <div
                    key={j}
                    className="flex items-start justify-between p-4 bg-gray-50 rounded-lg border border-gray-200"
                  >
                    <div className="flex-1">
                      <div className="font-semibold text-gray-900">{item.name}</div>
                      <div className="text-sm text-gray-600 mt-1">{item.description}</div>
                      <div className="text-xs text-gray-500 mt-2">
                        Estimated setup time: {item.estimatedTime}
                      </div>
                    </div>
                    <a
                      href={item.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="ml-4 text-blue-600 hover:text-blue-700"
                    >
                      <ExternalLink className="w-5 h-5" />
                    </a>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </section>

        {/* Learning Resources */}
        {categories.map((category, i) => {
          const Icon = iconMap[category.category] || Book

          return (
            <section key={i} className="mb-8 bg-white rounded-2xl shadow-lg border border-gray-100 p-8">
              <div className="flex items-center space-x-2 mb-6">
                <Icon className="w-6 h-6 text-blue-600" />
                <h2 className="text-2xl font-bold text-gray-900">{category.category}</h2>
              </div>

              <div className="space-y-4">
                {category.items.map((resource, j) => (
                  <a
                    key={j}
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-start justify-between p-5 bg-gray-50 hover:bg-gray-100 rounded-lg border border-gray-200 transition group"
                  >
                    <div className="flex-1">
                      <div className="flex items-center space-x-2">
                        <div className="font-bold text-gray-900 group-hover:text-blue-600 transition">
                          {resource.title}
                        </div>
                        <span className="text-xs px-2 py-1 bg-blue-100 text-blue-700 rounded-full capitalize">
                          {resource.type}
                        </span>
                      </div>
                      <p className="text-sm text-gray-600 mt-2">{resource.description}</p>
                    </div>
                    <ExternalLink className="w-5 h-5 text-gray-400 group-hover:text-blue-600 transition ml-4 flex-shrink-0" />
                  </a>
                ))}
              </div>
            </section>
          )
        })}

        {/* Quick Links */}
        <section className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl shadow-xl p-8 text-white">
          <h2 className="text-2xl font-bold mb-4">Need Help?</h2>
          <div className="grid md:grid-cols-3 gap-4">
            <a
              href="https://community.n8n.io"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-white/10 hover:bg-white/20 backdrop-blur rounded-lg p-4 transition"
            >
              <div className="font-semibold mb-2">n8n Community</div>
              <div className="text-sm text-blue-100">Ask questions and get help</div>
            </a>
            <a
              href="https://discord.gg/n8n"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-white/10 hover:bg-white/20 backdrop-blur rounded-lg p-4 transition"
            >
              <div className="font-semibold mb-2">n8n Discord</div>
              <div className="text-sm text-blue-100">Real-time chat support</div>
            </a>
            <a
              href="https://docs.n8n.io"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-white/10 hover:bg-white/20 backdrop-blur rounded-lg p-4 transition"
            >
              <div className="font-semibold mb-2">Official Docs</div>
              <div className="text-sm text-blue-100">Complete documentation</div>
            </a>
          </div>
        </section>
      </main>
    </div>
  )
}
