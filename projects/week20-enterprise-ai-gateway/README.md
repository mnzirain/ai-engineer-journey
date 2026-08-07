# Week 20 – Enterprise AI Gateway

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Enterprise AI](https://img.shields.io/badge/Enterprise-AI-purple)
![Gateway](https://img.shields.io/badge/AI-Gateway-orange)
![Docker Ready](https://img.shields.io/badge/Docker-Ready-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)

---

# Enterprise AI Gateway

## Portfolio Project

This project demonstrates the design and implementation of an **Enterprise AI Gateway** capable of securely routing requests to multiple AI providers through a unified, production-inspired interface.

Rather than allowing applications to communicate directly with different AI providers, the gateway centralizes authentication, authorization, rate limiting, monitoring, provider routing, and standardized responses.

The architecture mirrors modern enterprise AI gateway patterns used in cloud-native AI platforms.

---

# Why this project matters

Enterprise AI systems require far more than calling an LLM API.

Organizations need:

- Centralized AI access
- Authentication
- Authorization
- API Gateway
- Rate Limiting
- Monitoring
- Provider abstraction
- Secure request routing
- Standardized responses

This project demonstrates those principles through a simplified enterprise architecture.

---

# Enterprise Features

- Enterprise AI Gateway
- Multi-Provider Routing
- Authentication Middleware
- Authorization Middleware
- API Key Security
- Request Validation
- Intelligent Request Router
- Rate Limiting
- Metrics Endpoint
- Enterprise Logging
- Unified AI Responses
- Docker-ready Deployment

---

# Enterprise Architecture

![Enterprise AI Gateway Architecture](docs/architecture.png)

The gateway centralizes AI access through a secure middleware pipeline before routing requests to the appropriate provider.

For full documentation see:

```
docs/architecture.md
```

---

# Gateway Workflow

```
Client

↓

Authentication

↓

Authorization

↓

Rate Limiter

↓

Gateway Engine

↓

Intelligent Router

↓

AI Provider

↓

Unified Response

↓

Client
```

---

# REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Platform information |
| GET | /health | Health monitoring |
| GET | /providers | Available AI providers |
| GET | /models | Available models |
| POST | /generate | AI generation endpoint |
| GET | /metrics | Platform metrics |

---

# Enterprise Security

The gateway currently demonstrates:

- API-key authentication
- Authentication middleware
- Authorization middleware
- Request validation
- Rate limiting
- Secure routing

Future enterprise enhancements include:

- OAuth2
- JWT
- RBAC
- Identity Federation
- Audit Logging

---

# Multi-Provider Architecture

The gateway currently supports:

- OpenAI
- Hugging Face
- Local AI

The provider abstraction layer allows additional providers to be added without changing client applications.

Potential future providers:

- Azure OpenAI
- Anthropic Claude
- Google Gemini
- AWS Bedrock
- Mistral
- DeepSeek

---

# Testing

Enterprise validation includes:

- API Health
- Provider Discovery
- Model Discovery
- Request Routing
- Authentication
- Metrics

```
python -m pytest -v

6 passed
```

---

# Project Structure

```
week20-enterprise-ai-gateway/

app.py

Dockerfile

docker-compose.yml

requirements.txt

requirements_dev.txt

auth/

core/

gateway/

middleware/

models/

security/

tests/

docs/

README.md
```

---

# Screenshots

```
docs/screenshots/

01-swagger-home.png
02-health-endpoint.png
03-providers-endpoint.png
04-models-endpoint.png
05-authenticated-request.png
06-invalid-api-key.png
07-rate-limit-demo.png
08-metrics-endpoint.png
09-terminal-logging.png
10-authorize-button.png
11-tests-passing.png
12-architecture.png
```

---

# Docker Deployment

The project includes:

- Dockerfile
- docker-compose.yml

Deployment targets include:

- Docker
- Kubernetes
- Azure Container Apps
- AWS ECS
- Google Cloud Run

---

# Skills Demonstrated

### Enterprise AI Engineering

- AI Gateway Design
- Provider Abstraction
- Enterprise Middleware
- AI Routing
- Enterprise Security

### Backend Engineering

- FastAPI
- REST APIs
- Dependency Injection
- Modular Architecture
- Service Layers

### Security Engineering

- Authentication
- Authorization
- API Keys
- Rate Limiting

### DevOps

- Docker
- Containerization
- Deployment Readiness
- Automated Testing

---

# Real-World Applications

The architecture demonstrated here can evolve into:

- Enterprise AI Platforms
- AI Agent Platforms
- LLM Infrastructure
- Multi-Agent Systems
- Healthcare AI Platforms
- Secure Enterprise APIs
- MedNavi AI

---

# Relationship to MedNavi AI

The Enterprise AI Gateway forms the communication backbone for MedNavi AI.

Future MedNavi services—including multilingual transcription, SOAP generation, Retrieval-Augmented Generation (RAG), intelligent triage, appointment scheduling, pharmacy integration, and clinical AI assistants—can all communicate securely through this gateway.

By separating infrastructure from application logic, MedNavi AI gains:

- Scalability
- Provider independence
- Stronger security
- Easier maintenance
- Cloud-native deployment readiness

---

# Author

**Mike Nzirainengwe**

Enterprise AI Infrastructure Engineer  
LLM Engineer  
AI Platform Architect

Building Secure, Scalable & Production-Ready Enterprise AI Systems

**Long-Term Vision**

**MedNavi AI — Intelligent Healthcare Platform for Southern Africa**

---

# AI Engineer Journey

Week 20 concludes the structured AI Engineering Portfolio Journey.

Enterprise projects completed include:

- Week 17 – Enterprise MCP Server
- Week 18 – Enterprise Authentication Platform
- Week 19 – Enterprise Identity & Access Management Platform
- Week 20 – Enterprise AI Gateway

This portfolio demonstrates practical implementation of enterprise AI architecture, secure backend engineering, cloud-ready deployment, and production-inspired AI infrastructure.

---

© 2026 Mike Nzirainengwe
---

# ☸️ Kubernetes Deployment

Week 20 is deployed and verified on a local Kubernetes cluster running through Docker Desktop.

## Deployment Architecture

```text
Client
  │
  ▼
NodePort :31142
  │
  ▼
enterprise-ai-service :80
  │
  ▼
Enterprise AI Gateway Pod :8000
  │
  ▼
FastAPI /health
```

## Kubernetes Resources

- Namespace: `enterprise-ai`
- Deployment: `enterprise-ai-gateway`
- Service: `enterprise-ai-service`
- Service type: `NodePort`
- Application port: `8000`
- Kubernetes service port: `80`
- Local NodePort: `31142`
- Configuration: ConfigMap
- Secrets: Kubernetes Secret
- Health checks: HTTP readiness and liveness probes

## Deployment Verification

The workload was successfully verified with:

```bash
kubectl get deployment,pods,service -n enterprise-ai
```

The Gateway reached `1/1 Running` and Kubernetes successfully executed repeated HTTP health checks against `/health`, receiving HTTP `200 OK` responses.

The Kubernetes Service was also verified through the NodePort:

```bash
curl http://localhost:31142/health
curl http://localhost:31142/
curl http://localhost:31142/providers
curl http://localhost:31142/models
```

Verified API capabilities include:

- Health monitoring
- Gateway service status
- Multi-provider registry
- Model registry

## Infrastructure Evidence

![Kubernetes Deployment](screenshots/kubernetes-deployment-running.png)

![Kubernetes Infrastructure Overview](screenshots/kubernetes-infrastructure-overview.png)

![Kubernetes Gateway API Tests](screenshots/kubernetes-gateway-api-tests.png)

## Engineering Significance

This milestone demonstrates the transition from containerized AI application development to cloud-native workload deployment. The Gateway is packaged as a Docker image, deployed as a Kubernetes workload, exposed through a Kubernetes Service, and monitored through readiness and liveness probes.

The deployment provides a foundation for future work involving horizontal scaling, ingress, observability, secrets management, resource limits, autoscaling, and production cloud deployment.
