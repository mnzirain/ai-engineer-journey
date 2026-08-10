# Week 20 — Enterprise AI Gateway

> **A production-inspired, cloud-native AI gateway for governed multi-provider LLM access**

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API%20Platform-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Cloud--Native-326CE5?logo=kubernetes)](https://kubernetes.io/)
[![Pytest](https://img.shields.io/badge/Pytest-Tested-0A9EDC?logo=pytest)](https://pytest.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github)](https://github.com/)

---

# 1. Project Overview

Week 20 represents a major transition in the **AI Engineer Journey** from building individual AI applications toward designing the infrastructure layer through which enterprise AI applications can access multiple AI providers through a governed interface.

The project implements an **Enterprise AI Gateway** that provides a unified interface between client applications and multiple AI providers.

Instead of allowing every application to implement its own authentication, rate limiting, provider selection, monitoring, and response handling, the gateway centralizes these responsibilities behind one controlled platform boundary.

The result is a production-inspired architecture for:

- Secure AI access
- Multi-provider routing
- Authentication
- Authorization
- API-key validation
- Rate limiting
- Request logging
- Monitoring
- Provider abstraction
- Model discovery
- Standardized API responses
- Docker deployment
- Kubernetes workload deployment

This project is intentionally designed as an infrastructure-oriented AI system rather than a standalone chatbot.

---

# 2. Engineering Objective

The primary objective was to demonstrate the ability to move an AI service through multiple engineering layers:

```text
AI Application
      ↓
LLM Integration
      ↓
Provider Abstraction
      ↓
Secure AI Gateway
      ↓
Containerized Service
      ↓
Kubernetes Workload
      ↓
Cloud-Native Deployment Foundation

---

The project therefore focuses on the engineering surrounding AI models rather than only the model call itself.

The gateway establishes a reusable infrastructure boundary that can support future AI applications and services.

3. Architecture

The gateway follows a layered request-processing architecture:

                    ┌──────────────────────┐
                    │       Client         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Authentication       │
                    │ Middleware           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Rate Limiter         │
                    │ Middleware           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Gateway Engine       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Model / Request      │
                    │ Router               │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │   OpenAI   │   │ Hugging    │   │   Local    │
       │  Provider  │   │   Face     │   │    AI      │
       └────────────┘   └────────────┘   └────────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Unified Response     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Client         │
                    └──────────────────────┘

---

Detailed architecture documentation is available in:

docs/architecture.md

Architecture source:

docs/architecture.drawio

Architecture visual:

docs/architecture.png

4. Core Engineering Capabilities
AI Provider Abstraction

The gateway separates client applications from individual AI providers.

Current provider implementations include:

OpenAI
Hugging Face
Local AI

Provider-specific implementations are isolated inside:

providers/

This allows additional providers to be introduced without requiring client applications to change their integration pattern.

Potential future integrations include:

Azure OpenAI
Anthropic
Google Gemini
AWS Bedrock
Mistral
DeepSeek

These are architectural extension points rather than claims of current implementation.

5. Gateway Components

The gateway is organized into modular engineering components.

Gateway Engine
gateway/gateway_engine.py

Coordinates gateway-level processing.

Request Router
gateway/request_router.py

Responsible for routing incoming AI requests.

Model Selector
gateway/model_selector.py

Provides the model-selection layer between incoming requests and provider implementations.

Response Formatter
gateway/response_formatter.py

Provides a standardized response boundary independent of the underlying provider.

6. Security Layer

The gateway implements security controls at the API boundary.

Current capabilities include:

API-key authentication
Authentication middleware
Request validation
Authorization handling
Rate limiting
Kubernetes Secret integration
Configuration isolation

Security-related middleware includes:

middleware/authentication.py
middleware/rate_limiter.py

Sensitive provider credentials are represented through a Kubernetes Secret configuration.

The repository contains only a placeholder value:

OPENAI_API_KEY: "replace-with-your-key"

No real API credential is stored in the repository.

Kubernetes secret configuration:

k8s/secret.yaml

This is intentionally a non-production placeholder and must be replaced through an appropriate secret-management mechanism before a real deployment.

7. Observability & Operations

The gateway includes operational middleware for:

Request logging
Monitoring
Metrics
Rate-limit visibility

Relevant components include:

middleware/logging.py
middleware/monitoring.py
middleware/rate_limiter.py

The API also exposes:

GET /metrics

This establishes the foundation for future observability improvements such as:

Prometheus metrics
Grafana dashboards
Distributed tracing
Centralized log aggregation
Alerting
SLO/SLI monitoring

8. REST API

The gateway exposes a unified REST interface.

| Method | Endpoint     | Purpose             |
| ------ | ------------ | ------------------- |
| GET    | `/`          | Gateway information |
| GET    | `/health`    | Health status       |
| GET    | `/providers` | Provider discovery  |
| GET    | `/models`    | Model discovery     |
| POST   | `/generate`  | AI generation       |
| GET    | `/metrics`   | Operational metrics |

The API is exposed through FastAPI and can be inspected through the generated OpenAPI/Swagger interface.

9. Docker Deployment

The application is containerized using Docker.

Repository components:

Dockerfile
docker-compose.yml

Docker provides a consistent runtime environment for the gateway and establishes the foundation for deployment into container orchestration platforms.

The project is therefore structured to move from:

Local Development
       ↓
Docker Container
       ↓
Docker Compose
       ↓
Kubernetes
       ↓
Cloud-Native Infrastructure

Local Development
       ↓
Docker Container
       ↓
Docker Compose
       ↓
Kubernetes
       ↓
Cloud-Native Infrastructure

10. Kubernetes Deployment

A major objective of Week 20 was to move beyond containerization and verify the gateway as a Kubernetes workload.

The application was deployed and verified on a local Kubernetes cluster running through Docker Desktop.

This is an important distinction:

The Kubernetes deployment demonstrated in this repository is a verified local cloud-native deployment foundation, not a claim of production cloud deployment.

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

Kubernetes Resources

The Week 20 Kubernetes configuration includes:

k8s/
├── namespace.yaml
├── deployment.yaml
├── service.yaml
├── configmap.yaml
└── secret.yaml

The deployment uses:

Kubernetes Namespace
Deployment
Service
NodePort
ConfigMap
Secret
Readiness probe
Liveness probe

Configured application flow:

Application Port
8000

        ↓

Kubernetes Service
80

        ↓

NodePort
31142

11. Kubernetes Verification

The workload was verified using Kubernetes resource inspection:

kubectl get deployment,pods,service -n enterprise-ai

The gateway workload reached:

1/1 Running

The application health endpoint was also repeatedly verified through Kubernetes networking.

Examples:

curl http://localhost:31142/health
curl http://localhost:31142/
curl http://localhost:31142/providers
curl http://localhost:31142/models

The /health endpoint returned:

HTTP 200 OK

The NodePort service was therefore verified as a working path from the local host into the Kubernetes-deployed gateway.

12. Kubernetes Health Checks

The Kubernetes Deployment includes HTTP-based readiness and liveness probes.

These probes establish the foundation for Kubernetes to determine whether the application:

Is alive
Is ready to receive traffic
Should remain in service
Requires recovery

This is a significant step beyond simply running a Docker container because the workload is now being managed through an orchestration layer.

13. Infrastructure Evidence

The repository includes visual evidence from the verified Kubernetes deployment.

Kubernetes Cluster Status

docs/screenshots/kubernetes-cluster-status.png

Kubernetes NodePort Health Check
docs/screenshots/kubernetes-nodeport-health-check.png

Additional deployment evidence includes:

docs/screenshots/kubernetes-deployment-running.png
docs/screenshots/kubernetes-gateway-api-tests.png
docs/screenshots/kubernetes-infrastructure-overview.png

Additional API and security evidence is available in:

docs/screenshots/
14. Testing

The project contains a dedicated test suite:

tests/
├── conftest.py
└── test_gateway.py

The test suite is designed around gateway behavior including:

Gateway functionality
Request handling
Provider routing
Authentication behavior
Rate limiting
API responses

The repository therefore treats testing as part of the engineering lifecycle rather than as an afterthought.

15. Project Structure

week20-enterprise-ai-gateway/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements_dev.txt
│
├── gateway/
│   ├── gateway_engine.py
│   ├── model_selector.py
│   ├── request_router.py
│   └── response_formatter.py
│
├── middleware/
│   ├── authentication.py
│   ├── logging.py
│   ├── monitoring.py
│   └── rate_limiter.py
│
├── models/
│   └── gateway_models.py
│
├── providers/
│   ├── openai_provider.py
│   ├── huggingface_provider.py
│   └── local_provider.py
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── secret.yaml
│
├── tests/
│   ├── conftest.py
│   └── test_gateway.py
│
├── docs/
│   ├── architecture.md
│   ├── architecture.drawio
│   ├── architecture.png
│   └── screenshots/
│
└── README.md

16. Evidence-Driven Engineering

A central principle of this portfolio is:

Do not claim capabilities that cannot be demonstrated.

Week 20 therefore distinguishes between:

Verified
FastAPI gateway
Multi-provider architecture
Authentication middleware
Rate limiting
Monitoring middleware
Logging
Docker containerization
Kubernetes deployment
Kubernetes Service
NodePort exposure
ConfigMap
Kubernetes Secret configuration
Readiness probes
Liveness probes
API endpoints
Architecture documentation
Automated tests
Deployment evidence screenshots
Future Engineering Extensions
Horizontal Pod Autoscaling
Ingress
Production cloud deployment
Prometheus/Grafana observability
Distributed tracing
Advanced secret management
Multi-region deployment
Resource quotas
GPU scheduling
Service mesh
High-availability architecture

This distinction is intentional.

The objective is to demonstrate engineering maturity by clearly separating implemented capabilities, verified capabilities, and future architecture.

17. Relationship to the AI Engineer Journey

Week 20 builds directly on the capabilities developed throughout the preceding projects.

The progression includes:

Week 13
Enterprise RAG / Knowledge Systems
        ↓
Week 14
Enterprise AI Gateway
        ↓
Week 15
AI Orchestration
        ↓
Week 16
Enterprise Tool Calling
        ↓
Week 17
Model Context Protocol
        ↓
Week 18
Enterprise Authentication
        ↓
Week 19
Enterprise Identity & Access Management
        ↓
Week 20
Enterprise AI Gateway + Kubernetes

Week 20 therefore acts as an infrastructure-oriented integration milestone.

The gateway provides a platform boundary through which future AI applications can consume models through a consistent and governed interface.

18. Relationship to Future AI Applications

The architecture developed in Week 20 is designed as a reusable infrastructure foundation for future domain-specific AI applications.

Future AI services can be positioned behind a centralized gateway rather than integrating independently with multiple AI providers.

The gateway architecture provides a foundation for:

Provider independence
Centralized authentication
Consistent AI access
Rate limiting
Monitoring
Standardized interfaces
Cloud-native deployment

Domain-specific product workflows and commercial business logic are intentionally outside the scope of this portfolio implementation.
19. Engineering Skills Demonstrated
AI Engineering
Large Language Model integration
Multi-provider AI architecture
Provider abstraction
AI request routing
Model selection
Standardized AI responses
Backend Engineering
Python
FastAPI
REST APIs
Pydantic
Modular service architecture
Middleware design
API validation
Security Engineering
API-key authentication
Authentication middleware
Authorization
Rate limiting
Kubernetes Secrets
Secure configuration boundaries
Infrastructure Engineering
Docker
Docker Compose
Kubernetes
Kubernetes Deployments
Kubernetes Services
NodePort networking
ConfigMaps
Secrets
Readiness probes
Liveness probes
Reliability & Operations
Health endpoints
Monitoring middleware
Metrics
Logging
Automated tests
Deployment verification
Architecture documentation
20. What This Milestone Demonstrates

Week 20 demonstrates a progression from:

Building an AI application

to:

Building infrastructure through which AI applications operate.

The gateway introduces several principles that are fundamental to larger enterprise AI platforms:

Centralized AI access
Provider abstraction
Security boundaries
Middleware-based controls
Operational visibility
Containerization
Workload orchestration
Health management
Deployment verification

The Kubernetes deployment is particularly important because it demonstrates that the gateway is not limited to a local Python process or standalone Docker container.

It can be packaged and operated as an orchestrated workload.

21. Next Engineering Evolution

The next stage of development can extend the verified Kubernetes foundation toward:

Local Kubernetes
      ↓
Production Observability
      ↓
CI/CD
      ↓
Cloud Deployment
      ↓
Autoscaling
      ↓
High Availability
      ↓
Advanced Security
      ↓
Multi-Region AI Infrastructure

These capabilities will be developed incrementally as part of the continuing AI Engineer Journey.

22. Portfolio Position

Week 20 is one of the flagship infrastructure projects in this portfolio.

It demonstrates the ability to combine:

LLMs
+
Backend APIs
+
Security
+
AI Provider Abstraction
+
Gateway Architecture
+
Docker
+
Kubernetes
+
Testing
+
Operational Evidence

into one coherent AI infrastructure system.

This project is not presented as a substitute for production enterprise experience.

Instead, it demonstrates the practical engineering foundation being developed toward professional LLM Engineering, AI Platform Engineering, MLOps, and AI Infrastructure Engineering roles.

Author

Mike Nzirainengwe

AI Engineer | LLM Engineer | AI Platform Engineering

Building resilient, scalable, production-inspired AI systems and infrastructure.

Long-Term Mission

Build world-class AI infrastructure and intelligent platforms that create practical impact across Africa and beyond.

Long-Term Engineering Mission: Enterprise AI Infrastructure and AI Platform Architecture

© 2026 Mike Nzirainengwe