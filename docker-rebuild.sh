set -e

if [ $(docker-compose down) ]
then
  exec $(docker-compose down)
fi

DANGLING_VOLUMES="$(docker volume ls -qf dangling=true)"
if [ ${#DANGLING_VOLUMES} -gt 0 ]
then
  exec $(docker volume rm docker volume ls -qf dangling=true)
fi

exec docker-compose up --build
