#!/bin/bash
# wait-for-postgres.sh
#
# Waits for a successful PostgreSQL connection, then executes another command upon connection.
# Always runs Django migrations upon successful connection.
# Uses environment variables set in .env.

set -e
cmd="$@"

until PGPASSWORD=$DB_PASSWORD psql -v ON_ERROR_STOP=1 --host "$DB_HOST" --port "$DB_PORT" --username "$DB_USER" --password "$PGPASSWORD" --dbname "$DB_NAME" -c '\q'; do
  >&2 echo "[PSQL::WAITING] Listening via $DB_USER@$DB_HOST:$DB_PORT/$DB_NAME"
  sleep 3
done

>&2 echo "[PSQL::SUCCESS] Connected via $DB_USER@$DB_HOST:$DB_PORT/$DB_NAME"
exec $cmd
