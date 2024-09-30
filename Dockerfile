# Stage 1: Build Backend
FROM python:3.11.10 AS backend

# Set working directory for the backend
WORKDIR /app/backend

# Install virtual environment package
RUN python -m venv venv

# Activate the virtual environment and install dependencies
COPY back-end/requirements.txt .
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copy all backend files (including main.py)
COPY back-end/ .

# Stage 2: Build Frontend
FROM node:14 AS frontend

# Set working directory for the frontend
WORKDIR /app/frontend

# Copy the package.json file and install dependencies
COPY front-end/package.json .
RUN npm install

# Copy all frontend files
COPY front-end/ .

# Final Stage: Combine both applications
FROM python:3.11.10

# Set working directory for the combined build
WORKDIR /app/backend

# Copy backend files from the backend stage
COPY --from=backend /app/backend /app/backend

# Copy frontend files from the frontend stage
COPY --from=frontend /app/frontend /app/frontend

# Activate the virtual environment
ENV PATH="/app/backend/venv/bin:$PATH"

# Expose the ports (ensure these are the correct ports)
EXPOSE 10000 8000

# Start the backend application (adjust as necessary)
CMD ["python", "main.py"]