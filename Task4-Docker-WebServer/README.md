# Task 4: Web Server using Docker

## Overview
A **Python Flask** web server fully containerized with **Docker** (multi-stage build) and fronted by an **Nginx** reverse proxy. Demonstrates the complete Docker container lifecycle: build, run, health monitoring, troubleshooting, and best practices.

## Architecture
```
Browser :80
    ↓
Nginx (reverse proxy, rate limiting, security headers)
    ↓
Flask app (gunicorn, 2 workers) :8080 [internal]
    [running as non-root in isolated container]
```

## Components

| File | Purpose |
|------|----------|
| `Dockerfile` | Multi-stage build (builder + production), non-root user |
| `docker-compose.yml` | Webapp + Nginx with health checks |
| `nginx/nginx.conf` | Reverse proxy, rate limiting, security headers |
| `app/server.py` | Flask app with `/`, `/health`, `/api/info`, `/api/stats` |
| `tests/test_server.py` | 14 pytest tests |
| `scripts/manage.sh` | Lifecycle manager (build/up/down/logs/health/shell/clean) |

## Quick Start

```bash
cd Task4-Docker-WebServer

# 1. Build and start
./scripts/manage.sh build
./scripts/manage.sh up

# 2. Access the web server
curl http://localhost          # HTML landing page
curl http://localhost/health   # JSON health check
curl http://localhost/api/info # JSON app info
curl http://localhost/api/stats # JSON runtime stats

# 3. Monitor containers
./scripts/manage.sh health
./scripts/manage.sh logs

# 4. Open shell in container (troubleshooting)
./scripts/manage.sh shell

# 5. Run tests locally
./scripts/manage.sh test

# 6. Clean up everything
./scripts/manage.sh clean
```

## Container Lifecycle Commands

```bash
# Build image manually
docker build -t codealpha-webserver .

# Run standalone container
docker run -d -p 8080:8080 \
  -e ENVIRONMENT=production \
  --name webapp \
  --restart unless-stopped \
  codealpha-webserver

# Inspect health
docker inspect --format='{{.State.Health.Status}}' webapp

# View resource usage
docker stats webapp

# Exec into container
docker exec -it webapp /bin/sh

# View logs
docker logs -f webapp

# Stop and remove
docker stop webapp && docker rm webapp
```

## Criteria Met
- ✅ Docker containerization basics (multi-stage, non-root, HEALTHCHECK)
- ✅ Web server deployed and managed inside Docker (Flask + Nginx + Gunicorn)
- ✅ Container lifecycle: build → run → monitor → troubleshoot (`manage.sh`)
- ✅ Health monitoring (Docker HEALTHCHECK + `/health` endpoint + compose healthcheck)
- ✅ Best practices: reverse proxy, rate limiting, security headers, minimal image
