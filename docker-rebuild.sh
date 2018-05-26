docker-compose down && \
docker volume rm docker-django-react_pgdata && \
docker volume rm docker-django-react_frontend && \
docker volume rm docker-django-react_backend && \
rm -rf frontend/cache && \
rm -rf frontend/node_modules && \
rm -rf frontend/build && \
docker-compose up --build --quiet-pull --abort-on-container-exit --force-recreate
