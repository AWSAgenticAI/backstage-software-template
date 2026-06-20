# Use an official, lightweight Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file first to leverage Docker caching
COPY requirements.txt .

# Install all required Python libraries cleanly
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code from /app to the container
COPY ./src .

# EXPOSE the port your Python app listens on (e.g., 5000 for Flask, 8000 for FastAPI)
EXPOSE 5000
# The command to execute your application when the container starts
CMD ["python", "app.py"]
