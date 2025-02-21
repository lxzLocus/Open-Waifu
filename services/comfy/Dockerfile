
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip python3-venv git

# Set up working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the necessary port
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]