#!/usr/bin/bash

echo "[REACT] Starting $NODE_ENV server."
yarn install --non-interactive

if [ ! -d /code/frontend/build ] && [ $NODE_ENV = 'production' ]; then
    echo "[BUILD] Failed to detect build folder. Running yarn build..."
    cd /code/frontend/src
    yarn build --production
fi

yarn start
exec "$@"
