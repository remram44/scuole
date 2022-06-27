#!/bin/sh

set -o allexport
set -o nounset
set -o errexit
set -o xtrace

# Run postgis
/docker-entrypoint.sh postgres &

# Collect static files
python manage.py collectstatic --noinput

# Run app
python manage.py runserver 0.0.0.0:8000
