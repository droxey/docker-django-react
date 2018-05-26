docker-compose down && \
docker volume rm django-docker-react_pgdata && \
docker volume rm django-docker-react_backend && \
docker volume rm django-docker-react_frontend && \
docker-compose up --build --quiet-pull --abort-on-container-exit
