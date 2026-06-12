# Task 1: CI/CD Pipeline using Azure

## Overview
This task implements a full **CI/CD pipeline** using **Azure Pipelines**, **Azure Container Registry (ACR)**, and **Azure App Service** with blue/green (slot swap) deployment strategy.

## Architecture
```
Git Push → Azure Pipelines → Build & Test → Docker Build → ACR Push → Deploy to Staging → Smoke Tests → Swap to Production
```

## Components

| Component | Purpose |
|-----------|----------|
| `azure-pipelines.yml` | Full 4-stage CI/CD pipeline definition |
| `app/app.py` | Flask web application with `/`, `/health`, `/info` endpoints |
| `app/Dockerfile` | Multi-stage Docker build (builder + production) |
| `app/requirements.txt` | Python dependencies |
| `app/tests/test_app.py` | Pytest unit tests (12 tests) |
| `infrastructure/main.tf` | Terraform to provision ACR + App Service |

## Pipeline Stages

1. **Build & Test** – Install deps, run pytest with coverage, publish results
2. **Docker Build & Push** – Multi-stage build, Trivy security scan, push to ACR
3. **Deploy to Staging** – Container deploy + smoke tests (5 retries on `/health`)
4. **Deploy to Production** – Slot swap (zero-downtime) + health check

## Running Locally

```bash
# Run Flask app
cd Task1-CICD-Azure/app
pip install -r requirements.txt
python app.py

# Run tests
pip install pytest pytest-cov
pytest tests/ -v

# Build Docker image
docker build -t codealpha-webapp .
docker run -p 8000:8000 codealpha-webapp
curl http://localhost:8000/health

# Provision infrastructure
cd infrastructure
terraform init
terraform plan
terraform apply
```

## Criteria Met
- ✅ Automated CI/CD pipeline with Azure Pipelines
- ✅ Azure Container Registry for container storage
- ✅ Deploy via Azure App Service automatically (staging slot → production swap)
- ✅ Pipeline monitoring (test results, coverage, health checks published)
- ✅ Key DevOps concepts: IaC (Terraform), containerization, security scanning
