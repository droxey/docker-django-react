FROM python:3.6.5-stretch

# -- Set environment variables required for setup on any machine.
ENV DJANGO_SETTINGS_MODULE "core.local_settings"
ENV PYTHONUNBUFFERED 1
ENV PGAPPNAME dr_backend
# ---- Set to non-null value to disable warnings when running `apt-get` commands.
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE "true"

# -- Install Postgres10 in order to use the `psql` client.
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN apt-get -qq update
RUN apt-get install -y postgresql-client-10 --show-progress

# -- Copy this directory to the `/code` folder in the Docker container,
# -- then change directories to `/code` in the Docker container.
COPY . /code
WORKDIR /code

# -- Install Python dependencies.
RUN /bin/bash -c "rm Pipfile.lock"
RUN /bin/bash -c "pip install --upgrade pip"
RUN /bin/bash -c "pip install pipenv"
RUN /bin/bash -c "pipenv install --system --skip-lock"

# -- Change WORKDIR to ensure `manage.py` commands run in context via `docker-compose.yml`.
WORKDIR /code/backend
