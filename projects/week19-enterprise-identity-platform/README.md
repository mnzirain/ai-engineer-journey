# Week 19 – Enterprise Identity & Access Management Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![OAuth2](https://img.shields.io/badge/OAuth2-Enterprise-orange)
![JWT](https://img.shields.io/badge/JWT-Authentication-red)
![Enterprise AI](https://img.shields.io/badge/Enterprise-AI-purple)
![Docker Ready](https://img.shields.io/badge/Docker-Ready-blue)

---

# Enterprise Identity & Access Management Platform

## Portfolio Project

This project demonstrates the design and implementation of an Enterprise Identity & Access Management (IAM) Platform for modern AI applications.

The platform implements enterprise-grade authentication, authorization, session lifecycle management, JWT security, OAuth authentication flow, refresh token management, middleware security, and protected AI services.

The architecture follows modern cloud-native identity patterns used across enterprise AI systems and production platforms.

---

# Why this project matters

Enterprise AI systems cannot rely on simple username/password authentication.

Modern AI platforms require:

- Identity Providers
- OAuth2
- JWT Authentication
- Session Management
- Role-Based Access Control (RBAC)
- Refresh Token Rotation
- Protected Enterprise APIs

This project demonstrates those concepts through a simplified but production-inspired architecture.

---

# Enterprise Features

- Enterprise Identity Server
- OAuth Authentication
- JWT Access Token Generation
- Refresh Token Management
- Session Lifecycle Management
- Authentication Middleware
- Authorization Middleware
- Protected Enterprise Resources
- Health Monitoring
- Enterprise REST API
- Docker-ready Deployment Structure

---

# Enterprise Architecture

```
                Client

                  │

                  ▼

             FastAPI API

                  │

                  ▼

         Authentication Middleware

                  │

                  ▼

          Authorization Middleware

                  │

                  ▼

           Enterprise Identity Server

     ┌──────────┬──────────┬───────────┬───────────┐

     ▼          ▼          ▼           ▼

 OAuth2      JWT      Refresh Tokens   Sessions

                  │

                  ▼

          Protected Enterprise APIs
```

---

# Authentication Lifecycle

```
Login

↓

Identity Server

↓

OAuth Authentication

↓

Password Verification

↓

JWT Access Token

↓

Refresh Token

↓

Enterprise Session

↓

Protected Enterprise APIs

↓

Logout

↓

Session Terminated
```

---

# REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Platform information |
| GET | /health | Health monitoring |
| POST | /login | Enterprise login |
| POST | /refresh | Refresh access token |
| POST | /logout | Enterprise logout |
| GET | /protected | Protected enterprise endpoint |

---

# Testing

Enterprise validation includes:

- API Health Tests
- Authentication Tests
- Authorization Tests
- Login Workflow
- Refresh Workflow
- Logout Workflow

```
pytest -v

5 passed
```

---

# Project Structure

```
week19-enterprise-ai-auth-platform/

app.py

Dockerfile

docker-compose.yml

requirements.txt

requirements_dev.txt

auth/

core/

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

02-enterprise-identity-platform-running.png

03-health.png

04-login-success.png

05-protected-endpoint.png

06-refresh-token.png

07-logout.png

08-tests-passing.png

09-architecture.png
```

---

# Deployment

Containerization support is included.

```
Dockerfile

docker-compose.yml
```

The project is prepared for deployment to:

- Docker
- Kubernetes
- Azure Container Apps
- AWS ECS
- Google Cloud Run

---

# Skills Demonstrated

### AI Infrastructure

- Enterprise Authentication
- Identity & Access Management
- OAuth2
- JWT
- Session Lifecycle
- RBAC

### Backend Engineering

- FastAPI
- REST APIs
- Middleware
- Modular Architecture

### Enterprise Software Engineering

- Separation of Concerns
- Layered Architecture
- Secure API Design
- Docker-ready Deployment
- Automated Testing

---

# Real-World Applications

The architecture demonstrated here can be extended into:

- Enterprise AI Platforms
- LLM Infrastructure
- AI Agent Platforms
- Multi-Agent Systems
- Healthcare AI Platforms
- MedNavi AI
- Secure Enterprise APIs

---

# Author

**Mike Nzirainengwe**

AI Infrastructure Engineer | Enterprise AI Platform Engineer | LLM Engineer

Building production-ready Enterprise AI Systems while progressing toward the long-term vision of **MedNavi AI**, an intelligent healthcare platform for Southern Africa.

---

# Enterprise Portfolio Journey

This project forms part of the AI Engineering Portfolio Journey.

Previous Enterprise Projects include:

- Week 17 – Enterprise MCP Server
- Week 18 – Enterprise Authentication Platform
- Week 19 – Enterprise Identity & Access Management Platform

The journey continues toward enterprise-scale AI infrastructure, agentic AI systems, and production-ready AI platforms.