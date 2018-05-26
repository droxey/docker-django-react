#!/usr/bin/bash

cd /code/backend
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

exec "$@"
