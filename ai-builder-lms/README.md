# 🚀 AI Systems Builder LMS

A complete Learning Management System for the 30-Day AI Systems Builder Path. Transform from automation beginner to AI systems architect with this self-paced, interactive learning platform.

## ✨ Features

- 📚 **30 Days of Structured Content** - Day-by-day lessons with theory, code examples, and exercises
- 💻 **Syntax Highlighting** - Beautiful code examples with Prism.js
- ✅ **Progress Tracking** - Mark lessons complete and track your journey
- 📝 **Note-Taking** - Take and save notes for each lesson
- 🎯 **Weekly Projects** - Hands-on projects to cement your learning
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 🐳 **Docker Ready** - One-command deployment
- 💾 **File-Based Storage** - No database needed, progress saved to JSON files

## 🛠️ Tech Stack

- **Frontend**: Next.js 14 + React 18
- **Styling**: Tailwind CSS
- **Code Highlighting**: react-syntax-highlighter
- **Icons**: Lucide React
- **Backend**: Next.js API Routes
- **Storage**: File-based JSON (no database required)
- **Deployment**: Docker + docker-compose

## 📋 Prerequisites

Before you begin, ensure you have:

- **Docker** and **Docker Compose** installed
  - [Install Docker](https://docs.docker.com/get-docker/)
  - [Install Docker Compose](https://docs.docker.com/compose/install/)

OR for local development:

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **npm** or **yarn**

## 🚀 Quick Start (Docker - Recommended)

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-builder-lms
```

### 2. Start with Docker Compose

```bash
docker-compose up -d
```

### 3. Access the LMS

Open your browser and visit:

```
http://localhost:3000
```

That's it! 🎉 Your LMS is now running.

### Stopping the LMS

```bash
docker-compose down
```

### Viewing Logs

```bash
docker-compose logs -f
```

## 💻 Local Development Setup

If you prefer to run without Docker:

### 1. Install dependencies

```bash
npm install
```

### 2. Run development server

```bash
npm run dev
```

### 3. Access the LMS

```
http://localhost:3000
```

### 4. Build for production

```bash
npm run build
npm start
```

## 📁 Project Structure

```
ai-builder-lms/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── progress/
│   │   │       └── route.ts          # Progress tracking API
│   │   ├── day/
│   │   │   └── [id]/
│   │   │       └── page.tsx          # Individual lesson pages
│   │   ├── resources/
│   │   │   └── page.tsx              # Resources page
│   │   ├── globals.css               # Global styles
│   │   ├── layout.tsx                # Root layout
│   │   └── page.tsx                  # Dashboard/Home page
│   └── data/
│       └── courseData.json           # All course content
├── data/
│   └── progress.json                 # User progress (auto-created)
├── Dockerfile                        # Docker build instructions
├── docker-compose.yml                # Docker Compose configuration
├── package.json                      # Node dependencies
└── README.md                         # You are here!
```

## 📊 Data Persistence

Your progress is automatically saved to `data/progress.json`. This file is:

- ✅ Created automatically on first use
- ✅ Persisted across container restarts (via Docker volume)
- ✅ Human-readable JSON format
- ✅ Can be backed up easily

### Backing up your progress

```bash
# Copy progress file
cp data/progress.json data/progress.backup.json

# Or backup entire data directory
tar -czf progress-backup.tar.gz data/
```

### Resetting progress

```bash
# Stop the container
docker-compose down

# Remove progress file
rm data/progress.json

# Restart
docker-compose up -d
```

## 🎨 Customization

### Changing Port

Edit `docker-compose.yml`:

```yaml
ports:
  - "8080:3000"  # Change 8080 to your preferred port
```

### Adding Content

Edit `src/data/courseData.json` to add more lessons, modify content, or add new weeks.

The structure is:

```json
{
  "weeks": [
    {
      "weekNumber": 1,
      "title": "Week Title",
      "days": [
        {
          "dayNumber": 1,
          "title": "Lesson Title",
          "content": {
            "theory": "...",
            "concepts": [...],
            "codeExamples": [...]
          },
          "practice": {...},
          "keyTakeaways": [...],
          "resources": [...]
        }
      ]
    }
  ]
}
```

## 🔧 Troubleshooting

### Container won't start

```bash
# Check logs
docker-compose logs

# Rebuild from scratch
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Port already in use

```bash
# Check what's using port 3000
lsof -i :3000

# Or change the port in docker-compose.yml
```

### Progress not saving

```bash
# Check data directory permissions
ls -la data/

# Ensure directory exists and is writable
mkdir -p data
chmod 755 data
```

### npm install fails

```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

## 🌐 Deployment

### Deploy to Your Server

1. **SSH into your server**

```bash
ssh user@your-server.com
```

2. **Clone and start**

```bash
git clone <your-repo-url>
cd ai-builder-lms
docker-compose up -d
```

3. **Access via server IP**

```
http://your-server-ip:3000
```

### Using Nginx Reverse Proxy

Create `/etc/nginx/sites-available/ai-lms`:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable and restart:

```bash
sudo ln -s /etc/nginx/sites-available/ai-lms /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Adding SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## 📖 Usage Guide

### For Learners

1. **Start at Day 1** - Click "Start Day 1" from the dashboard
2. **Read the lesson** - Go through theory, concepts, and code examples
3. **Try the practice exercise** - Use the starter code and hints
4. **Take notes** - Use the notes section to record key insights
5. **Mark complete** - Click "Mark Complete" when done
6. **Move to next day** - Click "Next Day" to continue

### Daily Routine

- Spend 30 minutes per day
- Don't skip the practice exercises
- Take notes on key concepts
- Review code examples carefully
- Build the weekly projects

## 🎯 Course Overview

### Week 1: JavaScript for Automations
- Days 1-5: JS fundamentals
- Days 6-7: Data Transformer project

### Week 2: APIs and Logic Flow
- Days 8-12: API integration
- Days 13-14: Weather Alert Bot project

### Week 3: Smart Agents & AI APIs
- Days 15-19: AI integration
- Days 20-21: Smart Assistant project

### Week 4: Python & System Architecture
- Days 22-26: Python + AI systems
- Days 27-30: Full RAG System capstone

## 🤝 Contributing

This is a personal learning management system, but you can:

1. **Fork the repo** for your own use
2. **Customize content** for your learning goals
3. **Add new features** you'd find useful
4. **Share improvements** via pull requests

## 📝 License

This project is open source and available for personal use.

## 🆘 Support

- 📚 Check the [Resources page](http://localhost:3000/resources)
- 🐛 Found a bug? Check the Troubleshooting section
- 💡 Have a question? Review the course content structure

## 🎓 Credits

Created for the **30-Day AI Systems Builder Path** - a comprehensive program to master AI automation and system design.

---

**Ready to become an AI Systems Builder?** 🚀

Start your journey at [http://localhost:3000](http://localhost:3000)
