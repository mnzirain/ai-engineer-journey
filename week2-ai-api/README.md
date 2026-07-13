# 🤖 Mike's AI Summarizer API

An AI-powered REST API built with **FastAPI** and **Hugging Face Transformers** that summarizes long pieces of text into concise summaries.

This project demonstrates how to integrate a Large Language Model (LLM) into a production-style REST API with:

- Request validation
- Professional error handling
- Logging
- Automated testing
- Interactive API documentation

## 🚀 Features

- AI-powered text summarization
- FastAPI REST API
- Interactive Swagger documentation
- JSON request and response
- Request validation
- Professional error handling
- Request logging
- Health check endpoint
- Automated unit tests

## 🛠️ Technologies

- Python 3.13
- FastAPI
- Hugging Face Transformers
- PyTorch
- Uvicorn
- Pydantic

## 🏗️ Architecture

```text
                User
                  │
                  ▼
        FastAPI REST API
          (app.py)
                  │
                  ▼
      Summarization Service
       (summarizer.py)
                  │
                  ▼
 Hugging Face Transformer Model
 (sshleifer/distilbart-cnn-12-6)
                  │
                  ▼
          JSON Response
```

## 📂 Project Structure

```text
week2-ai-api/
│
├── app.py               # FastAPI application
├── summarizer.py        # AI summarization logic
├── test_api.py          # Automated API tests
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── __pycache__/         # Python cache (auto-generated)
```

## ▶️ Run the Project

Activate the virtual environment:

```bash
source .venv313/Scripts/activate
```

Start the server:

```bash
uvicorn app:app --reload
```

Open:

http://127.0.0.1:8000/docs

## 📮 API Endpoint

POST /summarize

Example request:

```json
{
  "text": "Artificial intelligence is transforming industries..."
}
```

Example response:

```json
{
  "summary": "AI is transforming industries by improving productivity."
}
```

## 🧪 Running the Tests

Run the automated tests with:

```bash
pytest
```

Expected output:

```text
========================
2 passed
========================
```

## 🎯 Learning Objectives

This project demonstrates:

- Building REST APIs with FastAPI
- Integrating AI models
- Working with JSON
- API documentation using Swagger
- Deploying AI models through web services

---

Developed by **Mike Nzirainengwe**