# Use Python 3.11 slim for a small footprint
FROM python:3.11-slim

# 1. Install system dependencies
# We include libpq-dev and gcc in case your utils use psycopg2-binary
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 2. Set working directory
WORKDIR /app

# 3. Install Python dependencies
# We copy requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY . .

# 5. Expose the FastAPI port
EXPOSE 8001

# 6. Run the application with hot-reload enabled for development
# Using 'app.main:app' assumes your FastAPI instance is in app/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]