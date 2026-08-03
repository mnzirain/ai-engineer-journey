# 📚 Week 3 – AI Document Chat (RAG)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-009688?logo=fastapi)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![SentenceTransformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-red)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FLAN--T5-yellow?logo=huggingface)
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-success)

An AI-powered Retrieval-Augmented Generation (RAG) chatbot capable of indexing PDF documents, performing semantic search with vector embeddings, and generating context-aware answers using a Large Language Model (LLM).

---

## 📸 Demo

### Swagger API

![Swagger API](screenshots/swagger-home.png)

The project exposes a REST API built with FastAPI. Interactive API documentation is available through Swagger UI.

---

### Upload PDF

![Upload PDF](screenshots/upload-api.png)

Users can upload one or more PDF documents, which are automatically processed into searchable chunks and indexed using FAISS.

---

### Ask Questions

![RAG Answer](screenshots/rag-answer.png)

Questions are answered using Retrieval-Augmented Generation (RAG). The application retrieves the most relevant document chunks before generating a grounded response using Google FLAN-T5.

---

---

# 🏗️ System Architecture

The RAG chatbot follows a modular Retrieval-Augmented Generation (RAG) architecture.

![RAG Architecture](architecture/rag-architecture.png)

### Architecture Flow

1. User submits a question through the FastAPI REST API.
2. The RAG Engine converts the question into an embedding.
3. FAISS performs semantic similarity search.
4. The most relevant document chunks are retrieved.
5. A prompt is constructed using the retrieved context.
6. The LLM generates a grounded response.
7. The API returns both the answer and the document sources.

---

# ⚙️ Engineering Highlights

This project demonstrates production-oriented AI engineering practices:

- Modular architecture
- Separation of Retrieval and Generation
- Vector Search using FAISS
- Embedding generation using SentenceTransformers
- Prompt engineering
- REST API design with FastAPI
- Source attribution
- Professional Git workflow
- Project documentation

# 💼 Key Skills Demonstrated

This project demonstrates practical AI Engineering skills including:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases (FAISS)
- Sentence Embeddings
- Prompt Engineering
- Large Language Models (FLAN-T5)
- FastAPI REST APIs
- PDF Processing
- Python Software Engineering
- Git & GitHub Workflow
- Debugging & Production Readiness

## 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into searchable chunks
- Generate vector embeddings
- Store embeddings in a vector database
- Retrieve relevant information using semantic search
- Answer user questions using an LLM
- REST API built with FastAPI
- Interactive Swagger documentation
- Docker support
- Unit testing with pytest

---

## 🛠️ Technologies

- Python 3.13
- FastAPI
- LangChain
- FAISS Vector Database
- Sentence Transformers
- Hugging Face Transformers
- PyPDF
- Docker
- Pytest

---

## 📂 Project Structure

```
week3-rag-chatbot/
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── test_rag.py
│
├── data/
├── documents/
└── vectorstore/
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Semantic Search
- Vector Databases
- Document Processing
- FastAPI APIs
- Docker
- AI Engineering Best Practices

---

# 🚀 Future Improvements

- Cloud Deployment (Azure / AWS)
- Docker Compose
- Streaming Responses
- Multiple LLM Support
- OpenAI Integration
- Llama 3 Support
- Mistral Support
- User Authentication
- Persistent Vector Database
- Conversation Memory
- Production Logging

---

---

## 👨‍💻 Author

**Mike Nzirainengwe**

AI Engineer | Generative AI | Retrieval-Augmented Generation (RAG) | FastAPI | Python | LLM Applications

GitHub:
https://github.com/mnzirain