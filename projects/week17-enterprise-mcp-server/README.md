# Week 17 — Enterprise Model Context Protocol (MCP) Server

> **Enterprise AI Infrastructure | MCP-Style Tool Infrastructure | Tool Discovery | Session & Context Management**

---

## 🏛️ Project Overview

Week 17 introduces an **Enterprise Model Context Protocol (MCP) Server** designed to demonstrate how AI systems can discover and invoke enterprise capabilities through a structured, protocol-driven architecture.

This project represents a transition from building AI applications toward building the **infrastructure layer that AI systems depend on**.

The implementation uses **FastAPI** as the HTTP/API layer and separates core responsibilities into dedicated components for:

- MCP server orchestration
- Tool discovery
- Tool invocation
- Session management
- Context management
- Structured request validation
- Standardized responses
- Protocol metadata
- Automated API testing

> **Scope clarification:** This project demonstrates an **MCP-style / MCP-inspired enterprise architecture**. It does not implement the official Model Context Protocol specification. Compatibility with that specification is identified as a future enhancement.

---

# 🎯 Engineering Objective

The objective is to demonstrate the design of a modular infrastructure component positioned between an AI client or LLM and enterprise capabilities.

The architecture separates protocol handling from individual tool implementations:

```text
                 Client / LLM
                      │
                      ▼
                FastAPI API Layer
                      │
                      ▼
                MCP Server Engine
                 │     │      │
                 │     │      └── Tool Registry
                 │     │             │
                 │     │       ┌─────┼─────┐
                 │     │       ▼     ▼     ▼
                 │     │    Search Summarize Translate
                 │     │
                 │     └── Context Manager
                 │
                 └── Session Manager

This separation establishes a foundation for enterprise AI systems in which AI reasoning and enterprise tool execution are treated as separate architectural concerns.

🧩 Core Capabilities
1. MCP Server Engine

The central MCPServer component coordinates:

Session creation
Context updates
Tool discovery
Tool invocation
Standardized responses
Protocol metadata

The implementation is located in:

core/mcp_server.py
2. Structured Request Contract

The project defines a Pydantic-based MCPRequest model containing:

session_id
tool
input
metadata

This establishes a structured request contract for MCP-style tool interactions.

Source:

core/mcp_request.py
3. Standardized Response Contract

Tool invocations return an MCPResponse model containing:

session_id
tool
status
output
metadata

Responses also include protocol metadata:

{
  "metadata": {
    "protocol": "MCP",
    "version": "1.0"
  }
}

Source:

core/mcp_response.py

This provides clients with a consistent response structure regardless of which registered tool was invoked.

🔎 Tool Discovery

The server exposes a dedicated tool-discovery endpoint:

GET /mcp/tools

The current tool registry contains:

search
summarize
translate

The registry is implemented separately from the MCP server engine:

registry/tool_registry.py

This separation makes the architecture extensible because additional enterprise capabilities can be registered without placing all tool definitions directly inside the API layer.

⚙️ Tool Invocation

Tools are invoked through:

POST /mcp/invoke

Example request:

{
  "tool": "search",
  "input": {
    "query": "Enterprise RAG"
  }
}

The MCP server:

Creates a session.
Stores the last invoked tool in the session context.
Identifies the requested tool.
Executes the corresponding tool behaviour.
Creates a standardized MCPResponse.
Returns protocol metadata with the response.

The implementation currently supports:

Search

Returns a structured message representing an enterprise knowledge search.

Summarize

Returns a structured message representing summarization of supplied text.

Translate

Returns a structured message representing translation of supplied text.

Unknown Tools

Unknown tool names are handled by the server and returned through the standardized response structure.

🧠 Session Management

The project includes a dedicated:

core/session_manager.py

The SessionManager generates unique session identifiers using UUIDs.

Each invocation through the MCP server creates a session identifier that is returned in the standardized response.

This establishes a foundation for associating requests with individual AI workflows or interactions.

🧠 Context Management

The project also includes:

core/context_manager.py

The ContextManager maintains session-scoped context.

The current implementation stores key/value information against a generated session identifier.

During tool invocation, the server records the most recently requested tool:

session_id
    │
    └── last_tool

This demonstrates the architectural separation between:

API transport
Session identity
Workflow context

The architecture can therefore evolve toward more sophisticated stateful AI workflows in later iterations.

🌐 REST API

The current FastAPI application exposes the following endpoints:

| Method | Endpoint      | Purpose              |
| ------ | ------------- | -------------------- |
| `GET`  | `/`           | Platform information |
| `GET`  | `/health`     | Service health       |
| `GET`  | `/mcp/tools`  | Tool discovery       |
| `POST` | `/mcp/invoke` | Tool invocation      |

The API is implemented in:

app.py

FastAPI also provides the interactive Swagger/OpenAPI interface used as part of the project's evidence.

🏗️ Architecture Components
FastAPI API Layer

Provides the HTTP interface through which clients interact with the Enterprise MCP Server.

MCP Server Engine

Coordinates sessions, context, tool discovery, tool invocation, and standardized responses.

Session Manager

Generates unique UUID-based session identifiers.

Context Manager

Maintains session-scoped contextual information.

Tool Registry

Maintains the catalogue of available enterprise tools.

Current registered capabilities:

Search
Summarize
Translate
Request / Response Models

Pydantic models define structured MCP-style request and response contracts.

📐 Architecture Documentation

Detailed architecture documentation is maintained separately from the application README.

Architecture Documentation

docs/architecture.md

Architecture Diagram

docs/architecture.png

Editable Draw.io Architecture Source

docs/architecture.drawio

The architecture documentation describes the relationship between:

FastAPI
   │
   ▼
MCP Server
   │
   ├── Session Manager
   │
   ├── Context Manager
   │
   └── Tool Registry
            │
            ├── Search
            ├── Summarize
            └── Translate
🧪 Automated Testing

The project contains automated tests using:

pytest
FastAPI TestClient

The test suite validates the core server functionality.

Tested Areas
Root endpoint
Health endpoint
Tool discovery
Search tool
Summarize tool
Translate tool
Unknown tool handling
Session creation
Protocol metadata
Test Files
tests/
├── test_health.py
├── test_mcp_server.py
└── test_tools.py
Verified Result

9 tests passing

The test suite provides automated evidence that the implemented API and MCP-style server behaviours operate as expected.

📸 Evidence & Demonstrations

The repository contains visual evidence covering the implemented API and server functionality.

API & Platform
Home Endpoint

screenshots/01-home-endpoint.png

Health Endpoint

screenshots/02-health-endpoint.png

MCP Tool Discovery

screenshots/03-mcp-tools.png

MCP Search Tool

screenshots/04-mcp-search-tool.png

MCP Summarize Tool

screenshots/05-mcp-summarize-tool.png

MCP Translate Tool

screenshots/06-mcp-translate-tool.png

Swagger / OpenAPI Overview

screenshots/07-swagger-overview.png

Tests Passing

screenshots/08-tests-passing.png

These screenshots provide portfolio evidence for the implemented API, tool discovery, tool invocation, Swagger interface, and automated testing.

📁 Project Structure
week17-enterprise-mcp-server/
│
├── api/
│   └── __init__.py
│
├── config/
│   └── __init__.py
│
├── core/
│   ├── __init__.py
│   ├── context_manager.py
│   ├── mcp_request.py
│   ├── mcp_response.py
│   ├── mcp_server.py
│   └── session_manager.py
│
├── registry/
│   ├── __init__.py
│   ├── prompt_registry.py
│   ├── resource_registry.py
│   └── tool_registry.py
│
├── services/
│   └── __init__.py
│
├── tools/
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_mcp_server.py
│   └── test_tools.py
│
├── docs/
│   ├── architecture.drawio
│   ├── architecture.md
│   └── architecture.png
│
├── screenshots/
│   ├── 01-home-endpoint.png
│   ├── 02-health-endpoint.png
│   ├── 03-mcp-tools.png
│   ├── 04-mcp-search-tool.png
│   ├── 05-mcp-summarize-tool.png
│   ├── 06-mcp-translate-tool.png
│   ├── 07-swagger-overview.png
│   └── 08-tests-passing.png
│
├── app.py
├── requirements.txt
├── requirements-dev.txt
└── README.md

🛠️ Technology Stack
Backend
Python
FastAPI
Pydantic
REST API
Uvicorn
AI Infrastructure
MCP-style protocol architecture
Tool discovery
Tool registry
Tool invocation
Session management
Context management
Structured request/response contracts
Protocol metadata
Testing
Pytest
FastAPI TestClient
Documentation
Markdown
Draw.io
Architecture documentation
Swagger/OpenAPI
🔐 Enterprise Design Principles
Modular Architecture

Responsibilities are separated into dedicated modules instead of being concentrated in a single application file.

Single Responsibility

Session management, context management, tool registration, request/response contracts, and MCP orchestration have dedicated components.

Protocol-Driven Design

AI capabilities are exposed through a structured protocol-style interface rather than requiring clients to understand individual tool implementations.

Extensible Tool Registry

The registry provides a central mechanism for discovering available enterprise capabilities.

Standardized Responses

Tool execution returns a consistent response containing:

Session information
Tool name
Status
Output
Protocol metadata
Separation of AI Reasoning and Tool Execution

The architecture establishes a clear boundary between the AI client or LLM and the enterprise capabilities that it can invoke.

🚀 Deployment Roadmap

The architecture documentation identifies deployment and infrastructure expansion as future stages.

Current
   │
   ▼
FastAPI MCP-Style Server
   │
   ▼
Docker Containerization
   │
   ▼
Kubernetes
   │
   ▼
CI/CD
   │
   ▼
Cloud Deployment
   │
   ▼
Enterprise Observability

These stages represent future evolution beyond the current local implementation.

🔮 Future Evolution

The architecture documentation identifies several future enhancements:

Authentication
RBAC
API keys
Async execution
Streaming responses
Full official MCP protocol compatibility
OpenTelemetry observability
Kubernetes deployment
Cloud deployment
CI/CD automation

These enhancements represent the natural evolution from an MCP-style enterprise tool server toward a more complete AI infrastructure platform.

🔗 Position in the AI Engineering Journey

Week 17 represents an important architectural transition in the portfolio.

The progression is:

AI Applications
      ↓
LLM Systems
      ↓
RAG & Agentic Systems
      ↓
AI Platforms
      ↓
AI Infrastructure
      ↓
MCP & Tool Infrastructure

Instead of focusing only on what an AI application can do, this milestone focuses on how AI systems communicate with and invoke external capabilities.

📈 Evolution into Week 18

Week 18 builds on the infrastructure foundation established here by introducing enterprise authentication and security capabilities.

Week 17
Enterprise MCP-Style Tool Infrastructure
          │
          ▼
Week 18
Enterprise Authentication & Security

This progression moves the portfolio toward increasingly complete enterprise AI infrastructure involving authentication, identity, authorization, gateways, and cloud-native systems.

🎯 Skills Demonstrated
AI Infrastructure Engineering
MCP-style architecture
Tool discovery
Tool invocation
Protocol-driven infrastructure
Enterprise tool registries
Backend Engineering
Python
FastAPI
REST API design
Pydantic
Modular backend architecture
Uvicorn
Enterprise Architecture
Session management
Context management
Protocol metadata
Component separation
Extensible architecture
Standardized responses
Quality Engineering
Automated API testing
FastAPI TestClient
Endpoint verification
Tool behaviour validation
Session validation
Protocol metadata validation
Technical Documentation
Architecture documentation
Draw.io system diagrams
Swagger/OpenAPI documentation
Evidence-based portfolio documentation
💼 Portfolio Relevance

This project demonstrates practical capabilities relevant to roles such as:

LLM Engineer
AI Infrastructure Engineer
AI Platform Engineer
AI Backend Engineer
Enterprise AI Engineer
AI Systems Engineer

The strongest portfolio value of Week 17 is its demonstration of the infrastructure boundary between AI reasoning systems and enterprise tools.

It shows an understanding that production AI systems require structured interfaces for discovering, invoking, and managing external capabilities.
