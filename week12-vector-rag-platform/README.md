# Week 12 – Enterprise Vector Databases & Semantic Search

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)
![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-Embeddings-red)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Pytest](https://img.shields.io/badge/Pytest-Passing-success)
![Enterprise AI](https://img.shields.io/badge/Enterprise-AI%20Engineering-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Production-style enterprise semantic search platform using FAISS, Sentence Transformers, LangChain, FastAPI, and enterprise vector database architecture.**

---

## Overview

This project demonstrates how modern Retrieval-Augmented Generation (RAG) systems retrieve information using semantic similarity instead of traditional keyword matching.

The platform performs an enterprise-grade retrieval workflow by:

- Loading enterprise knowledge documents
- Chunking large documents into searchable sections
- Generating sentence embeddings
- Building a FAISS vector database
- Performing semantic similarity search
- Returning the most relevant knowledge to the user

This architecture represents one of the core building blocks used in production AI systems, enterprise copilots, intelligent assistants, and future healthcare platforms such as **MedNavi AI**.

---

# Enterprise Features

- Enterprise Document Loader
- Smart Text Chunking
- SentenceTransformer Embeddings
- FAISS Vector Database
- Semantic Similarity Search
- Enterprise Retrieval Service
- Docker Containerization
- Automated Testing with Pytest
- Enterprise Documentation
- Professional Architecture Diagram

---

# Enterprise Architecture

```
                 Enterprise Semantic Search Platform

          Documents (.txt)
                 │
                 ▼
      Enterprise Document Loader
                 │
                 ▼
        Smart Text Chunking
                 │
                 ▼
    SentenceTransformer Embeddings
                 │
                 ▼
      FAISS Vector Database
                 │
                 ▼
      Enterprise Retrieval Service
                 │
                 ▼
          Semantic Search Results
```

Architecture Diagram:

```
docs/week12-vector-rag-platform-architecture.png
```

---

# Project Structure

```
week12-vector-rag-platform/

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
├── requirements.txt
├── .dockerignore
└── README.md
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| AI Embeddings | SentenceTransformers |
| Vector Database | FAISS |
| AI Framework | LangChain |
| Workflow Design | Enterprise Services |
| Testing | Pytest |
| Containerization | Docker |
| Documentation | Markdown |

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Platform

```bash
python app.py
```

Example Output

```
========================================
 Enterprise Semantic Search Platform
========================================

Documents Loaded : 1
Chunks Created   : 4

Building Embeddings...
Embeddings Created Successfully.
FAISS Vector Store Ready.

Semantic Search Results...
```

---

# Docker

Build the Docker image

```bash
docker build -t week12-vector-rag-platform .
```

Run the container

```bash
docker run week12-vector-rag-platform
```

---

# Testing

Execute the automated tests

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

# Screenshots

| Screenshot | Description |
|------------|-------------|
| 01-week12-project-structure.png | Enterprise project structure |
| 02-week12-document-ingestion-success.png | Document loading & smart chunking |
| 03-week12-faiss-semantic-search-success.png | FAISS semantic retrieval |
| 04-week12-semantic-retrieval-tests-passing.png | Automated testing |
| 05-week12-enterprise-semantic-search-platform.png | Complete semantic search platform |
| 08-week12-docker-success.png | Docker image build |
| 09-week12-all-tests-passing.png | Final platform verification |

---

# Skills Demonstrated

This project demonstrates practical experience with:

- Enterprise Retrieval-Augmented Generation (RAG)
- Semantic Search
- Sentence Embeddings
- Vector Databases
- FAISS
- Intelligent Document Retrieval
- AI Knowledge Systems
- Docker
- Automated Testing
- Enterprise Software Architecture

---

# Learning Outcomes

By completing this project I learned how to:

- Load enterprise knowledge documents
- Build smart document chunking pipelines
- Generate sentence embeddings
- Build FAISS vector indexes
- Perform semantic similarity search
- Design reusable retrieval services
- Build enterprise AI pipelines
- Dockerize AI applications
- Write automated tests
- Produce professional AI engineering documentation

---

# Future Improvements

Future enterprise upgrades include:

- Hybrid Search (BM25 + Vector Search)
- Metadata Filtering
- Overlapping Chunking
- Semantic Chunking
- ChromaDB
- PostgreSQL pgvector
- Pinecone
- Weaviate
- Milvus
- Enterprise Retrieval APIs
- LLM-powered Answer Generation

---

# Portfolio Progress

```
Week 1  → AI Summarizer
Week 2  → FastAPI AI API
Week 3  → Docker AI Deployment
Week 4  → AI Microservices
Week 5  → AI Production Platform
Week 6  → Enterprise APIs
Week 7  → Enterprise AI Services
Week 8  → Enterprise AI Architecture
Week 9  → Enterprise Workflow Platform
Week 10 → Enterprise Multi-Agent Platform
Week 11 → Enterprise Memory & RAG Platform
Week 12 → Enterprise Vector Databases & Semantic Search Platform
```

---

# Author

## Mike Nzirainengwe

**LLM Engineer | AI Platform Engineer | AI Infrastructure Engineer | AI Solutions Architect (in progress)**

Building production-grade Enterprise AI systems with a long-term mission of developing **MedNavi AI**, an enterprise healthcare AI platform for intelligent clinical documentation, Retrieval-Augmented Generation, workflow automation, and multilingual medical assistance.

---

**Week 12 Complete ✅**