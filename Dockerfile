# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file first (for dependency caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy all code folders and key files to container
COPY api/ ./api/
COPY config/ ./config/
COPY model/ ./model/
COPY schema/ ./schema/
COPY app.py .
COPY model.pkl .
COPY patients.json .

# Expose default FastAPI port
EXPOSE 8000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Start FastAPI API app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
