# Jenkins JNLP Linux Remote Agent
# Task 2: Jenkins Remoting

FROM jenkins/inbound-agent:latest-jdk17

USER root

# Install build tools for distributed jobs
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    wget \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Allow jenkins user to use docker
RUN usermod -aG docker jenkins

USER jenkins

LABEL maintainer="Marwan Tamer" \
      task="Task2-Jenkins-Remoting" \
      agent-type="linux-jnlp"
