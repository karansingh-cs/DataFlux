# Base image — official Python 3.11 on lightweight Linux
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (so Docker caches this layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python files into the container
COPY . .

# Default command — overridden by docker-compose
CMD ["python", "logger.py"]