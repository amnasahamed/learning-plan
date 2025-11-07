#!/bin/bash

# AI Builder LMS - Docker Deployment Script
# This script automates the deployment process

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_step() {
    echo -e "${BLUE}==>${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}!${NC} $1"
}

# Check if Docker is installed
check_docker() {
    print_step "Checking Docker installation..."
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    print_success "Docker is installed ($(docker --version))"
}

# Check if Docker Compose is installed
check_docker_compose() {
    print_step "Checking Docker Compose installation..."
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi
    print_success "Docker Compose is installed ($(docker-compose --version))"
}

# Check if port 737 is available
check_port() {
    print_step "Checking if port 737 is available..."
    if lsof -Pi :737 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        print_warning "Port 737 is already in use!"
        echo "Do you want to continue anyway? (y/N)"
        read -r response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            print_error "Deployment cancelled."
            exit 1
        fi
    else
        print_success "Port 737 is available"
    fi
}

# Setup JWT secret
setup_jwt_secret() {
    print_step "Setting up JWT secret..."

    if [ -f .env ]; then
        print_success ".env file already exists"
        if grep -q "JWT_SECRET" .env; then
            print_success "JWT_SECRET is configured"
        else
            print_warning "JWT_SECRET not found in .env, adding default..."
            echo "JWT_SECRET=ai-builder-lms-secret-key-2024" >> .env
        fi
    else
        print_warning ".env file not found, creating with default secret..."
        echo "# JWT Secret for authentication" > .env
        echo "JWT_SECRET=ai-builder-lms-secret-key-2024" >> .env
        print_success "Created .env file with default JWT secret"
        print_warning "⚠️  For production, please change the JWT_SECRET in .env file!"
    fi
}

# Create data directory
setup_data_dir() {
    print_step "Setting up data directory..."
    mkdir -p data
    print_success "Data directory is ready"
}

# Stop existing containers
stop_existing() {
    print_step "Stopping existing containers..."
    if docker ps -a | grep -q ai-builder-lms; then
        docker-compose down
        print_success "Stopped existing containers"
    else
        print_success "No existing containers to stop"
    fi
}

# Build Docker image
build_image() {
    print_step "Building Docker image..."
    if [ "$1" == "--no-cache" ]; then
        print_warning "Building without cache (this may take longer)..."
        docker-compose build --no-cache
    else
        docker-compose build
    fi
    print_success "Docker image built successfully"
}

# Start containers
start_containers() {
    print_step "Starting containers..."
    docker-compose up -d
    print_success "Containers started"
}

# Wait for health check
wait_for_healthy() {
    print_step "Waiting for application to be healthy..."

    max_attempts=30
    attempt=0

    while [ $attempt -lt $max_attempts ]; do
        if docker inspect ai-builder-lms | grep -q '"Status": "healthy"'; then
            print_success "Application is healthy!"
            return 0
        fi

        if docker inspect ai-builder-lms | grep -q '"Status": "unhealthy"'; then
            print_error "Application is unhealthy!"
            print_error "Check logs with: docker-compose logs -f"
            return 1
        fi

        echo -n "."
        sleep 2
        attempt=$((attempt + 1))
    done

    echo ""
    print_warning "Health check timeout. Container may still be starting..."
    print_warning "Check status with: docker-compose ps"
}

# Show deployment info
show_info() {
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                                                       ║${NC}"
    echo -e "${GREEN}║  🎉 AI Builder LMS Deployed Successfully! 🎉         ║${NC}"
    echo -e "${GREEN}║                                                       ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "  ${BLUE}Access your LMS at:${NC} http://localhost:737"
    echo ""
    echo -e "  ${YELLOW}Useful Commands:${NC}"
    echo -e "    View logs:      ${GREEN}docker-compose logs -f${NC}"
    echo -e "    Stop:           ${GREEN}docker-compose stop${NC}"
    echo -e "    Restart:        ${GREEN}docker-compose restart${NC}"
    echo -e "    Check status:   ${GREEN}docker-compose ps${NC}"
    echo ""
    echo -e "  ${YELLOW}First Time Setup:${NC}"
    echo -e "    1. Open http://localhost:737"
    echo -e "    2. Click 'Get Started' or 'Sign Up'"
    echo -e "    3. Create your account"
    echo -e "    4. Start learning!"
    echo ""
    echo -e "  ${YELLOW}Sharing with Others:${NC}"
    echo -e "    Share the URL with friends/students"
    echo -e "    They can create their own accounts"
    echo ""
}

# Main deployment function
deploy() {
    echo ""
    echo -e "${BLUE}╔═══════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                                                       ║${NC}"
    echo -e "${BLUE}║       AI Builder LMS - Deployment Script             ║${NC}"
    echo -e "${BLUE}║                                                       ║${NC}"
    echo -e "${BLUE}╚═══════════════════════════════════════════════════════╝${NC}"
    echo ""

    # Pre-flight checks
    check_docker
    check_docker_compose
    check_port

    # Setup
    setup_jwt_secret
    setup_data_dir

    # Deploy
    stop_existing
    build_image "$1"
    start_containers

    # Verify
    sleep 5
    wait_for_healthy

    # Show info
    show_info
}

# Parse command line arguments
case "${1:-}" in
    --no-cache)
        deploy --no-cache
        ;;
    --help|-h)
        echo "Usage: $0 [OPTIONS]"
        echo ""
        echo "Options:"
        echo "  --no-cache    Build without using Docker cache"
        echo "  --help, -h    Show this help message"
        echo ""
        echo "Examples:"
        echo "  $0                 # Normal deployment"
        echo "  $0 --no-cache      # Fresh build without cache"
        ;;
    "")
        deploy
        ;;
    *)
        print_error "Unknown option: $1"
        echo "Use --help for usage information"
        exit 1
        ;;
esac
