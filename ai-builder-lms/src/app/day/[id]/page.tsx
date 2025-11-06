'use client'

import { useEffect, useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import Link from 'next/link'
import {
  ArrowLeft, ArrowRight, CheckCircle2, Circle, Book, Code2,
  Target, Lightbulb, ExternalLink, Save, ChevronDown, ChevronUp
} from 'lucide-react'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism'
import courseData from '@/data/courseData.json'

export default function DayPage() {
  const params = useParams()
  const router = useRouter()
  const dayId = parseInt(params.id as string)

  const [isCompleted, setIsCompleted] = useState(false)
  const [note, setNote] = useState('')
  const [savedNote, setSavedNote] = useState('')
  const [showSolution, setShowSolution] = useState(false)
  const [loading, setLoading] = useState(true)

  // Find the day data
  const findDayData = () => {
    for (const week of courseData.weeks) {
      const day = week.days.find(d => d.dayNumber === dayId)
      if (day) {
        return { day, week }
      }
    }
    return null
  }

  const dayData = findDayData()

  useEffect(() => {
    fetchProgress()
  }, [dayId])

  const fetchProgress = async () => {
    try {
      const res = await fetch('/api/progress')
      const data = await res.json()
      setIsCompleted(data.completedDays?.includes(dayId) || false)
      setSavedNote(data.notes?.[dayId]?.content || '')
      setNote(data.notes?.[dayId]?.content || '')
    } catch (error) {
      console.error('Error fetching progress:', error)
    } finally {
      setLoading(false)
    }
  }

  const toggleComplete = async () => {
    try {
      const action = isCompleted ? 'uncomplete_day' : 'complete_day'
      await fetch('/api/progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action, day: dayId })
      })
      setIsCompleted(!isCompleted)
    } catch (error) {
      console.error('Error updating progress:', error)
    }
  }

  const saveNote = async () => {
    try {
      await fetch('/api/progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'save_note', day: dayId, note })
      })
      setSavedNote(note)
      alert('Note saved successfully!')
    } catch (error) {
      console.error('Error saving note:', error)
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading lesson...</p>
        </div>
      </div>
    )
  }

  if (!dayData) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">Day not found</h1>
          <Link href="/" className="text-blue-600 hover:underline">
            Return to dashboard
          </Link>
        </div>
      </div>
    )
  }

  const { day, week } = dayData

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <Link
              href="/"
              className="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition"
            >
              <ArrowLeft className="w-5 h-5" />
              <span className="font-medium">Back to Dashboard</span>
            </Link>
            <button
              onClick={toggleComplete}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-medium transition ${
                isCompleted
                  ? 'bg-green-100 text-green-700 hover:bg-green-200'
                  : 'bg-blue-600 text-white hover:bg-blue-700'
              }`}
            >
              {isCompleted ? (
                <>
                  <CheckCircle2 className="w-5 h-5" />
                  <span>Completed</span>
                </>
              ) : (
                <>
                  <Circle className="w-5 h-5" />
                  <span>Mark Complete</span>
                </>
              )}
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Day Header */}
        <div className="mb-8 fade-in">
          <div className="flex items-center space-x-2 text-sm text-gray-600 mb-2">
            <span>Week {week.weekNumber}</span>
            <span>•</span>
            <span>Day {day.dayNumber}</span>
            <span>•</span>
            <span>{day.duration}</span>
          </div>
          <h1 className="text-4xl font-bold text-gray-900 mb-4">{day.title}</h1>

          {/* Learning Objectives */}
          <div className="bg-blue-50 border border-blue-200 rounded-xl p-6">
            <div className="flex items-center space-x-2 mb-3">
              <Target className="w-5 h-5 text-blue-600" />
              <h2 className="text-lg font-semibold text-gray-900">Learning Objectives</h2>
            </div>
            <ul className="space-y-2">
              {day.learningObjectives.map((objective, i) => (
                <li key={i} className="flex items-start space-x-2">
                  <CheckCircle2 className="w-5 h-5 text-blue-600 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">{objective}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Theory Section */}
        <section className="mb-8 bg-white rounded-2xl shadow-lg border border-gray-100 p-8 fade-in">
          <div className="flex items-center space-x-2 mb-6">
            <Book className="w-6 h-6 text-purple-600" />
            <h2 className="text-2xl font-bold text-gray-900">Theory</h2>
          </div>

          <div className="prose prose-lg max-w-none">
            {day.content.theory.split('\n\n').map((paragraph, i) => {
              if (paragraph.startsWith('**') && paragraph.endsWith('**')) {
                return (
                  <h3 key={i} className="text-xl font-bold text-gray-900 mt-6 mb-3">
                    {paragraph.replace(/\*\*/g, '')}
                  </h3>
                )
              }
              return (
                <p key={i} className="text-gray-700 leading-relaxed mb-4">
                  {paragraph.split(/(\*\*.*?\*\*)/).map((part, j) => {
                    if (part.startsWith('**') && part.endsWith('**')) {
                      return <strong key={j}>{part.replace(/\*\*/g, '')}</strong>
                    }
                    if (part.includes('`') && !part.includes('```')) {
                      return part.split(/(`.*?`)/).map((subpart, k) => {
                        if (subpart.startsWith('`') && subpart.endsWith('`')) {
                          return (
                            <code key={k} className="bg-gray-100 px-2 py-1 rounded text-sm font-mono">
                              {subpart.replace(/`/g, '')}
                            </code>
                          )
                        }
                        return subpart
                      })
                    }
                    return part
                  })}
                </p>
              )
            })}
          </div>

          {/* Concepts */}
          <div className="mt-8 space-y-4">
            {day.content.concepts.map((concept, i) => (
              <div key={i} className="bg-gray-50 rounded-xl p-6 border border-gray-200">
                <h3 className="text-lg font-bold text-gray-900 mb-2">{concept.name}</h3>
                <p className="text-gray-700 mb-4">{concept.explanation}</p>
                <SyntaxHighlighter
                  language="javascript"
                  style={vscDarkPlus}
                  customStyle={{
                    borderRadius: '0.75rem',
                    padding: '1rem',
                    fontSize: '0.9rem'
                  }}
                >
                  {concept.example}
                </SyntaxHighlighter>
              </div>
            ))}
          </div>
        </section>

        {/* Code Examples */}
        <section className="mb-8 bg-white rounded-2xl shadow-lg border border-gray-100 p-8 fade-in">
          <div className="flex items-center space-x-2 mb-6">
            <Code2 className="w-6 h-6 text-blue-600" />
            <h2 className="text-2xl font-bold text-gray-900">Code Examples</h2>
          </div>

          <div className="space-y-6">
            {day.content.codeExamples.map((example, i) => (
              <div key={i} className="border border-gray-200 rounded-xl overflow-hidden">
                <div className="bg-gray-50 px-6 py-4 border-b border-gray-200">
                  <h3 className="font-bold text-gray-900">{example.title}</h3>
                </div>
                <div className="p-6">
                  <SyntaxHighlighter
                    language={example.language}
                    style={vscDarkPlus}
                    customStyle={{
                      borderRadius: '0.75rem',
                      padding: '1rem',
                      fontSize: '0.9rem'
                    }}
                    showLineNumbers
                  >
                    {example.code}
                  </SyntaxHighlighter>
                  <div className="mt-4 bg-blue-50 border border-blue-200 rounded-lg p-4">
                    <p className="text-sm text-gray-700">
                      <strong className="text-blue-700">Explanation:</strong> {example.explanation}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Practice Exercise */}
        <section className="mb-8 bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl shadow-lg border border-green-200 p-8 fade-in">
          <div className="flex items-center space-x-2 mb-6">
            <Target className="w-6 h-6 text-green-600" />
            <h2 className="text-2xl font-bold text-gray-900">Practice Exercise</h2>
          </div>

          <div className="bg-white rounded-xl p-6 mb-6">
            <h3 className="text-xl font-bold text-gray-900 mb-4">{day.practice.title}</h3>
            <div className="prose max-w-none mb-4">
              {day.practice.instructions.split('\n').map((line, i) => (
                <p key={i} className="text-gray-700 mb-2">{line}</p>
              ))}
            </div>

            {/* Starter Code */}
            <div className="mb-6">
              <h4 className="font-semibold text-gray-900 mb-3">Starter Code:</h4>
              <SyntaxHighlighter
                language="javascript"
                style={vscDarkPlus}
                customStyle={{
                  borderRadius: '0.75rem',
                  padding: '1rem',
                  fontSize: '0.9rem'
                }}
              >
                {day.practice.starterCode}
              </SyntaxHighlighter>
            </div>

            {/* Hints */}
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-6">
              <div className="flex items-center space-x-2 mb-3">
                <Lightbulb className="w-5 h-5 text-yellow-600" />
                <h4 className="font-semibold text-gray-900">Hints:</h4>
              </div>
              <ul className="space-y-2">
                {day.practice.hints.map((hint, i) => (
                  <li key={i} className="text-sm text-gray-700 flex items-start space-x-2">
                    <span className="text-yellow-600 font-bold">•</span>
                    <span>{hint}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Solution Toggle */}
            <div>
              <button
                onClick={() => setShowSolution(!showSolution)}
                className="flex items-center space-x-2 text-gray-700 hover:text-gray-900 font-medium mb-4"
              >
                {showSolution ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
                <span>{showSolution ? 'Hide' : 'Show'} Solution</span>
              </button>

              {showSolution && (
                <div className="fade-in">
                  <SyntaxHighlighter
                    language="javascript"
                    style={vscDarkPlus}
                    customStyle={{
                      borderRadius: '0.75rem',
                      padding: '1rem',
                      fontSize: '0.9rem'
                    }}
                    showLineNumbers
                  >
                    {day.practice.solution}
                  </SyntaxHighlighter>
                </div>
              )}
            </div>
          </div>
        </section>

        {/* Key Takeaways */}
        <section className="mb-8 bg-white rounded-2xl shadow-lg border border-gray-100 p-8 fade-in">
          <div className="flex items-center space-x-2 mb-6">
            <Lightbulb className="w-6 h-6 text-yellow-500" />
            <h2 className="text-2xl font-bold text-gray-900">Key Takeaways</h2>
          </div>
          <ul className="space-y-3">
            {day.keyTakeaways.map((takeaway, i) => (
              <li key={i} className="flex items-start space-x-3">
                <CheckCircle2 className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">{takeaway}</span>
              </li>
            ))}
          </ul>
        </section>

        {/* Resources */}
        <section className="mb-8 bg-white rounded-2xl shadow-lg border border-gray-100 p-8 fade-in">
          <div className="flex items-center space-x-2 mb-6">
            <ExternalLink className="w-6 h-6 text-purple-600" />
            <h2 className="text-2xl font-bold text-gray-900">Additional Resources</h2>
          </div>
          <div className="space-y-3">
            {day.resources.map((resource, i) => (
              <a
                key={i}
                href={resource.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-between p-4 bg-gray-50 hover:bg-gray-100 rounded-lg border border-gray-200 transition"
              >
                <div>
                  <div className="font-semibold text-gray-900">{resource.title}</div>
                  <div className="text-sm text-gray-600 capitalize">{resource.type}</div>
                </div>
                <ExternalLink className="w-5 h-5 text-gray-400" />
              </a>
            ))}
          </div>
        </section>

        {/* Notes Section */}
        <section className="mb-8 bg-white rounded-2xl shadow-lg border border-gray-100 p-8 fade-in">
          <div className="flex items-center space-x-2 mb-6">
            <Save className="w-6 h-6 text-blue-600" />
            <h2 className="text-2xl font-bold text-gray-900">Your Notes</h2>
          </div>
          <textarea
            value={note}
            onChange={(e) => setNote(e.target.value)}
            placeholder="Take notes about what you learned today..."
            className="w-full h-40 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
          />
          <div className="flex items-center justify-between mt-4">
            <span className="text-sm text-gray-500">
              {note === savedNote ? 'All changes saved' : 'Unsaved changes'}
            </span>
            <button
              onClick={saveNote}
              disabled={note === savedNote}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-medium transition ${
                note === savedNote
                  ? 'bg-gray-200 text-gray-500 cursor-not-allowed'
                  : 'bg-blue-600 text-white hover:bg-blue-700'
              }`}
            >
              <Save className="w-4 h-4" />
              <span>Save Note</span>
            </button>
          </div>
        </section>

        {/* Navigation */}
        <div className="flex items-center justify-between">
          {dayId > 1 ? (
            <Link
              href={`/day/${dayId - 1}`}
              className="flex items-center space-x-2 px-6 py-3 bg-white hover:bg-gray-50 text-gray-700 rounded-lg border border-gray-300 transition font-medium"
            >
              <ArrowLeft className="w-5 h-5" />
              <span>Previous Day</span>
            </Link>
          ) : (
            <div></div>
          )}

          {dayId < 30 ? (
            <Link
              href={`/day/${dayId + 1}`}
              className="flex items-center space-x-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition font-medium ml-auto"
            >
              <span>Next Day</span>
              <ArrowRight className="w-5 h-5" />
            </Link>
          ) : (
            <Link
              href="/"
              className="flex items-center space-x-2 px-6 py-3 bg-green-600 hover:bg-green-700 text-white rounded-lg transition font-medium ml-auto"
            >
              <CheckCircle2 className="w-5 h-5" />
              <span>Complete Course!</span>
            </Link>
          )}
        </div>
      </main>
    </div>
  )
}
