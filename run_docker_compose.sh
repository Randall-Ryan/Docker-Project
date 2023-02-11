#!/bin/bash


# remove the local data dir
sudo rm -rf db-data/

# re-build/run the docker services defined in docker-compose file
docker-compose down --volumes
docker-compose build
docker-compose up --renew-anon-volumes
