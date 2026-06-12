# Task 2: Jenkins Remoting Project

## Overview
This task sets up a **Jenkins Controller + Remote Agents** architecture using the Jenkins Remoting protocol (JNLP/WebSocket), distributing build loads across isolated Docker containers running on different architectures.

## Architecture
```
Jenkins Controller (port 8080/50000)
       ├── linux-agent   (JNLP – Python builds)
       └── docker-agent  (Docker-in-Docker – container builds)
              ├── python:3.10  (matrix test)
              ├── python:3.11  (matrix test)
              └── python:3.12  (matrix test)
```

## Components

| File | Purpose |
|------|---------|
| `Jenkinsfile` | 4-stage declarative pipeline with parallel agent dispatch |
| `docker-compose.yml` | Controller + 2 remote agents as containers |
| `docker/linux-agent/Dockerfile` | JNLP Linux agent image |
| `docker/docker-agent/Dockerfile` | Docker-in-Docker JNLP agent image |
| `app/calculator.py` | Sample app with 6 operations |
| `app/tests/test_calculator.py` | 17 pytest tests |
| `scripts/setup-agent.sh` | Script to register a bare-metal agent |

## Quick Start

```bash
# 1. Start the Jenkins stack
cd Task2-Jenkins-Remoting
docker-compose up -d

# 2. Get admin password
docker exec jenkins-controller cat /var/jenkins_home/secrets/initialAdminPassword

# 3. Open Jenkins UI
open http://localhost:8080

# 4. Create agent nodes in UI:
#    Manage Jenkins → Nodes → New Node
#    Name: linux-agent, Type: Permanent Agent, Launch: JNLP
#    Copy the agent secret and set it as LINUX_AGENT_SECRET env var

# 5. Restart agents with secret
LINUX_AGENT_SECRET=<secret> DOCKER_AGENT_SECRET=<secret> docker-compose up -d

# 6. Run tests locally
cd app && pip install -r requirements.txt
pytest tests/ -v
```

## Criteria Met
- ✅ Jenkins Remoting to connect remote nodes (JNLP/WebSocket)
- ✅ Build loads distributed across linux-agent and docker-agent
- ✅ Jobs run on various Python architectures (3.10, 3.11, 3.12) in parallel
- ✅ Security via node isolation (agents run in isolated containers)
- ✅ Hands-on Jenkins remote execution (stash/unstash, parallel stages)
