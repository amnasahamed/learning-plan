import { NextResponse } from 'next/server';

// Force dynamic rendering for this route
export const dynamic = 'force-dynamic';

export async function POST() {
  const response = NextResponse.json({ success: true });

  // Clear the auth cookie
  response.cookies.delete('auth-token');

  return response;
}
