# Use full Ubuntu-based Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV GOOGLE_API_KEY=your_api_key

# Expose port
EXPOSE 3000

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
