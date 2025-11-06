# 🚀 Deploy to Your Server - Complete Guide

This guide will help you deploy the AI Builder LMS to your own server in under 10 minutes.

## 📋 What You Need

- A server (VPS, cloud instance, or dedicated server)
- SSH access to your server
- Root or sudo privileges
- 1GB+ RAM recommended
- 10GB+ disk space

## 🎯 Step-by-Step Deployment

### Step 1: Connect to Your Server

```bash
ssh your-username@your-server-ip
```

### Step 2: Install Docker (if not already installed)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install docker-compose -y

# Verify installation
docker --version
docker-compose --version
```

**Important:** Log out and back in for the docker group changes to take effect:

```bash
exit
ssh your-username@your-server-ip
```

### Step 3: Clone Your Repository

```bash
# Navigate to where you want to install
cd ~

# Clone from GitHub (replace with your actual repo URL)
git clone https://github.com/amnasahamed/learning-plan.git
cd learning-plan/ai-builder-lms
```

### Step 4: Start the LMS

```bash
# Start the application
docker-compose up -d

# Check if it's running
docker-compose ps

# View logs (optional)
docker-compose logs -f
```

### Step 5: Configure Firewall

```bash
# Allow HTTP traffic on port 3000
sudo ufw allow 3000/tcp

# Enable firewall if not already enabled
sudo ufw enable

# Check status
sudo ufw status
```

### Step 6: Access Your LMS

Open your browser and visit:

```
http://your-server-ip:3000
```

## 🎉 Success!

Your AI Builder LMS is now running on your server!

---

## 🔒 Optional: Add Domain Name & SSL

### With Nginx Reverse Proxy

#### 1. Install Nginx

```bash
sudo apt install nginx -y
```

#### 2. Create Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/ai-lms
```

Paste this configuration (replace `yourdomain.com` with your actual domain):

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

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

#### 3. Enable the Site

```bash
# Create symbolic link
sudo ln -s /etc/nginx/sites-available/ai-lms /etc/nginx/sites-enabled/

# Remove default site (optional)
sudo rm /etc/nginx/sites-enabled/default

# Test configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

#### 4. Update Firewall

```bash
# Allow Nginx
sudo ufw allow 'Nginx Full'

# Remove direct access to port 3000 (optional, for security)
sudo ufw delete allow 3000/tcp

# Check status
sudo ufw status
```

Now your LMS is accessible at: `http://yourdomain.com`

### Add SSL Certificate (HTTPS)

#### 1. Install Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
```

#### 2. Get SSL Certificate

```bash
# Replace with your actual domain
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Follow the prompts:
- Enter your email
- Agree to terms
- Choose whether to redirect HTTP to HTTPS (recommended: Yes)

#### 3. Verify Auto-Renewal

```bash
# Test renewal
sudo certbot renew --dry-run
```

Certbot automatically sets up a cron job for renewal.

Now your LMS is accessible at: `https://yourdomain.com` 🎉

---

## 🔄 Updating the LMS

When you want to update the LMS with new content or features:

```bash
# Navigate to the directory
cd ~/learning-plan/ai-builder-lms

# Pull latest changes
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose up -d --build
```

---

## 📊 Monitoring & Maintenance

### Check Application Status

```bash
# View running containers
docker-compose ps

# View logs
docker-compose logs -f

# Check resource usage
docker stats ai-builder-lms
```

### Backup Your Progress

```bash
# Create a backup directory
mkdir -p ~/lms-backups

# Backup progress data
cp ~/learning-plan/ai-builder-lms/data/progress.json \
   ~/lms-backups/progress-$(date +%Y%m%d-%H%M).json
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
cp ~/learning-plan/ai-builder-lms/data/progress.json \
   $BACKUP_DIR/progress-$(date +%Y%m%d-%H%M).json
# Keep only last 30 backups
ls -t $BACKUP_DIR/progress-*.json | tail -n +31 | xargs -r rm
```

Make it executable and add to cron:

```bash
# Make executable
chmod +x ~/backup-lms.sh

# Add to crontab (runs daily at 3 AM)
(crontab -l 2>/dev/null; echo "0 3 * * * ~/backup-lms.sh") | crontab -
```

---

## 🆘 Troubleshooting

### LMS won't start

```bash
# Check logs for errors
docker-compose logs

# Check if port 3000 is already in use
sudo lsof -i :3000

# Restart Docker
sudo systemctl restart docker
docker-compose up -d
```

### Can't access from browser

1. **Check if container is running:**
   ```bash
   docker-compose ps
   ```

2. **Check firewall:**
   ```bash
   sudo ufw status
   ```

3. **Test locally on server:**
   ```bash
   curl http://localhost:3000
   ```

4. **Check your server's external IP:**
   ```bash
   curl ifconfig.me
   ```

### Docker Compose command not found

```bash
# Try with hyphen
docker-compose --version

# Or install docker-compose plugin
sudo apt install docker-compose-plugin
docker compose --version
```

### Permission denied errors

```bash
# Ensure your user is in docker group
groups

# If docker group is missing, add it
sudo usermod -aG docker $USER

# Log out and back in
exit
```

### Out of disk space

```bash
# Check disk space
df -h

# Clean up Docker
docker system prune -a -f
docker volume prune -f
```

---

## 🎯 Quick Command Reference

```bash
# Start LMS
docker-compose up -d

# Stop LMS
docker-compose down

# Restart LMS
docker-compose restart

# View logs
docker-compose logs -f

# Update LMS
git pull && docker-compose up -d --build

# Backup progress
cp data/progress.json data/progress-backup.json

# Check status
docker-compose ps
docker stats ai-builder-lms
```

---

## 💡 Pro Tips

1. **Use a domain name** - Easier to remember than IP addresses
2. **Enable SSL** - Secure your connection with HTTPS
3. **Set up backups** - Automate with cron jobs
4. **Monitor resources** - Use `docker stats` regularly
5. **Keep it updated** - Pull changes regularly

---

## 📞 Support

If you encounter issues:

1. Check the logs: `docker-compose logs`
2. Verify Docker is running: `docker ps`
3. Check firewall rules: `sudo ufw status`
4. Ensure port 3000 is accessible
5. Review the troubleshooting section above

---

## 🎓 You're All Set!

Your AI Builder LMS is now:
- ✅ Running on your server
- ✅ Accessible via browser
- ✅ Saving progress automatically
- ✅ Ready for daily learning

**Start your 30-day journey to becoming an AI Systems Builder!** 🚀

Access your LMS at:
- Direct: `http://your-server-ip:3000`
- With domain: `http://yourdomain.com`
- With SSL: `https://yourdomain.com`
