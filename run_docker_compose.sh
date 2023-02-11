#!/bin/bash

# simple script to re-build/run the docker services defined in docker-compose file
sudo rm -rf db-data/
docker-compose down --volumes
docker-compose build
docker-compose up --renew-anon-volumes
