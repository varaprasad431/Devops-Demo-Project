# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application code to the container
COPY app.py /app

# Install Flask
RUN pip install flask

# Command to run the backend application
CMD ["python", "app.py"]

