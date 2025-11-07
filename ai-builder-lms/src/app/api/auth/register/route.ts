import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import { hashPassword, generateToken, sanitizeUser, User } from '@/lib/auth';

// Force dynamic rendering for this route
export const dynamic = 'force-dynamic';

const USERS_FILE = path.join(process.cwd(), 'data', 'users.json');

function ensureUsersFile() {
  const dataDir = path.join(process.cwd(), 'data');
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }
  if (!fs.existsSync(USERS_FILE)) {
    fs.writeFileSync(USERS_FILE, JSON.stringify([], null, 2));
  }
}

function getUsers(): User[] {
  ensureUsersFile();
  const data = fs.readFileSync(USERS_FILE, 'utf-8');
  return JSON.parse(data);
}

function saveUsers(users: User[]) {
  ensureUsersFile();
  fs.writeFileSync(USERS_FILE, JSON.stringify(users, null, 2));
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { email, password, name } = body;

    // Validation
    if (!email || !password || !name) {
      return NextResponse.json(
        { error: 'Email, password, and name are required' },
        { status: 400 }
      );
    }

    if (password.length < 6) {
      return NextResponse.json(
        { error: 'Password must be at least 6 characters' },
        { status: 400 }
      );
    }

    // Check if user exists
    const users = getUsers();
    const existingUser = users.find(u => u.email.toLowerCase() === email.toLowerCase());

    if (existingUser) {
      return NextResponse.json(
        { error: 'User with this email already exists' },
        { status: 409 }
      );
    }

    // Create new user
    const newUser: User = {
      id: Date.now().toString(),
      email: email.toLowerCase(),
      password: hashPassword(password),
      name,
      createdAt: new Date().toISOString()
    };

    users.push(newUser);
    saveUsers(users);

    // Generate token
    const token = generateToken(newUser.id, newUser.email);

    // Return user data and token
    const response = NextResponse.json({
      user: sanitizeUser(newUser),
      token
    });

    // Set cookie
    response.cookies.set('auth-token', token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: 60 * 60 * 24 * 7 // 7 days
    });

    return response;
  } catch (error) {
    console.error('Registration error:', error);
    return NextResponse.json(
      { error: 'Registration failed' },
      { status: 500 }
    );
  }
}
