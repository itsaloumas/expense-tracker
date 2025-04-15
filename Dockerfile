FROM python:3.10-slim

# Install build tools and MariaDB dev libraries
RUN apt-get update && apt-get install -y build-essential libmariadb-dev && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container to /app (this will be the repository root)
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repository content into the container
COPY . /app

# Expose port 8000
EXPOSE 8000

# Default command runs the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]