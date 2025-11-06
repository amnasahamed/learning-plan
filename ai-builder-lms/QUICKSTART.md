# ⚡ Quick Start Guide

Get your AI Builder LMS running in under 5 minutes!

## 🚀 Option 1: Docker (Recommended)

### Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))

### Steps

```bash
# 1. Navigate to the project
cd ai-builder-lms

# 2. Start the application
docker-compose up -d

# 3. Open your browser
# Visit: http://localhost:3000
```

**That's it!** 🎉

### Stop the application

```bash
docker-compose down
```

---

## 💻 Option 2: Local Development

### Prerequisites
- Node.js 18+ ([Download](https://nodejs.org/))

### Steps

```bash
# 1. Navigate to the project
cd ai-builder-lms

# 2. Install dependencies (first time only)
npm install

# 3. Start development server
npm run dev

# 4. Open your browser
# Visit: http://localhost:3000
```

### Build for production

```bash
npm run build
npm start
```

---

## 📱 First Steps in the LMS

1. **Dashboard** - See your progress overview
2. **Start Day 1** - Click "Start Day 1" button
3. **Learn** - Read through the lesson content
4. **Practice** - Try the coding exercises
5. **Take Notes** - Use the notes section
6. **Mark Complete** - Check off when done
7. **Continue** - Move to Day 2

---

## 🔧 Common Commands

### Docker

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f

# Restart
docker-compose restart

# Rebuild
docker-compose up -d --build
```

### NPM

```bash
# Development
npm run dev

# Production
npm run build
npm start

# Lint
npm run lint
```

---

## 📊 Your Progress

Your learning progress is automatically saved to:
- Docker: `./data/progress.json`
- Local: `./data/progress.json`

This file persists across restarts!

---

## 🆘 Troubleshooting

### Port 3000 already in use

**Docker:**
Edit `docker-compose.yml`:
```yaml
ports:
  - "8080:3000"  # Change 8080 to your preferred port
```

**Local:**
```bash
PORT=8080 npm start
```

### Cannot connect

1. Check if it's running: `docker-compose ps` or check terminal
2. Try: `http://127.0.0.1:3000`
3. Check firewall settings

### Docker build fails

```bash
# Clear and rebuild
docker-compose down
docker system prune -a
docker-compose up -d --build
```

### npm install fails

```bash
# Clear cache
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

---

## 🎯 Next Steps

1. ✅ Get the app running
2. 📖 Read [README.md](./README.md) for full documentation
3. 🚀 Read [SETUP.md](./SETUP.md) for server deployment
4. 📚 Start Day 1 of your learning journey!

---

## 💡 Tips

- **Daily commitment**: Spend 30 minutes each day
- **Don't skip practice**: Code examples are crucial
- **Take notes**: Use the built-in note-taking feature
- **Build projects**: Complete the weekly projects
- **Stay consistent**: Learning compounds over time

---

**Ready to become an AI Systems Builder?** 🚀

Visit [http://localhost:3000](http://localhost:3000) and start Day 1!
