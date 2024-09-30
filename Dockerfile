# Use a multi-stage build

# Stage 1: Build Backend
FROM python:3.10 AS backend

# Set working directory for the backend
WORKDIR /app/backend

# Copy the requirements file and install dependencies
COPY back-end/requirements.txt .
RUN pip install -r requirements.txt

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
COPY front-end/package.json .

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
CMD ["python", "main.py"] 