#!/usr/bin/env bash
# manage.sh – Docker lifecycle management for Task 4
# Usage: ./scripts/manage.sh [build|up|down|logs|health|shell|clean]

set -euo pipefail

COMPOSE_FILE="$(dirname "$0")/../docker-compose.yml"
CONTAINER="codealpha-webapp"

cmd="${1:-help}"

case "$cmd" in
  build)
    echo "🔨  Building Docker image..."
    docker compose -f "$COMPOSE_FILE" build --no-cache
    echo "✅ Build complete"
    ;;

  up)
    echo "🚀  Starting containers..."
    docker compose -f "$COMPOSE_FILE" up -d
    echo "✅ Stack is up. Access at http://localhost"
    ;;

  down)
    echo "🛑  Stopping containers..."
    docker compose -f "$COMPOSE_FILE" down
    echo "✅ Stack stopped"
    ;;

  logs)
    docker compose -f "$COMPOSE_FILE" logs -f
    ;;

  health)
    echo "💚  Container health status:"
    docker inspect --format='{{.Name}}: {{.State.Health.Status}}' \
      codealpha-webapp codealpha-nginx 2>/dev/null || echo "Containers not running"
    ;;

  shell)
    echo "💻  Opening shell in webapp container..."
    docker exec -it "$CONTAINER" /bin/sh
    ;;

  test)
    echo "🧪  Running tests..."
    cd "$(dirname "$0")/.."
    pip install -q flask pytest
    pytest tests/ -v
    ;;

  clean)
    echo "🧹  Removing containers, images, and volumes..."
    docker compose -f "$COMPOSE_FILE" down -v --rmi local
    docker system prune -f
    echo "✅ Cleanup complete"
    ;;

  help|*)
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  build   Build Docker images"
    echo "  up      Start the stack"
    echo "  down    Stop the stack"
    echo "  logs    Follow container logs"
    echo "  health  Check container health"
    echo "  shell   Open shell in webapp container"
    echo "  test    Run pytest locally"
    echo "  clean   Remove everything (containers, images, volumes)"
    ;;
esac
