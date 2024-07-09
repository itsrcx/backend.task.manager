# Use the official Python image from the Docker Hub
FROM python:3.10-bullseye

# Set environment variables to prevent Python from writing pyc files and to buffer stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gettext \
    && rm -rf /var/lib/apt/lists/*


# Updtae existing pip installation
RUN pip install --upgrade pip

# Create a non-root user
RUN adduser --disabled-login django

# add working directory
WORKDIR /home/django

# adding path for django user installed binaries
ENV PATH="/home/django/.local/bin:${PATH}"

# Switch to the non-root user
USER django

# Install Python dependencies as the non-root user
COPY --chown=django:django requirements.txt /home/django/
RUN pip install -r requirements.txt

COPY --chown=django:django . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
