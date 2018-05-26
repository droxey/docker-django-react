#!/usr/bin/bash
cd /code/frontend/src
chown node:node -R .
yarn install
yarn start
