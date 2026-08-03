# Use official Python image
FROM python:3.13-slim

# Working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install fastapi uvicorn

# Expose FastAPI port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]