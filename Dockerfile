# Use a stable Python 3.9 base image
FROM python:3.9-bullseye

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install necessary system dependencies including Qt and X11 for OpenCV
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libx11-dev \
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libxcb-xinerama0-dev \
    libqt5gui5 \
    libqt5core5a \
    libqt5dbus5 \
    libx11-xcb-dev && \
    rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3 -m venv /env

# Upgrade pip
RUN /env/bin/pip install --upgrade pip

# Install Python dependencies inside the virtual environment
RUN /env/bin/pip install -r requirements.txt

# Set environment variable to use the virtual environment
ENV PATH="/env/bin:$PATH"

# Expose port (if needed)
EXPOSE 8080

# Run the application inside the virtual environment
CMD ["python", "body-dector.py"]
