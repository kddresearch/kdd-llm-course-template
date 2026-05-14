FROM python:3.13.0-alpine AS base

# Define working directory
# WORKDIR /app

# Copy requirements file
# COPY ./requirements.txt ./

# Install dependencies
# ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# RUN pip3 install -r requirements.txt

# Copy source code
# COPY . .

# Start the application
# CMD ["python", "app.py"]

CMD ["python", "-c", "print('Hello, World!')"]
