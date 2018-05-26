# docker-django-react

Dockerized boilerplate. PostgreSQL 10 database + Django 2.0.x/DRF API backend + React frontend. Powered via proxy!

## Prerequisites

### Docker

1. Docker
1. docker-compose

## Installation

### Docker

1. Clone the repo: `git clone git@github.com:outputs-io/docker-django-react.git your-project-name`
1. Navigate to the repo directory created in the last step: `cd your-project-name`
1. Delete the leftover `.git` directory: `rm .git`. _Remember to `git init` and `git remote add origin <url>` when you're ready to add, commit, and push your code!_
1. Create a `.env` file by using `.env.sample` as a boilerplate: `cp .env.sample .env` Edit the new `.env` file and augment the variables to match your local environment.
1. Create a `backend/core/local_settings.py` file by using `backend/core/local_settings.py.sample` as a boilerplate: `cp backend/core/local_settings.py.sample backend/core/local_settings.py` Edit the new `backend/core/local_settings.py` file and augment the variables to match your local environment.
1. Execute `docker-compose up`.
1. Wait until the build finishes. You'll see this message: `dr_example_frontend | Compiled successfully!`
1. Open browser and access `http://localhost:8000` to access the frontend.
1. Use cURL in a new Terminal tab to test the backend Django API via DRF token authentication:
    ```bash
    $ curl -X POST -d "username=SUPERUSER_USERNAME&password=SUPERUSER_PASSWORD" http://localhost:8000/api/v1/auth/`
    {"token":"a66bfc378fc443f33953c99c3d852bace48094c2"}%
    ```
1. Write your fancy new Django + React app!

# Debugging Django via VSCode Remote Debugger

Add the following `launch.json` entry:

```json
  {
      "name": "Remote Django App",
      "type": "python",
      "request": "attach",
      "localRoot": "${workspaceRoot}",
      "remoteRoot": "/code/backend",
      "port": 8010,
      "secret": "debugger-local-secret",
      "host": "localhost"
  }
```
