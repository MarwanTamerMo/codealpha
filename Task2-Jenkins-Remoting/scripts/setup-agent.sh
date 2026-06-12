#!/usr/bin/env bash
# setup-agent.sh – Configure a new Jenkins JNLP remote agent
# Usage: ./setup-agent.sh <JENKINS_URL> <AGENT_NAME> <AGENT_SECRET>
# Task 2: Jenkins Remoting Project

set -euo pipefail

JENKINS_URL="${1:-http://localhost:8080}"
AGENT_NAME="${2:-linux-agent}"
AGENT_SECRET="${3:?Agent secret is required as 3rd argument}"
WORK_DIR="/home/jenkins/agent"
AGENT_JAR="/usr/local/bin/agent.jar"

echo "========================================"
echo " Jenkins Remote Agent Setup"
echo "========================================"
echo "Controller URL : $JENKINS_URL"
echo "Agent Name     : $AGENT_NAME"
echo "Work Directory : $WORK_DIR"

# 1. Install Java if missing
if ! command -v java &>/dev/null; then
    echo "[1/4] Installing OpenJDK 17..."
    apt-get update -qq
    apt-get install -y --no-install-recommends openjdk-17-jre-headless
else
    echo "[1/4] Java found: $(java -version 2>&1 | head -1)"
fi

# 2. Download agent.jar from controller
echo "[2/4] Downloading agent.jar from Jenkins controller..."
curl -sSL "${JENKINS_URL}/jnlpJars/agent.jar" -o "$AGENT_JAR"
chmod +x "$AGENT_JAR"
echo "agent.jar downloaded successfully"

# 3. Create work directory
echo "[3/4] Preparing workspace at $WORK_DIR"
mkdir -p "$WORK_DIR"

# 4. Start agent via JNLP (Remoting protocol)
echo "[4/4] Connecting agent '$AGENT_NAME' to controller..."
exec java -jar "$AGENT_JAR" \
    -url "$JENKINS_URL" \
    -secret "$AGENT_SECRET" \
    -name "$AGENT_NAME" \
    -workDir "$WORK_DIR" \
    -webSocket
