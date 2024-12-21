# Use an official Python image as the base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libnss3 \
    libnspr4 \
    libxss1 \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libxtst6 \
    libgdk-pixbuf2.0-0 \
    xdg-utils \
    libvulkan1 && \
    rm -rf /var/lib/apt/lists/*

# Install Google Chrome by downloading the .deb file
RUN wget -N https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    apt-get -y install -f && \
    rm google-chrome-stable_current_amd64.deb

# Install Python dependencies
RUN pip install chromedriver-autoinstaller selenium beautifulsoup4

# Set the working directory
WORKDIR /Help_AI_AGENT

# Copy the content into the container
COPY Help_AI_AGENT /Help_AI_AGENT

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Python script
ENTRYPOINT ["python", "/Help_AI_AGENT/main.py"]

