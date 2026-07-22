# Week 7 – Enterprise Multi-Agent Orchestrator

# Week 7 – Enterprise Multi-Agent Orchestrator

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![AI Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-purple)
![Portfolio](https://img.shields.io/badge/Portfolio-AI%20Engineering-orange)

## Project Overview

This project demonstrates a production-style AI Multi-Agent Orchestrator built with FastAPI and Python.

Unlike a single chatbot, the system automatically plans tasks, builds context, discovers available AI agents dynamically, routes work to specialized agents, and executes tools through a centralized Tool Registry.

This project represents the transition from simple AI applications to enterprise AI system architecture.

---

## Architecture

The system follows a modular layered architecture.

```
User
   │
FastAPI API
   │
Orchestrator Engine
   │
Planner
   │
Workflow State
   │
Context Builder
   │
Router
   │
Dynamic Agent Discovery
   │
Specialized Agents
   │
Tool Registry
   │
Final Response
```

See:

```
architecture/
```

and

```
Screenshots/
week7-enterprise-architecture.png
```

---

## Folder Structure

```
week7-multi-agent-orchestrator/

app.py
engine.py
planner.py
router.py
registry.py
context_builder.py
state.py

agents/
tools/
tests/
architecture/
Screenshots/
```

---

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Docker
- Git
- GitHub

---

## Features

- Multi-Agent Architecture
- Planner
- Context Builder
- Router
- Workflow State
- Dynamic Agent Discovery
- Specialized AI Agents
- Tool Registry
- Memory Tool
- Calculator Tool
- Docker Containerization

---

## Implemented Agents

| Agent | Purpose |
|--------|----------|
| Greeting Agent | Handles greetings |
| Memory Agent | Stores and retrieves memory |
| Calculator Agent | Performs calculations |
| Knowledge Agent | General knowledge responses |
| Echo Agent | Demonstrates automatic discovery |

---

## Tool Registry

Currently implemented:

- Calculator Tool
- Memory Tool

Architecture supports future tools such as:

- Greeting Tool
- Knowledge Tool

without changing the orchestration engine.

---

## Running Locally

Activate environment

```bash
source .venv313/Scripts/activate
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## Running with Docker

Build

```bash
docker build -t week7-orchestrator .
```

Run

```bash
docker run -d -p 8000:8000 --name week7-container week7-orchestrator
```

Open

```
http://localhost:8000/docs
```

---

## Example Requests

```
Hello
```

```
20 + 30
```

```
My name is Mike
```

```
What is my name?
```

---

## Skills Demonstrated

- AI System Design
- Multi-Agent Systems
- AI Workflow Orchestration
- Context Management
- Dynamic Agent Discovery
- Modular Architecture
- Docker
- FastAPI APIs
- Enterprise Software Design

---

## Future Improvements

- LangGraph Integration
- LlamaIndex
- Vector Database
- Redis Memory
- Kubernetes Deployment
- AWS Deployment
- OpenTelemetry Monitoring
- Multi-LLM Support

---

## Author

**Mike Nzirainengwe**

AI Engineering Journey

Building toward becoming:

- World-Class LLM Engineer
- AI Infrastructure Engineer
- AI Architect