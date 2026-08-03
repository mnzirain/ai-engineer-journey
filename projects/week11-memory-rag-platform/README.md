# 🚀 Week 11 — Enterprise Memory & RAG Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-green)
![LangChain](https://img.shields.io/badge/LangChain-Framework-success)
![RAG](https://img.shields.io/badge/RAG-Memory%20Platform-purple)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📖 Overview

This project extends the Enterprise Multi-Agent Platform by introducing a shared memory layer and retrieval capabilities, forming the foundation of a Retrieval-Augmented Generation (RAG) architecture.

The platform demonstrates how multiple AI agents can share persistent knowledge while remaining modular, scalable, and independently deployable.

---

## ✨ Enterprise Features

- Enterprise Workflow Planner
- Supervisor Graph Routing
- Greeting Agent
- Calculator Agent
- Knowledge Agent
- Translation Agent
- Memory Agent
- Retrieval Agent
- Shared Memory Store
- Retrieval Service
- Docker Container
- Enterprise Testing

---

## 🏗️ Enterprise Architecture

The system uses a layered enterprise architecture.

```text
User
        │
        ▼
Enterprise Planner
        │
        ▼
Supervisor Graph
        │
 ┌──────┼─────────────────────────────┐
 ▼      ▼      ▼      ▼      ▼       ▼
Greeting Calculator Knowledge Translation Memory Retrieval
        │                            │
        │                            ▼
        │                  Retrieval Service
        │                            │
        └──────────────► Memory Store
```

📄 Detailed architecture documentation:

```
docs/week11-memory-rag-platform-architecture.md
```

🖼️ Architecture diagram:

```
docs/week11-memory-rag-platform-architecture.png
```

---

## 📁 Project Structure

```text
week11-memory-rag-platform/
├── agents/
├── config/
├── docs/
├── embeddings/
├── graphs/
├── memory/
├── models/
├── planner/
├── registry/
├── retriever/
├── screenshots/
├── services/
├── tests/
├── Dockerfile
├── requirements.txt
└── app.py
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/mnzirain/ai-engineer-journey.git
```

Navigate into the project:

```bash
cd week11-memory-rag-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

# 🐳 Docker

Build the container:

```bash
docker build -t week11-memory-rag-platform .
```

Run the platform:

```bash
docker run --rm week11-memory-rag-platform
```

---

# 🧪 Enterprise Testing

Run all tests:

```bash
pytest
```

The project includes automated tests for:

- Memory Service
- Retrieval Service
- Enterprise Planner
- Multi-Agent Routing

---

# 📸 Project Screenshots

| Screenshot | Description |
|------------|-------------|
| 01 | Initial Project Structure |
| 02 | Memory Service |
| 03 | Retrieval Service |
| 04 | Memory & Retrieval Agents |
| 05 | Supervisor Graph |
| 06 | Platform Running Successfully |
| 07 | Memory Retrieval Success |
| 08 | Docker Build & Container Success |
| 09 | All Tests Passing |

---

# 🛠️ Technologies Used

- Python 3.13
- LangChain
- LangGraph
- Docker
- Pytest
- Enterprise Workflow Architecture
- Multi-Agent AI
- Shared Memory
- Retrieval-Augmented Generation (RAG) Foundations

---

# 🎯 Learning Outcomes

By completing this project I learned how to:

- Design enterprise memory architecture
- Build retrieval services
- Separate memory writing from retrieval
- Build modular AI agents
- Route requests through a supervisor graph
- Dockerize enterprise AI platforms
- Write automated tests
- Build scalable AI software using software engineering principles

---

# 🚀 Future Improvements

- Vector Database Integration (FAISS / ChromaDB)
- Semantic Embeddings
- Long-Term Conversation Memory
- RAG Document Retrieval
- OpenAI Integration
- Local LLM Support
- Redis Memory Layer
- PostgreSQL Persistence
- Kubernetes Deployment
- Production Monitoring

---

# 👨‍💻 Author

**Mike Nzirainengwe**

**LLM Engineer | AI Infrastructure Engineer | AI Solutions Architect**

Building enterprise-grade AI systems with a focus on:

- Large Language Models (LLMs)
- Multi-Agent AI Systems
- AI Infrastructure
- RAG Architectures
- MLOps
- Cloud AI Platforms

GitHub Portfolio:

https://github.com/mnzirain/ai-engineer-journey

---

⭐ If you found this project useful, consider starring the repository.