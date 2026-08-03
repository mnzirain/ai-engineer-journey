# Use an official Python image
FROM python:3.13-slim

# Create a working directory
WORKDIR /app

# Copy dependency list first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# FastAPI runs on port 8000
EXPOSE 8000

# Start the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]