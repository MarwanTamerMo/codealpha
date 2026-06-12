# Task 4: Web Server using Docker
# CodeAlpha DevOps Internship
#
# Multi-stage build:
#   Stage 1 (builder) - install Python dependencies
#   Stage 2 (production) - minimal runtime image

# ── Stage 1: builder ─────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ── Stage 2: production ──────────────────────────────────────────────────────
FROM python:3.11-slim AS production

# Security: non-root user
RUN groupadd -r webuser && useradd -r -g webuser -d /app -s /sbin/nologin webuser

WORKDIR /app

# Copy deps from builder
COPY --from=builder /root/.local /home/webuser/.local

# Copy application
COPY app/ ./app/
COPY static/ ./static/

# Set ownership
RUN chown -R webuser:webuser /app

USER webuser

ENV PATH=/home/webuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

EXPOSE 8080

# Built-in health check (used by Docker and compose)
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD python -c \
  "import urllib.request; r=urllib.request.urlopen('http://localhost:8080/health'); exit(0 if r.status==200 else 1)"

CMD ["gunicorn", \
     "--bind", "0.0.0.0:8080", \
     "--workers", "2", \
     "--timeout", "60", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "app.server:app"]
