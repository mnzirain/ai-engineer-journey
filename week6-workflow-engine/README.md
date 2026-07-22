# Week 6 – AI Workflow Engine

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![AI Engineering Journey](https://img.shields.io/badge/AI%20Engineer%20Journey-Week%206-blueviolet)


> Dynamic AI Workflow Orchestration with FastAPI and Docker

---

## Overview

This project demonstrates the design and implementation of a lightweight AI Workflow Engine built entirely in Python.

The engine dynamically routes user requests to specialized workflow nodes using a planner and execution engine while maintaining shared workflow state.

The project also exposes the engine through a FastAPI REST API and packages the entire application inside a Docker container.

This project forms part of my AI Engineer Journey toward becoming a world-class LLM Engineer, AI Infrastructure Engineer, and AI Architect.

---

# Architecture

The complete system architecture is available below.

![Architecture](architecture/week6-workflow-engine-architecture.png)

---

# Features

- Workflow State Management
- Dynamic Workflow Planning
- Workflow Graph
- Graph Traversal
- Execution Engine
- Greeting Node
- Calculator Node
- Memory Store Node
- Memory Retrieve Node
- FastAPI REST API
- Docker Containerization

---

# Project Structure

```text
week6-workflow-engine/

├── architecture/
│   ├── week6-workflow-engine.drawio
│   └── week6-workflow-engine-architecture.png
│
├── nodes/
│   ├── base_node.py
│   ├── planner_node.py
│   ├── greeting_node.py
│   ├── calculator_node.py
│   ├── memory_store_node.py
│   └── memory_retrieve_node.py
│
├── tests/
│
├── Dockerfile
├── .dockerignore
├── engine.py
├── graph.py
├── state.py
├── condition.py
└── app.py
```

---

# Workflow

```
User

↓

FastAPI

↓

Workflow Engine

↓

Planner

↓

Workflow Builder

↓

Execution Engine

↓

Workflow Nodes

↓

Workflow State

↓

JSON Response
```

---

# API Endpoints

## POST /workflow

Example Request

```json
{
    "message": "What is my name?"
}
```

Example Response

```json
{
    "response": "Your name is Mike."
}
```

---

# Docker

Build

```bash
docker build -t workflow-engine .
```

Run

```bash
docker run -p 8000:8000 workflow-engine
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Screenshots

## Swagger Overview

![](Screenshots/01-swagger-overview.png)

---

## Greeting

![](Screenshots/02-greeting-test.png)

---

## Memory Store

![](Screenshots/03-memory-store.png)

---

## Memory Retrieve

![](Screenshots/04-memory-retrieve.png)

---

## Calculator

![](Screenshots/05-calculator-test.png)

---

## Uvicorn Running

![](Screenshots/06-uvicorn-running.png)

---

## Docker Running

![](Screenshots/07-docker-running.png)

---

## Swagger Running Inside Docker

![](Screenshots/08-swagger-inside-docker.png)

---

# Technologies

- Python
- FastAPI
- Uvicorn
- Docker
- Git
- GitHub

---

# Learning Objectives

This project demonstrates understanding of:

- AI Workflow Design
- Dynamic Workflow Planning
- Graph Traversal
- Shared Workflow State
- REST API Development
- Docker Containerization
- Software Architecture

---

# Future Improvements

- Multi-Agent Workflows
- LangGraph Integration
- CrewAI Integration
- LLM Routing
- Persistent Memory
- Tool Calling
- Kubernetes Deployment

---

# Author

Mike Nzirainengwe

AI Engineer Journey Portfolio

2026