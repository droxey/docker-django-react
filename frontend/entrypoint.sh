#!/usr/bin/bash
cd /code/frontend/src
chown node:node -R .
yarn install --non-interactive
yarn build
yarn start
