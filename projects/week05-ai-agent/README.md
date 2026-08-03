# Week 5 — Modular AI Agent

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi)
![Transformers](https://img.shields.io/badge/Hugging_Face-Transformers-yellow)
![LLM](https://img.shields.io/badge/LLM-FLAN--T5-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

## Overview

This project demonstrates how to build a modular AI Agent from first principles.

Instead of relying on high-level agent frameworks, the system is composed of independent components responsible for planning, routing, memory management, tool execution, and language model interaction.

The architecture mirrors production AI systems where orchestration, modularity, and maintainability are essential.

---

## Key Skills Demonstrated

- AI Agent Architecture
- FastAPI API Development
- Tool Registry Pattern
- Planner & Router Design
- Stateful Memory
- Prompt Engineering
- LLM Integration
- Modular Software Design
- REST APIs
- OpenAPI / Swagger

## Features

- Multi-turn conversations
- Conversation memory
- Planner module
- Router module
- Tool Registry
- Greeting Tool
- Calculator Tool
- Hugging Face LLM integration
- FastAPI REST API
- Swagger documentation
- Modular architecture

---

## Architecture

![Architecture](architecture/week5-agent-architecture.png)

---

## Project Structure

```text
week5-ai-agent/

├── app.py
├── agent.py
├── planner.py
├── router.py
├── registry.py
├── tools.py
├── memory.py
├── llm.py
├── prompt_template.py
├── llms/
│   ├── base.py
│   └── huggingface.py
├── architecture/
├── screenshots/
├── tests/
└── README.md
```

---

## API

Run

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Swagger automatically documents every endpoint.

---

## Example Conversation

User

```
Hello
```

Assistant

```
Hello! How can I help you today?
```

User

```
My name is Mike
```

Assistant

```
Nice to meet you!
```

User

```
What is my name?
```

Assistant

```
Your name is Mike.
```

User

```
calculate 12 * 8
```

Assistant

```
The answer is 96.
```

---

## Technologies

- Python
- FastAPI
- Hugging Face Transformers
- FLAN-T5
- Prompt Engineering
- REST APIs
- Swagger
- Git
- VS Code

---

## What I Learned

This project introduced modular AI engineering concepts including:

- AI planning
- Tool routing
- Stateful conversation memory
- Tool registries
- REST API development
- OpenAPI documentation
- Software architecture documentation

---

## Next Project

Week 6 — Building a Graph-Based AI Workflow Engine