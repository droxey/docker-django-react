FROM node:9

# -- Set env vars for setup.
ENV NPM_CONFIG_LOGLEVEL warn
ENV NODE_ENV=production PORT=3000


# -- Create /code/frontend directory and add /frontend to it.
RUN mkdir -p /code/frontend/cache
WORKDIR /code/frontend

# -- The port our React app is running on.
EXPOSE $PORT

# -- Add our node_modules to $PATH.
ENV PATH /code/frontend/node_modules/.bin:$PATH

# -- Copy and shrinkwrap dependencies.
COPY package.json /code/frontend/package.json
COPY npm-shrinkwrap.json /code/frontend/npm-shrinkwrap.json

# -- Install yarn, set cache folder, install node_modules, and cleanup.
RUN npm install --no-progress --production
RUN yarn config set cache-folder /code/frontend/cache
RUN yarn cache clean

# -- Add frontend React app.
ADD . /code/frontend
