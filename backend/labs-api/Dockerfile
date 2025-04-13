# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Expose the port that Django runs on
EXPOSE 8000

# Run Django server (or use gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
