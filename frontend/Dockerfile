FROM node:6.9.5

# -- Create /code/frontend directory and add /frontend to it.
WORKDIR /code/frontend
ADD . /code/frontend
RUN mkdir /code/frontend/cache

# -- Set appropriate node permissions on /frontend.
RUN chown node:node -R .

# -- Install yarn, set cache folder, install node_modules, and cleanup.
RUN npm install -g -s --no-progress yarn && \
    yarn config set cache-folder /code/frontend/cache && \
    yarn install --silent --non-interactive && \
    yarn cache clean
