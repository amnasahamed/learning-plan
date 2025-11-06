# 🎯 Quick Setup Guide - Port 737

Your AI Builder LMS is configured to run on **port 737**.

## 🚀 One-Command Deployment

```bash
cd ai-builder-lms
docker-compose up -d
```

## 🌐 Access Your LMS

```
http://localhost:737          # Local access
http://your-server-ip:737     # Remote access
```

## 🔥 Firewall Configuration

If you're deploying on a server, open port 737:

```bash
# Allow port 737
sudo ufw allow 737/tcp

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status
```

## 🔧 Management Commands

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Restart
docker-compose restart

# View logs
docker-compose logs -f

# Check status
docker-compose ps
```

## 📝 Nginx Reverse Proxy (Optional)

If you want to use a domain name:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

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

Save to `/etc/nginx/sites-available/ai-lms` and enable:

```bash
sudo ln -s /etc/nginx/sites-available/ai-lms /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 Add SSL (HTTPS)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

## ✅ Verification Checklist

- [ ] Docker is installed
- [ ] Port 737 is open in firewall
- [ ] Application is running: `docker-compose ps`
- [ ] Can access at `http://your-ip:737`
- [ ] Progress is being saved in `data/progress.json`

## 🆘 Troubleshooting

### Can't access on port 737

```bash
# Check if container is running
docker-compose ps

# Check if port is listening
sudo netstat -tlnp | grep 737

# Check firewall
sudo ufw status | grep 737

# View logs for errors
docker-compose logs
```

### Port 737 already in use

```bash
# Check what's using the port
sudo lsof -i :737

# Or choose a different port by editing docker-compose.yml
# Change "737:3000" to "8080:3000" (or any port you prefer)
```

## 🎉 That's It!

Your AI Builder LMS is running on port 737.

**Start learning**: `http://your-server-ip:737`
