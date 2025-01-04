# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the PYTHONPATH to include the src directory
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y libsndfile1
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]