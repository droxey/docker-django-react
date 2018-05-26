#!/usr/bin/env sh
bash
cd /code/frontend/src
chown node:node -R .
yarn install
yarn start
