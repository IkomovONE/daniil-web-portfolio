# Use a multi-stage build
# Stage 1: Build Backend
FROM python:3.10 AS backend

WORKDIR /app/backend

COPY back-end/requirements.txt .
RUN pip install -r requirements.txt

COPY back-end/ .

# Stage 2: Build Frontend
FROM node:14 AS frontend

WORKDIR /app/frontend

COPY front-end/package.json .
RUN npm install

COPY front-end/ .

# Final Stage: Combine both applications
FROM python:3.10

# Copy backend files
COPY --from=backend /app/backend /app/backend

# Copy frontend files
COPY --from=frontend /app/frontend /app/frontend

# Set working directory
WORKDIR /app/backend

# Expose the ports
EXPOSE 8000 3000

# Start commands for backend and frontend (adjust as necessary)
CMD ["python", "app/main.py"]  # Adjust to your back-end start command
# For front-end, you may need to run a command like `npm start` 
# You might want to handle the front-end separately, e.g., using a reverse proxy like Nginx, or serve it through the back-end.