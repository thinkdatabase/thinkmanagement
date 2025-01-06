# Use a lightweight Python image
FROM python:3.10-slim

# Install system dependencies for MySQL, pkg-config, and Python
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . .

# Expose the app on port 8080
EXPOSE 8080

# Run the Django app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "ThinkfoTechManagement.wsgi:application"]
