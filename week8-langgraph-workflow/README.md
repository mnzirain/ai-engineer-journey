# Week 8 – Enterprise LangGraph Workflow

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-1.x-green)
![LangChain](https://img.shields.io/badge/LangChain-Core-success)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-Pytest-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![AI Engineer Journey](https://img.shields.io/badge/AI%20Engineer%20Journey-Week%208-purple)

> Building Enterprise AI Workflows using LangGraph 1.x

---

## Overview

This project demonstrates how to build an enterprise-ready AI workflow using **LangGraph 1.x**.

Rather than implementing a single monolithic workflow, the project introduces architectural components commonly used in production AI systems:

- Enterprise Planner
- Workflow Registry
- Specialized Workflow Graphs
- LangGraph State Management
- Containerization with Docker
- Unit Testing using Pytest

The objective is to learn workflow orchestration while designing software that resembles real enterprise AI platforms.

---

# Technologies Used

- Python 3.13
- LangGraph 1.x
- LangChain Core
- Pytest
- Docker
- Git
- VS Code

---

# Project Structure

```text
week8-langgraph-workflow/

├── app.py
├── graph.py
├── Dockerfile
├── .dockerignore
├── pytest.ini
├── README.md

├── config/
│   ├── __init__.py
│   └── settings.py

├── services/
│   ├── __init__.py
│   └── planner_service.py

├── graphs/
│   ├── __init__.py
│   ├── greeting_graph.py
│   └── workflow_registry.py

├── nodes/
│   ├── planner_node.py
│   ├── greeting_node.py
│   ├── knowledge_node.py
│   └── calculator_node.py

├── state/
│   ├── __init__.py
│   └── workflow_state.py

├── tests/
│   ├── __init__.py
│   └── test_planner.py

├── architecture/

└── Screenshots/
```

---

## Enterprise Architecture

The following diagram illustrates the enterprise workflow introduced in Week 8.

![Architecture](Screenshots/16-week8-enterprise-architecture.png)

This project introduces an enterprise workflow architecture:

```text
                User

                  │

                  ▼

         Enterprise Planner

                  │

                  ▼

          Workflow Registry

      ┌─────────┼─────────┐

      ▼         ▼         ▼

 Greeting   Calculator   Knowledge

 Workflow    Workflow    Workflow
```

This architecture separates:

- decision making
- workflow selection
- workflow execution

which improves scalability and maintainability.

---

# Features

- Enterprise Planner Service
- Workflow Registry
- LangGraph MessagesState
- Greeting Workflow
- Knowledge Workflow
- Calculator Workflow (prototype)
- Docker Support
- Unit Tests
- Enterprise Project Structure

---

# Unit Testing

Planner classification is verified using Pytest.

Current tests:

- Greeting classification
- Calculator classification
- Knowledge classification

Result:

✅ 3 Tests Passed

---

# Docker Support

The project includes:

- Dockerfile
- .dockerignore

The application builds successfully inside Docker and executes the workflow.

---

## Screenshots

### 1. First LangGraph Workflow

Demonstrates the first successful LangGraph workflow execution.

![First Workflow](Screenshots/01-first-workflow.png)

---

### 2. Multi-Node Workflow

Shows the transition from a single-node workflow to a multi-node enterprise workflow.

![Multi Node Workflow](Screenshots/02-multi-node-workflow.png)

---

### 3. Enterprise Workflow

Demonstrates the enterprise version of the LangGraph workflow.

![Enterprise Workflow](Screenshots/03-enterprise-workflow.png)

---

### 4. Enterprise Workflow Code

Core implementation of the enterprise workflow architecture.

![Workflow Code](Screenshots/04-enterprise-workflow-code.png)

---

### 5. Conditional Routing

Planner successfully selecting the correct workflow based on user input.

![Conditional Routing](Screenshots/05-conditional-routing.png)

---

### 6. Conditional Routing Code

Implementation of the enterprise routing logic.

![Conditional Routing Code](Screenshots/06-conditional-routing-code.png)

---

### 7. Docker Build

Successful containerization of the project.

![Docker Build](Screenshots/07-docker-build.png)

---

### 8. Docker Execution

Successful execution of the application inside a Docker container.

![Docker Run](Screenshots/08-docker-run.png)

---

### 9. Enterprise Architecture

Final enterprise architecture used throughout Week 8.

![Enterprise Architecture](Screenshots/09-enterprise-architecture.png)

---

# Engineering Decision

During development, LangGraph conditional routing exposed a framework-specific branch resolution issue when routing calculator requests inside a single monolithic graph.

Rather than tightly coupling workflow routing inside LangGraph, the project was intentionally redesigned toward an enterprise architecture using:

- Enterprise Planner
- Workflow Registry
- Specialized Workflow Graphs

This architecture more closely resembles production AI systems and becomes the foundation for the next phase of the AI Engineer Journey.

---

# Lessons Learned

- LangGraph workflow fundamentals
- MessagesState
- Enterprise workflow design
- Workflow separation
- Docker containerization
- Enterprise project organization
- Automated testing with Pytest

---

# Next Steps

Week 9 introduces:

- Multiple independent workflow graphs
- Enterprise Workflow Platform
- Dynamic graph selection
- Workflow orchestration
- Scalable AI platform architecture

---

# Author

**Mike Nzirainengwe**

AI Engineer Journey

Building towards becoming:

- LLM Engineer
- AI Infrastructure Engineer
- AI Architect