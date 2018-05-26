FROM node:latest

# -- Setup environment variables.
ENV DEBIAN_FRONTEND noninteractive

# -- Install bash.
RUN apt-get update && apt-get install bash
SHELL ["/bin/bash", "-c"]

# -- Change directories and copy frontend code.
WORKDIR /code/frontend
COPY . /code/frontend

# -- Install yarn, run npm install, yarn build, yarn prune, and clean yarn cache.
RUN npm install -g -s --no-progress yarn && \
    npm install --no-progress && \
    yarn build && \
    yarn cache clean

# -- Run `yarn start` to watch files in development.
CMD [ "yarn", "start" ]
