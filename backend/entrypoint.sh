#!/bin/sh
set -e  # Exit immediately if any command fails

# ---------------------------------------
# Wait for Postgres
# ---------------------------------------
echo "Waiting for Postgres..."
/wait-for-db.sh db 5432 -- echo "Postgres is up"

# ---------------------------------------
# Wait for Redis
# ---------------------------------------
REDIS_HOST=${REDIS_HOST:-redis}
REDIS_PORT=${REDIS_PORT:-6379}
echo "Waiting for Redis..."
/wait-for-db.sh $REDIS_HOST $REDIS_PORT -- echo "Redis is up"

# ---------------------------------------
# Create migrations for authentication app (fix the dependency error)
# ---------------------------------------
echo "Creating migrations for authentication app..."
# python manage.py makemigrations authentication --noinput

# ---------------------------------------
# Apply database migrations
# ---------------------------------------
echo "Applying database migrations..."
python manage.py migrate --noinput

# ---------------------------------------
# Collect static files
# ---------------------------------------
echo "Collecting static files..."
python manage.py collectstatic --noinput

# ---------------------------------------
# Start Celery Worker in background
# ---------------------------------------
echo "Starting Celery worker..."
celery -A shop worker -l info --detach

# ---------------------------------------
# Start Django with Gunicorn
# ---------------------------------------
echo "Starting Django Gunicorn server..."
exec gunicorn shop.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 2