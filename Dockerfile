
# Use Python 3.11 as base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /usr/src/app

# Prevent Python from writing bytecode files
ENV PYTHONDONTWRITEBYTECODE 1

# Ensure Python prints to stdout/stderr instantly
ENV PYTHONUNBUFFERED 1

# Set the port number for the application
ENV PORT 8000

# Copy current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies from requirements.txt without caching
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Command to run the application
CMD python manage.py runserver 0.0.0.0:$PORT
