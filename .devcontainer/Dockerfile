# .devcontainer/Dockerfile

FROM ubuntu:22.04

# Install Python and common packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev git curl && \
    apt-get install -y build-essential libssl-dev libffi-dev && \
    apt-get install -y python3-venv

# Set default Python
RUN ln -sf python3 /usr/bin/python

# Install Python packages
COPY ../api/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

WORKDIR /workspace

