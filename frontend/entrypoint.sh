#!/usr/bin/bash

yarn install --non-interactive
if [ ! -f /code/frontend/build ]; then
    echo "[BUILD] Failed to detect build folder. Running yarn build..."
    cd /code/frontend/src
    yarn build
fi
yarn start
exec "$@"
