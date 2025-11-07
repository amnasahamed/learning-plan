# Docker Deployment Guide

This guide will help you deploy the AI Builder LMS using Docker.

## Prerequisites

- Docker installed (version 20.10 or higher)
- Docker Compose installed (version 2.0 or higher)
- Git installed
- At least 2GB of free disk space

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-builder-lms
```

### 2. Configure Environment Variables

The application requires a JWT secret for authentication. You can either:

**Option A: Use the default secret (for testing only)**
```bash
# The docker-compose.yml will use the default secret
docker-compose up -d
```

**Option B: Set a custom secret (recommended for production)**
```bash
# Create or edit the .env file
echo "JWT_SECRET=your-super-secret-key-change-this" > .env

# Start the application
docker-compose up -d
```

### 3. Access the Application

Once the container is running, access the application at:
- **URL:** http://localhost:737
- **Port:** 737 (configured in docker-compose.yml)

## Detailed Deployment Steps

### Step 1: Build the Docker Image

```bash
# Build the image without cache (fresh build)
docker-compose build --no-cache

# Or build with cache (faster for rebuilds)
docker-compose build
```

### Step 2: Start the Container

```bash
# Start in detached mode (background)
docker-compose up -d

# Or start in foreground to see logs
docker-compose up
```

### Step 3: Verify Deployment

```bash
# Check container status
docker-compose ps

# View logs
docker-compose logs -f

# Check health status
docker inspect ai-builder-lms | grep -A 10 Health
```

## Common Deployment Commands

### View Logs
```bash
# View all logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# View last 100 lines
docker-compose logs --tail=100
```

### Restart the Application
```bash
# Restart the container
docker-compose restart

# Restart with rebuild
docker-compose down
docker-compose up -d --build
```

### Stop the Application
```bash
# Stop containers (data persists)
docker-compose stop

# Stop and remove containers (data persists in volume)
docker-compose down

# Stop and remove everything including volumes (CAUTION: deletes user data)
docker-compose down -v
```

### Update the Application
```bash
# Pull latest code
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose up -d --build
```

## Data Persistence

User data is stored in the `./data` directory on your host machine:
- **Location:** `./data` (mapped to `/app/data` in container)
- **Contents:**
  - `users.json` - User accounts
  - `progress.json` - Learning progress

### Backup User Data
```bash
# Create backup
tar -czf lms-backup-$(date +%Y%m%d).tar.gz data/

# Restore backup
tar -xzf lms-backup-YYYYMMDD.tar.gz
```

## Troubleshooting

### Container Won't Start

1. **Check if port 737 is already in use:**
```bash
# Linux/Mac
lsof -i :737

# Windows
netstat -ano | findstr :737
```

2. **View detailed error logs:**
```bash
docker-compose logs ai-builder-lms
```

3. **Check container status:**
```bash
docker ps -a | grep ai-builder-lms
```

### Build Failures

1. **Clear Docker cache and rebuild:**
```bash
docker-compose down
docker system prune -a
docker-compose build --no-cache
docker-compose up -d
```

2. **Check disk space:**
```bash
df -h
docker system df
```

### Permission Issues

If you encounter permission errors with the data directory:

```bash
# Fix permissions (Linux/Mac)
sudo chown -R 1001:1001 ./data

# Or make it world-writable (less secure)
chmod 777 ./data
```

### Authentication Not Working

1. **Check JWT secret is set:**
```bash
docker-compose exec ai-builder-lms env | grep JWT_SECRET
```

2. **Verify .env file exists:**
```bash
cat .env
```

3. **Restart with updated environment:**
```bash
docker-compose down
docker-compose up -d
```

### Application Running but Can't Access

1. **Check container is actually running:**
```bash
docker-compose ps
```

2. **Test from inside container:**
```bash
docker-compose exec ai-builder-lms wget -O- http://localhost:3000
```

3. **Check firewall settings:**
```bash
# Linux
sudo ufw status
sudo ufw allow 737

# Check if port is listening
netstat -tlnp | grep 737
```

## Production Deployment

### Security Recommendations

1. **Change JWT Secret:**
```bash
# Generate a secure random secret
openssl rand -base64 32

# Add to .env file
echo "JWT_SECRET=<your-generated-secret>" > .env
```

2. **Use HTTPS (Reverse Proxy):**

Install nginx or Caddy as a reverse proxy:

**Nginx Example:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:737;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

**Caddy Example (simpler):**
```
your-domain.com {
    reverse_proxy localhost:737
}
```

3. **Enable Firewall:**
```bash
# Only allow necessary ports
sudo ufw enable
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
```

4. **Regular Backups:**

Set up a cron job for automatic backups:
```bash
# Edit crontab
crontab -e

# Add daily backup at 2 AM
0 2 * * * cd /path/to/ai-builder-lms && tar -czf backups/lms-$(date +\%Y\%m\%d).tar.gz data/
```

### Performance Optimization

1. **Limit container resources:**

Edit `docker-compose.yml`:
```yaml
services:
  ai-builder-lms:
    # ... other config ...
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

2. **Enable logging rotation:**

Edit `docker-compose.yml`:
```yaml
services:
  ai-builder-lms:
    # ... other config ...
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Monitoring

### Health Checks

The container includes automatic health checks:
```bash
# View health status
docker inspect ai-builder-lms --format='{{.State.Health.Status}}'

# View health check logs
docker inspect ai-builder-lms --format='{{range .State.Health.Log}}{{.Output}}{{end}}'
```

### Resource Usage

```bash
# View real-time stats
docker stats ai-builder-lms

# View specific metrics
docker stats ai-builder-lms --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

## Advanced Configuration

### Custom Port

To change the port from 737 to something else:

1. Edit `docker-compose.yml`:
```yaml
ports:
  - "8080:3000"  # Change 737 to your desired port
```

2. Restart:
```bash
docker-compose down
docker-compose up -d
```

### Multiple Instances

To run multiple instances (different ports):

```bash
# Instance 1 (port 737)
docker-compose -p lms-dev up -d

# Instance 2 (port 738)
docker-compose -p lms-staging -f docker-compose.staging.yml up -d
```

## Getting Help

If you encounter issues not covered here:

1. Check container logs: `docker-compose logs -f`
2. Inspect container: `docker inspect ai-builder-lms`
3. Check Docker daemon logs: `journalctl -u docker`
4. Visit the project's GitHub issues page

## Summary

**Quick Commands Cheat Sheet:**
```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Restart
docker-compose restart

# Logs
docker-compose logs -f

# Rebuild
docker-compose up -d --build

# Status
docker-compose ps

# Backup
tar -czf backup.tar.gz data/
```

Your AI Builder LMS should now be running successfully! 🚀
