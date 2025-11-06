# 🚀 Setup Guide

## Quick Setup on Your Server

Follow these steps to deploy the AI Builder LMS on your own server.

## Prerequisites

Your server needs:
- Ubuntu 20.04+ (or similar Linux distribution)
- Docker and Docker Compose installed
- At least 1GB RAM
- Port 3000 available (or customize)

## Step-by-Step Installation

### 1. Connect to Your Server

```bash
ssh your-user@your-server-ip
```

### 2. Install Docker (if not installed)

```bash
# Update package index
sudo apt update

# Install required packages
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Add your user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Log out and back in for group changes to take effect
exit
```

### 3. Clone the Repository

```bash
# SSH back into your server
ssh your-user@your-server-ip

# Clone your repository
git clone https://github.com/your-username/ai-builder-lms.git
cd ai-builder-lms
```

### 4. Start the Application

```bash
# Build and start with docker-compose
docker-compose up -d

# Check status
docker-compose ps

# View logs (optional)
docker-compose logs -f
```

### 5. Access the LMS

Open your browser and visit:

```
http://your-server-ip:3000
```

## 🎯 You're Done!

The LMS is now running and ready to use.

## Management Commands

### Check Status

```bash
docker-compose ps
```

### View Logs

```bash
# All logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# Last 100 lines
docker-compose logs --tail=100
```

### Restart the Application

```bash
docker-compose restart
```

### Stop the Application

```bash
docker-compose down
```

### Update the Application

```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose up -d --build
```

## 🔒 Security Best Practices

### 1. Enable UFW Firewall

```bash
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 3000/tcp  # LMS (or your custom port)
sudo ufw enable
```

### 2. Use Nginx as Reverse Proxy (Optional but Recommended)

Install Nginx:

```bash
sudo apt install nginx
```

Create configuration:

```bash
sudo nano /etc/nginx/sites-available/ai-lms
```

Add this configuration:

```nginx
server {
    listen 80;
    server_name your-domain.com;  # or your server IP

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/ai-lms /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Update firewall:

```bash
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 3000/tcp  # No need to expose directly anymore
```

### 3. Add SSL with Let's Encrypt (Optional)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal is configured automatically
```

## 📊 Monitoring

### Check Disk Space

```bash
df -h
```

### Check Memory Usage

```bash
free -h
```

### Check Docker Container Stats

```bash
docker stats ai-builder-lms
```

## 🔄 Backup Your Progress

### Manual Backup

```bash
# Backup progress file
cp data/progress.json data/progress-backup-$(date +%Y%m%d).json

# Or create a complete backup
tar -czf lms-backup-$(date +%Y%m%d).tar.gz data/
```

### Automated Daily Backups

Create a backup script:

```bash
nano ~/backup-lms.sh
```

Add this content:

```bash
#!/bin/bash
BACKUP_DIR=~/lms-backups
mkdir -p $BACKUP_DIR
cd ~/ai-builder-lms
cp data/progress.json $BACKUP_DIR/progress-$(date +%Y%m%d-%H%M).json
# Keep only last 30 days
find $BACKUP_DIR -name "progress-*.json" -mtime +30 -delete
```

Make it executable:

```bash
chmod +x ~/backup-lms.sh
```

Add to crontab (daily at 2 AM):

```bash
crontab -e
```

Add this line:

```
0 2 * * * /home/your-user/backup-lms.sh
```

## 🆘 Troubleshooting

### Container won't start

```bash
# Check logs
docker-compose logs

# Check if port is in use
sudo lsof -i :3000

# Rebuild from scratch
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Can't access from browser

```bash
# Check if container is running
docker-compose ps

# Check firewall
sudo ufw status

# Test locally on server
curl http://localhost:3000
```

### Out of disk space

```bash
# Check space
df -h

# Clean up Docker
docker system prune -a
docker volume prune
```

## 🎉 Success!

Your AI Builder LMS is now running securely on your server. Start learning at:

- Without Nginx: `http://your-server-ip:3000`
- With Nginx: `http://your-domain.com`
- With SSL: `https://your-domain.com`

Happy learning! 🚀
