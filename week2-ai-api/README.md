# 🤖 Week 2 – AI Summarizer API

A REST API that summarizes text using Hugging Face Transformers and FastAPI.

## 🚀 Features

- AI-powered text summarization
- FastAPI REST API
- Interactive Swagger documentation
- JSON request and response
- Built with Python 3.13

## 🛠️ Technologies

- Python 3.13
- FastAPI
- Hugging Face Transformers
- PyTorch
- Uvicorn
- Pydantic

## 📂 Project Structure

week2-ai-api/
├── app.py
├── summarizer.py
├── requirements.txt
└── README.md

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

## 🎯 Learning Objectives

This project demonstrates:

- Building REST APIs with FastAPI
- Integrating AI models
- Working with JSON
- API documentation using Swagger
- Deploying AI models through web services

---

Developed by **Mike Nzirainengwe**