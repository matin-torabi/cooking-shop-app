# pull official base image
FROM python:3.13.7-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



RUN pip install pipenv


# copy requirements first (for better caching)
COPY requirements.txt .

# install python dependencies

# --no-cache-dir
RUN pip install -r requirements.txt

# copy project code
COPY . .

# copy entrypoint scripts
COPY wait-for-db.sh entrypoint.sh /
RUN chmod +x /wait-for-db.sh /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]