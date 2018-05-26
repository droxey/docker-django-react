FROM node:latest

# -- Setup environment variables.
ENV DEBIAN_FRONTEND noninteractive

# -- Install bash.
RUN apt-get update && apt-get install bash
SHELL ["/bin/bash", "-c"]

# -- Change directories and copy frontend code.
WORKDIR /code/frontend
COPY . /code/frontend

# -- Install yarn.
RUN npm install -g -s --no-progress yarn
