import { NextRequest, NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

// Force dynamic rendering for this route
export const dynamic = 'force-dynamic';

const DATA_FILE = path.join(process.cwd(), 'data', 'progress.json')

// Ensure data directory exists
function ensureDataDir() {
  const dataDir = path.join(process.cwd(), 'data')
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true })
  }
}

// Read progress data
function readProgress() {
  ensureDataDir()
  try {
    if (fs.existsSync(DATA_FILE)) {
      const data = fs.readFileSync(DATA_FILE, 'utf-8')
      return JSON.parse(data)
    }
  } catch (error) {
    console.error('Error reading progress:', error)
  }
  return {
    completedDays: [],
    notes: {},
    lastActivity: null
  }
}

// Write progress data
function writeProgress(data: any) {
  ensureDataDir()
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2))
    return true
  } catch (error) {
    console.error('Error writing progress:', error)
    return false
  }
}

// GET - Retrieve progress
export async function GET() {
  try {
    const progress = readProgress()
    return NextResponse.json(progress)
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch progress' },
      { status: 500 }
    )
  }
}

// POST - Update progress
export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const progress = readProgress()

    if (body.action === 'complete_day') {
      const { day } = body
      if (!progress.completedDays.includes(day)) {
        progress.completedDays.push(day)
        progress.completedDays.sort((a: number, b: number) => a - b)
      }
    } else if (body.action === 'uncomplete_day') {
      const { day } = body
      progress.completedDays = progress.completedDays.filter((d: number) => d !== day)
    } else if (body.action === 'save_note') {
      const { day, note } = body
      progress.notes[day] = {
        content: note,
        updatedAt: new Date().toISOString()
      }
    }

    progress.lastActivity = new Date().toISOString()

    const success = writeProgress(progress)

    if (success) {
      return NextResponse.json(progress)
    } else {
      return NextResponse.json(
        { error: 'Failed to save progress' },
        { status: 500 }
      )
    }
  } catch (error) {
    return NextResponse.json(
      { error: 'Invalid request' },
      { status: 400 }
    )
  }
}

// DELETE - Reset progress
export async function DELETE() {
  try {
    const emptyProgress = {
      completedDays: [],
      notes: {},
      lastActivity: new Date().toISOString()
    }
    writeProgress(emptyProgress)
    return NextResponse.json({ message: 'Progress reset successfully' })
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to reset progress' },
      { status: 500 }
    )
  }
}
