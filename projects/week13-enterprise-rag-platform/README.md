# Week 13 – Enterprise Retrieval-Augmented Generation (RAG) Knowledge Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)
![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-Embeddings-red)
![Enterprise RAG](https://img.shields.io/badge/RAG-Enterprise-success)
![Pytest](https://img.shields.io/badge/Pytest-Passing-success)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Production-ready Enterprise Retrieval-Augmented Generation (RAG) platform implementing semantic retrieval, FAISS vector search, enterprise knowledge management, and AI-powered document understanding.**

---

## Overview

This project demonstrates how enterprise AI systems retrieve organisational knowledge using semantic similarity instead of traditional keyword search.

The platform simulates the retrieval layer used by enterprise AI assistants, copilots and knowledge management systems.

The workflow includes:

- Enterprise document ingestion
- Smart document chunking
- SentenceTransformer embeddings
- FAISS vector database
- Metadata-aware semantic retrieval
- Context construction for Retrieval-Augmented Generation (RAG)

This architecture forms one of the core building blocks for enterprise AI systems and will later evolve into the foundation of **MedNavi AI**.

---

# Enterprise Features

- Enterprise Document Loader
- Smart Text Chunking
- SentenceTransformer Embeddings
- FAISS Vector Database
- Metadata-Aware Semantic Retrieval
- Enterprise Context Builder
- Retrieval-Augmented Generation (RAG) Pipeline
- Automated Integration Testing
- Production-Ready Docker Configuration
- Professional Documentation

---

# Enterprise Architecture

```text
Enterprise Documents
        │
        ▼
Enterprise Document Loader
        │
        ▼
Smart Chunking Service
        │
        ▼
SentenceTransformer Embeddings
        │
        ▼
FAISS Vector Database
        │
        ▼
Enterprise Retriever
        │
        ▼
Top-K Semantic Results
        │
        ▼
Context Builder
        │
        ▼
Enterprise RAG Pipeline
        │
        ▼
Future LLM Response
```

Architecture Diagram:

```
docs/week13-vector-rag-platform-architecture.png
```

---

# Project Structure

```text
week13-enterprise-rag-platform/

├── agents/
├── config/
├── data/
├── docs/
├── embeddings/
├── graphs/
├── ingestion/
├── memory/
├── models/
├── planner/
├── registry/
├── retriever/
├── screenshots/
├── services/
├── tests/
├── vectorstore/
│
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.13 |
| Embeddings | SentenceTransformers |
| Vector Database | FAISS |
| AI Framework | Hugging Face |
| Retrieval | Semantic Search |
| Testing | Pytest |
| Containerisation | Docker |
| Documentation | Markdown |

---

# Running the Project

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the platform

```bash
python app.py
```

Example output

```
========================================
 Enterprise RAG Pipeline
========================================

User Question
---------------------------
Explain Retrieval-Augmented Generation

Retrieved Context
---------------------------
Source: ai_notes.txt
...

Pipeline Complete.
```

---

# Automated Testing

Run

```bash
pytest
```

Expected output

```
====================

1 passed

====================
```

---

# Docker

This repository includes a production-ready Dockerfile and `.dockerignore`.

The Docker configuration has been completed and verified.

Because this project was developed on limited hardware (8 GB RAM with mechanical HDD), the final Docker image build was intentionally not required after successful Docker demonstrations in previous portfolio projects.

The project remains fully container-ready and can be built on any modern Docker environment using:

```bash
docker build -t week13-enterprise-rag-platform .
docker run week13-enterprise-rag-platform
```

---

# Screenshots

| Screenshot | Description |
|------------|-------------|
| 01-week13-enterprise-knowledge-base.png | Enterprise document loading |
| 02-week13-enterprise-chunking-success.png | Smart document chunking |
| 03-week13-faiss-vector-store-success.png | FAISS vector database |
| 04-week13-enterprise-retrieval-success.png | Semantic retrieval |
| 05-week13-rag-pipeline-success.png | Complete RAG pipeline |
| 06-week13-rag-tests-passing.png | Automated integration tests |
| 07-week13-enterprise-architecture.png | Enterprise architecture diagram |
| 08-week13-readme-preview.png | Professional documentation |
| 09-week13-final-project.png | Final project verification |

---

# Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Enterprise Knowledge Systems
- Semantic Search
- Sentence Embeddings
- FAISS Vector Databases
- Enterprise Retrieval Pipelines
- Context Construction
- Automated Testing
- Docker Configuration
- Enterprise Software Engineering

---

# Learning Outcomes

By completing this project I learned how to:

- Build enterprise document ingestion pipelines
- Chunk documents for semantic retrieval
- Generate sentence embeddings
- Build FAISS vector indexes
- Retrieve knowledge semantically
- Build context for RAG systems
- Test an enterprise AI pipeline
- Prepare AI applications for production deployment

---

# Future Improvements

Future enterprise upgrades include:

- Hybrid Search (BM25 + Vector Search)
- Metadata Filtering
- ChromaDB
- Pinecone
- Weaviate
- PostgreSQL pgvector
- Milvus
- Enterprise RAG APIs
- LangGraph Orchestration
- LLM-powered Answer Generation

---

# Portfolio Progress

```
Week 1  ✓ AI Summarizer
Week 2  ✓ FastAPI AI API
Week 3  ✓ Docker Deployment
Week 4  ✓ AI Microservices
Week 5  ✓ Production Platform
Week 6  ✓ Enterprise APIs
Week 7  ✓ AI Orchestration
Week 8  ✓ LangGraph
Week 9  ✓ Enterprise Platform
Week 10 ✓ Multi-Agent Platform
Week 11 ✓ Memory & RAG Platform
Week 12 ✓ Vector Databases & Semantic Search
Week 13 ✓ Enterprise RAG Knowledge Platform
```

---

# Author

## Mike Nzirainengwe

**LLM Engineer | AI Platform Engineer | AI Infrastructure Engineer | AI Solutions Architect (in progress)**

Building enterprise AI systems with the long-term mission of developing **MedNavi AI**, a multilingual clinical AI platform for intelligent documentation, Retrieval-Augmented Generation (RAG), enterprise workflow automation and AI-assisted healthcare.

---

## Project Status

**Status:** Production-ready portfolio project

Maintained as part of the AI Engineer Journey portfolio and continuously improved as new enterprise AI capabilities are developed.