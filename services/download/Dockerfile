FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    python3 \
    python3-pip \
    python3-venv

# Set up working directory
WORKDIR /app

# Copy necessary files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose necessary ports
EXPOSE 8080

# Command to run the service
CMD ["python3", "app.py"]