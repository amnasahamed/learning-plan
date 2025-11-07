'use client'

import { useEffect, useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import Link from 'next/link'
import { useAuth } from '@/context/AuthContext'
import { ArrowLeft, CheckCircle2, Target, Code, Rocket, Book, User, LogOut, Linkedin } from 'lucide-react'
import courseData from '@/data/courseData.json'

export default function ProjectPage() {
  const params = useParams()
  const router = useRouter()
  const { user, loading: authLoading, logout } = useAuth()
  const [project, setProject] = useState<any>(null)
  const [week, setWeek] = useState<any>(null)

  useEffect(() => {
    if (!authLoading && !user) {
      router.push('/login')
      return
    }

    const weekNumber = parseInt(params.id as string)
    const weekData = courseData.weeks.find(w => w.weekNumber === weekNumber)

    if (weekData) {
      setWeek(weekData)
      setProject(weekData.project)
    }
  }, [user, authLoading, router, params.id])

  if (authLoading || !user) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
        </div>
      </div>
    )
  }

  if (!project || !week) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">Project Not Found</h1>
          <Link href="/dashboard" className="text-blue-600 hover:text-blue-700">
            ← Back to Dashboard
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Link
                href="/dashboard"
                className="inline-flex items-center space-x-2 text-gray-600 hover:text-gray-900 transition"
              >
                <ArrowLeft className="w-5 h-5" />
                <span>Dashboard</span>
              </Link>
              <div className="h-6 w-px bg-gray-300"></div>
              <h1 className="text-lg font-semibold text-gray-900">Week {week.weekNumber} Project</h1>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2 text-sm text-gray-700">
                <User className="w-4 h-4" />
                <span>{user?.name}</span>
              </div>
              <button
                onClick={logout}
                className="inline-flex items-center space-x-1 text-sm text-gray-600 hover:text-red-600 transition"
              >
                <LogOut className="w-4 h-4" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Project Header */}
        <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl shadow-xl p-8 text-white mb-8">
          <div className="flex items-center space-x-3 mb-4">
            <div className="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center">
              <Rocket className="w-6 h-6" />
            </div>
            <div>
              <p className="text-blue-100 text-sm font-medium">Week {week.weekNumber} Project</p>
              <h1 className="text-3xl font-bold">{project.title}</h1>
            </div>
          </div>
          <p className="text-xl text-blue-50">{project.description}</p>
        </div>

        {/* Week Context */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center space-x-2">
            <Book className="w-5 h-5 text-blue-600" />
            <span>Week {week.weekNumber}: {week.title}</span>
          </h2>
          <p className="text-gray-700 mb-4">{week.goal}</p>
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <p className="text-sm text-blue-800">
              <strong>💡 Tip:</strong> Complete Days {(week.weekNumber - 1) * 7 + 1}-{week.weekNumber * 7} before starting this project to build the necessary skills.
            </p>
          </div>
        </div>

        {/* Requirements */}
        {project.requirements && project.requirements.length > 0 && (
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-8">
            <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center space-x-2">
              <CheckCircle2 className="w-5 h-5 text-green-600" />
              <span>Requirements</span>
            </h2>
            <ul className="space-y-3">
              {project.requirements.map((req: string, index: number) => (
                <li key={index} className="flex items-start space-x-3">
                  <div className="w-6 h-6 rounded-full bg-green-100 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span className="text-sm font-semibold text-green-700">{index + 1}</span>
                  </div>
                  <span className="text-gray-700">{req}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Learning Objectives */}
        {project.learningObjectives && project.learningObjectives.length > 0 && (
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-8">
            <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center space-x-2">
              <Target className="w-5 h-5 text-purple-600" />
              <span>What You'll Learn</span>
            </h2>
            <ul className="space-y-2">
              {project.learningObjectives.map((objective: string, index: number) => (
                <li key={index} className="flex items-start space-x-2">
                  <span className="text-purple-600">→</span>
                  <span className="text-gray-700">{objective}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Implementation Guide */}
        {project.implementation && (
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-8">
            <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center space-x-2">
              <Code className="w-5 h-5 text-orange-600" />
              <span>Implementation Guide</span>
            </h2>
            <div className="prose max-w-none">
              {typeof project.implementation === 'string' ? (
                <p className="text-gray-700 whitespace-pre-wrap">{project.implementation}</p>
              ) : (
                <div className="space-y-4">
                  {project.implementation.steps && project.implementation.steps.map((step: any, index: number) => (
                    <div key={index} className="border-l-4 border-orange-400 pl-4">
                      <h3 className="font-semibold text-gray-900 mb-2">Step {index + 1}: {step.title}</h3>
                      <p className="text-gray-700">{step.description}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        )}

        {/* Call to Action */}
        <div className="bg-gradient-to-r from-green-600 to-teal-600 rounded-xl shadow-lg p-8 text-white text-center">
          <h2 className="text-2xl font-bold mb-4">Ready to Build?</h2>
          <p className="text-green-50 mb-6">
            Start implementing this project and apply what you've learned in Week {week.weekNumber}!
          </p>
          <div className="flex items-center justify-center space-x-4">
            <Link
              href={`/day/${(week.weekNumber - 1) * 7 + 1}`}
              className="inline-flex items-center space-x-2 bg-white text-green-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition"
            >
              <ArrowLeft className="w-5 h-5" />
              <span>Review Week {week.weekNumber} Lessons</span>
            </Link>
            <Link
              href="/dashboard"
              className="inline-flex items-center space-x-2 bg-green-700 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-800 transition"
            >
              <span>Back to Dashboard</span>
            </Link>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center text-gray-600">
            <p className="font-semibold mb-2">30-Day AI Systems Builder Path</p>
            <p className="text-sm mb-4">Transform from automation beginner to AI systems architect</p>
            <div className="flex items-center justify-center space-x-2 text-sm">
              <span>Created by</span>
              <a
                href="https://www.linkedin.com/in/amnasahamed/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center space-x-1 text-blue-600 hover:text-blue-700 font-medium transition"
              >
                <span>Amnas Ahamed</span>
                <Linkedin className="w-4 h-4" />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
