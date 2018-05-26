#!/usr/bin/env sh
bash
cd /code/backend
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000
