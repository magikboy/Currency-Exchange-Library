# Supply Chain Backdoor Simulation Environment
# This Dockerfile creates a controlled environment for educational/research purposes
# to simulate supply chain vulnerabilities in a Python project

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    nano \
    vim \
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for security
RUN useradd -m -s /bin/bash simuser && \
    chown -R simuser:simuser /app

# Copy the base application files
COPY currency_exchange.py /app/
COPY main.py /app/
COPY README.md /app/
COPY LICENSE /app/

# Set up Python environment
RUN pip install --no-cache-dir --upgrade pip

# Copy and install requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Create a requirements file for potential dependencies
RUN echo "# Base requirements for currency exchange library" > requirements.txt && \
    echo "# Additional packages may be added for simulation components" >> requirements.txt

# Set proper permissions
RUN chown -R simuser:simuser /app

# Switch to non-root user
USER simuser

# Set environment variables for the simulation
ENV PYTHONPATH=/app
ENV SIMULATION_MODE=true
ENV CONTAINER_ENV=true

# Expose port for potential web interface or monitoring
EXPOSE 8080

# Default command - runs main.py to demonstrate normal library usage
CMD ["python", "main.py"]

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import currency_exchange; print('Health check passed')" || exit 1

# Labels for documentation
LABEL maintainer="simulation-env" \
      description="Controlled environment for supply chain backdoor simulation" \
      version="1.0" \
      security.purpose="educational-research-only" \
      environment="isolated-container"
