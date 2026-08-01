# Week 17 – Enterprise Model Context Protocol (MCP) Server

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Enterprise-green)
![MCP](https://img.shields.io/badge/Model_Context_Protocol-MCP-orange)
![Architecture](https://img.shields.io/badge/Architecture-Enterprise-purple)
![Testing](https://img.shields.io/badge/Pytest-Passing-success)

---

# Enterprise AI Engineering Journey

**Week 17** introduces an **Enterprise Model Context Protocol (MCP) Server**, demonstrating how modern AI platforms expose tools, services, and capabilities to Large Language Models (LLMs) using a standardized protocol.

Unlike earlier weeks that focused on AI applications and orchestration, this project moves deeper into **AI Infrastructure Engineering**, simulating how production AI platforms communicate with enterprise tools.

This project represents a major transition from building AI applications to building the **infrastructure that powers AI systems**.

---

# Project Objectives

The Enterprise MCP Server demonstrates:

- Enterprise AI communication protocols
- Tool discovery
- Standardized tool metadata
- Session-based request processing
- Protocol metadata
- Enterprise API architecture
- AI platform design patterns
- Production-ready documentation
- Automated testing

---

# Why Model Context Protocol (MCP)?

Modern LLM systems rarely work alone.

Instead, they interact with:

- Internal enterprise APIs
- Search systems
- Databases
- ERP systems
- CRM platforms
- Medical systems
- Financial systems
- Security systems

MCP provides a **standard protocol** allowing AI models to safely communicate with external capabilities.

This architecture is increasingly adopted across enterprise AI systems because it separates:

- AI reasoning
- Tool execution
- Security
- Infrastructure

---

# Architecture

```
                Client
                   │
                   ▼
            FastAPI REST API
                   │
                   ▼
             MCP Server Engine
                   │
        ┌──────────┼───────────┐
        ▼          ▼           ▼
    Search     Summarize   Translate
       Tool        Tool         Tool
```

The MCP Server receives requests from clients, identifies the requested enterprise tool, executes the tool, and returns standardized responses.

---

# Enterprise Components

## MCP Server

Responsible for:

- Managing sessions
- Routing requests
- Executing enterprise tools
- Returning protocol-compliant responses

---

## Tool Registry

Maintains a catalogue of available enterprise tools.

Example:

- Search
- Summarize
- Translate

The registry allows AI systems to discover capabilities dynamically.

---

## Tool Metadata

Every enterprise tool exposes metadata including:

- Name
- Description
- Version
- Input schema
- Output schema

This allows AI agents to understand available capabilities without hardcoding behaviour.

---

## REST API

The server exposes enterprise endpoints including:

### Root

```
GET /
```

Platform information.

---

### Health Check

```
GET /health
```

Platform availability.

---

### Available Tools

```
GET /tools
```

Returns all registered enterprise tools.

---

### Execute Tool

```
POST /mcp
```

Example:

```json
{
  "tool": "search",
  "payload": {
    "query": "Enterprise RAG"
  }
}
```

---

# Example Response

```json
{
  "session_id": "...",
  "tool": "search",
  "status": "success",
  "output": {
    "message": "Searching enterprise knowledge..."
  },
  "metadata": {
    "protocol": "MCP",
    "version": "1.0"
  }
}
```

---

# Testing

Automated tests validate:

- Root endpoint
- Health endpoint
- Tool discovery
- Search tool
- Summarizer tool
- Translator tool
- Unknown tool handling
- Session creation
- Protocol metadata

Current status:

**9 Tests Passing**

---

# Folder Structure

```
week17-enterprise-mcp-server/
│
├── app.py
├── auth/
├── core/
├── registry/
├── models/
├── tests/
├── docs/
├── screenshots/
└── README.md
```

---

# Screenshots

Included:

- Swagger API
- Tool Discovery
- MCP Execution
- Architecture Diagram
- Test Results

---

# Enterprise Skills Demonstrated

- FastAPI
- REST API Design
- Enterprise AI Infrastructure
- MCP Protocol
- Tool Discovery
- Modular Architecture
- Session Management
- Protocol Design
- Automated Testing
- Software Documentation

---

# Portfolio Relevance

This project demonstrates skills directly applicable to roles such as:

- AI Infrastructure Engineer
- LLM Engineer
- AI Platform Engineer
- Backend AI Engineer
- Enterprise AI Solutions Engineer

---

# Next Evolution

Week 18 expands this architecture by introducing:

- Enterprise Authentication
- API Keys
- Role-Based Access Control (RBAC)
- Security Middleware

Together, Weeks 17 and 18 form the foundation of a production-grade enterprise AI platform.

---

## Author

**Mike Nzirainengwe**

AI Engineering Journey

Building production-ready AI systems, enterprise infrastructure, and Generative AI platforms one week at a time.

GitHub Portfolio:
https://github.com/mnzirain/ai-engineer-journey