# Use lightweight Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (Docker cache optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose application port
EXPOSE 80

# Run the Flask application
CMD ["python", "main.py"]
