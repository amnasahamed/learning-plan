'use client'

import { useEffect, useState } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/context/AuthContext'
import { BookOpen, Code, Rocket, Target, CheckCircle2, Circle, Clock, Award, LogOut, User, Linkedin } from 'lucide-react'

export default function DashboardPage() {
  const [progress, setProgress] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const { user, loading: authLoading, logout } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (!authLoading && !user) {
      router.push('/login')
    }
  }, [user, authLoading, router])

  useEffect(() => {
    if (user) {
      fetchProgress()
    }
  }, [user])

  const fetchProgress = async () => {
    try {
      const res = await fetch('/api/progress')
      const data = await res.json()
      setProgress(data)
    } catch (error) {
      console.error('Error fetching progress:', error)
    } finally {
      setLoading(false)
    }
  }

  const completedDays = progress?.completedDays?.length || 0
  const totalDays = 30
  const progressPercent = (completedDays / totalDays) * 100

  const weeks = [
    {
      number: 1,
      title: 'JavaScript for Automations',
      icon: Code,
      days: [1, 2, 3, 4, 5],
      project: 'Smart Data Transformer',
      color: 'bg-blue-500'
    },
    {
      number: 2,
      title: 'APIs and Logic Flow',
      icon: Target,
      days: [8, 9, 10, 11, 12],
      project: 'Weather Alert Bot',
      color: 'bg-purple-500'
    },
    {
      number: 3,
      title: 'Smart Agents & AI APIs',
      icon: Rocket,
      days: [15, 16, 17, 18, 19],
      project: 'Context-Aware AI Assistant',
      color: 'bg-pink-500'
    },
    {
      number: 4,
      title: 'Python & System Architecture',
      icon: Award,
      days: [22, 23, 24, 25, 26],
      project: 'Full RAG System',
      color: 'bg-green-500'
    }
  ]

  if (authLoading || !user) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
                <Rocket className="w-7 h-7 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">AI Systems Builder</h1>
                <p className="text-sm text-gray-600">30-Day Learning Path</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Link
                href="/resources"
                className="text-gray-700 hover:text-blue-600 font-medium transition"
              >
                Resources
              </Link>
              <div className="flex items-center space-x-2 text-gray-700">
                <User className="w-4 h-4" />
                <span className="text-sm font-medium">{user?.name}</span>
              </div>
              <button
                onClick={logout}
                className="flex items-center space-x-2 text-gray-700 hover:text-red-600 transition"
              >
                <LogOut className="w-4 h-4" />
                <span className="text-sm font-medium">Logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Progress Overview */}
        <div className="mb-8 bg-white rounded-2xl shadow-lg p-8 border border-gray-100">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">Your Progress</h2>
              <p className="text-gray-600 mt-1">Keep the momentum going!</p>
            </div>
            <div className="text-right">
              <div className="text-4xl font-bold text-blue-600">{completedDays}/30</div>
              <div className="text-sm text-gray-500">Days Completed</div>
            </div>
          </div>

          {/* Progress Bar */}
          <div className="relative">
            <div className="h-4 bg-gray-200 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-blue-500 to-purple-600 progress-bar"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
            <div className="text-sm text-gray-600 mt-2 text-right">
              {progressPercent.toFixed(0)}% Complete
            </div>
          </div>

          {/* Quick Stats */}
          <div className="grid grid-cols-3 gap-4 mt-6">
            <div className="bg-blue-50 rounded-xl p-4 border border-blue-100">
              <div className="flex items-center space-x-2">
                <Clock className="w-5 h-5 text-blue-600" />
                <span className="text-sm font-medium text-gray-700">Time/Day</span>
              </div>
              <div className="text-2xl font-bold text-blue-600 mt-2">30 min</div>
            </div>
            <div className="bg-purple-50 rounded-xl p-4 border border-purple-100">
              <div className="flex items-center space-x-2">
                <BookOpen className="w-5 h-5 text-purple-600" />
                <span className="text-sm font-medium text-gray-700">Current Week</span>
              </div>
              <div className="text-2xl font-bold text-purple-600 mt-2">
                Week {Math.min(Math.floor(completedDays / 7) + 1, 4)}
              </div>
            </div>
            <div className="bg-green-50 rounded-xl p-4 border border-green-100">
              <div className="flex items-center space-x-2">
                <Target className="w-5 h-5 text-green-600" />
                <span className="text-sm font-medium text-gray-700">Projects</span>
              </div>
              <div className="text-2xl font-bold text-green-600 mt-2">
                {Math.floor(completedDays / 7)}/4
              </div>
            </div>
          </div>
        </div>

        {/* Course Curriculum */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Course Curriculum</h2>
          <div className="grid gap-6 md:grid-cols-2">
            {weeks.map((week) => {
              const Icon = week.icon
              const weekCompleted = week.days.every(day =>
                progress?.completedDays?.includes(day)
              )
              const someCompleted = week.days.some(day =>
                progress?.completedDays?.includes(day)
              )

              return (
                <div
                  key={week.number}
                  className="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden card-hover"
                >
                  {/* Header */}
                  <div className={`${week.color} p-6 text-white`}>
                    <div className="flex items-start justify-between">
                      <div>
                        <div className="text-sm font-semibold opacity-90 mb-1">
                          Week {week.number}
                        </div>
                        <h3 className="text-xl font-bold mb-2">{week.title}</h3>
                        <div className="flex items-center space-x-2 text-sm opacity-90">
                          <Icon className="w-4 h-4" />
                          <span>Project: {week.project}</span>
                        </div>
                      </div>
                      {weekCompleted && (
                        <CheckCircle2 className="w-8 h-8" />
                      )}
                    </div>
                  </div>

                  {/* Days */}
                  <div className="p-6">
                    <div className="flex items-center justify-between mb-4">
                      <span className="text-sm font-semibold text-gray-700">Daily Lessons</span>
                      <span className="text-xs text-gray-500">
                        {week.days.filter(d => progress?.completedDays?.includes(d)).length}/{week.days.length} complete
                      </span>
                    </div>
                    <div className="space-y-2">
                      {week.days.map((day) => {
                        const isCompleted = progress?.completedDays?.includes(day)
                        return (
                          <Link
                            key={day}
                            href={`/day/${day}`}
                            className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50 transition border border-gray-100"
                          >
                            <div className="flex items-center space-x-3">
                              {isCompleted ? (
                                <CheckCircle2 className="w-5 h-5 text-green-500" />
                              ) : (
                                <Circle className="w-5 h-5 text-gray-300" />
                              )}
                              <span className={`font-medium ${isCompleted ? 'text-gray-500' : 'text-gray-900'}`}>
                                Day {day}
                              </span>
                            </div>
                            <span className="text-sm text-gray-500">30 min →</span>
                          </Link>
                        )
                      })}
                    </div>

                    {/* Project Link */}
                    <Link
                      href={`/project/${week.number}`}
                      className="mt-4 w-full flex items-center justify-center space-x-2 bg-gray-50 hover:bg-gray-100 text-gray-700 font-semibold py-3 rounded-lg transition border border-gray-200"
                    >
                      <Target className="w-4 h-4" />
                      <span>Week {week.number} Project</span>
                    </Link>
                  </div>
                </div>
              )
            })}
          </div>
        </div>

        {/* Call to Action */}
        <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl shadow-xl p-8 text-white text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Start Learning?</h2>
          <p className="text-blue-100 mb-6 text-lg">
            Begin your journey to becoming an AI Systems Builder today
          </p>
          <Link
            href="/day/1"
            className="inline-flex items-center space-x-2 bg-white text-blue-600 px-8 py-3 rounded-lg font-bold hover:bg-gray-100 transition"
          >
            <Rocket className="w-5 h-5" />
            <span>Start Day 1</span>
          </Link>
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
                <span>Amna Sahamed</span>
                <Linkedin className="w-4 h-4" />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
