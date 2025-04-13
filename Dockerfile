FROM python:3.10-slim

# Install build tools and MariaDB development libraries
RUN apt-get update && apt-get install -y build-essential libmariadb-dev && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first for caching purposes
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . /app

# Expose port 8000 for the application
EXPOSE 8000

# Run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
