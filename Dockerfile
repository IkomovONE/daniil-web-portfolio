# Use a multi-stage build

# Stage 1: Build Backend
FROM python:3.10 AS backend

# Set working directory for the backend
WORKDIR /app/backend

# Copy the requirements file and install dependencies
COPY back-end/requirements.txt .  # Copy requirements.txt to /app/backend
RUN pip install -r requirements.txt

# Copy all backend files (including main.py)
COPY back-end/ .  # Copy everything from back-end to /app/backend

# Stage 2: Build Frontend
FROM node:14 AS frontend

# Set working directory for the frontend
WORKDIR /app/frontend

# Copy the package.json file and install dependencies
COPY front-end/package.json .  # Copy package.json to /app/frontend/
RUN npm install

# Copy all frontend files
COPY front-end/ .  # Copy everything from front-end to /app/frontend/

# Final Stage: Combine both applications
FROM python:3.10

# Copy backend files
COPY --from=backend /app/backend /app/backend

# Copy frontend files
COPY --from=frontend /app/frontend /app/frontend

# Set working directory to the backend
WORKDIR /app/backend

# Expose the ports (ensure these are the correct ports)
EXPOSE 8000 3000

# Start the backend application (adjust as necessary)
CMD ["python", "main.py"]  # Updated to point directly to main.py