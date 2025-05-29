FROM python:3.9-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED 1

# Copy requirements.txt FIRST to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app/

# Expose port for the Django development server
EXPOSE 8000

# Default command for the backend service (Django web server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]