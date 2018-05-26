#!/usr/bin/bash
cd /code/backend

python manage.py migrate --noinput --verbosity 0
python manage.py collectstatic --noinput --verbosity 0

if [ $USE_VSCODE_DEBUGGER = 1 ]; then
  python manage.py runserver 0.0.0.0:8000 --noreload --nothreading --verbosity 0
else
  python manage.py runserver 0.0.0.0:8000 --verbosity 0
fi

exec "$@"
