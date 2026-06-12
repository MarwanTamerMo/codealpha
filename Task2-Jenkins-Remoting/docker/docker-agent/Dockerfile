# Jenkins Docker-capable Remote Agent
# Task 2: Jenkins Remoting

FROM jenkins/inbound-agent:latest-jdk17

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

RUN usermod -aG docker jenkins

USER jenkins

LABEL maintainer="Marwan Tamer" \
      task="Task2-Jenkins-Remoting" \
      agent-type="docker-jnlp"
