docker-compose down && \
docker volume rm docker-django-react_pgdata && \
docker volume rm docker-django-react_frontend && \
docker volume rm docker-django-react_backend && \
docker-compose up --build --quiet-pull --abort-on-container-exit
