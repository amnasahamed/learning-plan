# 🔐 Authentication Guide

The AI Builder LMS now includes JWT-based authentication, allowing you to share it with friends and students!

## Features

- ✅ **JWT Authentication** - Secure token-based auth
- ✅ **Email + Password** - Simple registration
- ✅ **Multi-User Support** - Share with friends and students
- ✅ **File-Based Storage** - Lite backend (no database)
- ✅ **Protected Routes** - Dashboard and lessons require login
- ✅ **Persistent Sessions** - 7-day token expiry
- ✅ **n8n Chatbot Integration** - Built-in AI assistant

## User Data Storage

User accounts are stored in `data/users.json` (file-based, keeping it lite!).

```json
{
  "id": "unique-id",
  "email": "user@example.com",
  "password": "hashed-password",
  "name": "User Name",
  "createdAt": "2024-11-06T..."
}
```

Each user's progress is tracked separately in `data/progress.json`.

## How It Works

### Registration Flow
1. User visits `/register`
2. Enters name, email, password
3. Account created in `data/users.json`
4. JWT token issued and stored in cookie
5. Redirected to dashboard

### Login Flow
1. User visits `/login`
2. Enters email and password
3. Credentials verified
4. JWT token issued and stored in cookie
5. Redirected to dashboard

### Protected Routes
- `/dashboard` - Main course dashboard
- `/day/[id]` - Individual lessons
- `/resources` - Learning resources

All protected routes redirect to `/login` if not authenticated.

## Security

- **Passwords**: Hashed with bcrypt (10 rounds)
- **JWT Secret**: Configurable via JWT_SECRET environment variable
- **HTTP-Only Cookies**: Token stored in HTTP-only cookie
- **7-Day Expiry**: Tokens expire after 7 days
- **Secure in Production**: Cookies use secure flag in production

## Configuration

### Environment Variables

Create `.env` file:

```bash
JWT_SECRET=your-super-secret-key-change-this
```

Or set in docker-compose.yml:

```yaml
environment:
  - JWT_SECRET=your-secret-key
```

### Default Configuration

If no JWT_SECRET is provided, defaults to:
```
ai-builder-lms-secret-key-2024
```

**⚠️ IMPORTANT:** Change this in production!

## n8n Chatbot Integration

The LMS includes a chat widget powered by your n8n workflow:

**Webhook URL**: `https://n8n.themelon.in/webhook/be575669-d460-4f3a-be2c-0b8206552977/chat`

The chatbot appears on all pages and can help users with questions about the course.

### How to Update Chatbot

Edit `src/app/layout.tsx`:

```typescript
createChat({
  webhookUrl: 'YOUR_N8N_WEBHOOK_URL'
});
```

## User Management

### View All Users

```bash
cat data/users.json
```

### Manual User Creation

Add to `data/users.json`:

```json
{
  "id": "1699999999999",
  "email": "newuser@example.com",
  "password": "$2a$10$hashedpassword...",
  "name": "New User",
  "createdAt": "2024-11-06T12:00:00.000Z"
}
```

### Reset User Password

1. Generate new hash:
```javascript
const bcrypt = require('bcryptjs');
console.log(bcrypt.hashSync('newpassword', 10));
```

2. Update `data/users.json` with new hash

### Delete User

Remove user object from `data/users.json`

## API Endpoints

### POST /api/auth/register
Register new user

**Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe"
}
```

**Response:**
```json
{
  "user": {
    "id": "...",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "token": "jwt-token..."
}
```

### POST /api/auth/login
Login existing user

**Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "user": { ... },
  "token": "jwt-token..."
}
```

### GET /api/auth/me
Get current user

**Headers:**
```
Cookie: auth-token=jwt-token
```

**Response:**
```json
{
  "user": {
    "id": "...",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

### POST /api/auth/logout
Logout user (clears cookie)

## Sharing with Friends

1. **Deploy** your LMS to a server
2. **Share the URL** with friends/students
3. **They register** with their email
4. **Everyone learns** independently with their own progress!

## Troubleshooting

### "Invalid token" error
- Token expired (7 days)
- JWT_SECRET changed
- **Solution**: Logout and login again

### Can't login after registration
- Check `data/users.json` exists
- Verify file permissions
- Check Docker volume mounting

### Password requirements
- Minimum 6 characters
- No special requirements (keep it simple!)

## Future Enhancements

Possible additions:
- Email verification
- Password reset
- User roles (admin/student)
- Social login (Google, GitHub)
- Profile management

---

**Your LMS is now multi-user ready!** 🎉

Share with your friends and build an AI learning community!
