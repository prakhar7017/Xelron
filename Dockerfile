FROM ubuntu:22.04

# Avoid prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    gdb \
    valgrind \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up workspace
WORKDIR /workspace

# Copy all task files
COPY . /workspace/

# Make run-tests.sh executable
RUN chmod +x /workspace/run-tests.sh

# Default command
CMD ["/bin/bash"]
