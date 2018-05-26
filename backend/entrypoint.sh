#!/usr/bin/bash

cd /code/backend
python manage.py migrate --noinput --verbosity 0
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver 0.0.0.0:8000 --verbosity 0

exec "$@"
