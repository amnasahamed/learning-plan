import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import { verifyToken, sanitizeUser, User } from '@/lib/auth';

// Force dynamic rendering for this route
export const dynamic = 'force-dynamic';

const USERS_FILE = path.join(process.cwd(), 'data', 'users.json');

function getUsers(): User[] {
  try {
    if (fs.existsSync(USERS_FILE)) {
      const data = fs.readFileSync(USERS_FILE, 'utf-8');
      return JSON.parse(data);
    }
  } catch (error) {
    console.error('Error reading users:', error);
  }
  return [];
}

export async function GET(request: NextRequest) {
  try {
    // Get token from cookie or header
    const token = request.cookies.get('auth-token')?.value ||
                  request.headers.get('authorization')?.replace('Bearer ', '');

    if (!token) {
      return NextResponse.json(
        { error: 'Not authenticated' },
        { status: 401 }
      );
    }

    // Verify token
    const decoded = verifyToken(token);

    if (!decoded) {
      return NextResponse.json(
        { error: 'Invalid token' },
        { status: 401 }
      );
    }

    // Find user
    const users = getUsers();
    const user = users.find(u => u.id === decoded.userId);

    if (!user) {
      return NextResponse.json(
        { error: 'User not found' },
        { status: 404 }
      );
    }

    return NextResponse.json({
      user: sanitizeUser(user)
    });
  } catch (error) {
    console.error('Auth verification error:', error);
    return NextResponse.json(
      { error: 'Authentication failed' },
      { status: 500 }
    );
  }
}
