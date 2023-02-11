# Randy Client/Server Docker Project

### This is a personal project demonstrating a simple client/server socket connection using docker. The project contains postgres and metabase services with some very basic SQL functionality between the client & server. TODO: Setup a deployement with kubernetes

## Step 1: Clone this repo and open the project:

### $ git clone https://github.com/Randall-Ryan/Docker-Project.git

### $ cd Docker-Project/

## Step 2: Create four seperate env files with their respective variables:

### $ touch .client.env

```
export CLIENT_SECRET_HOST="x"

export CLIENT_SECRET_PORT="x"
```

### $ touch .server.env

```
export SERVER_SECRET_PORT="x"

export SERVER_SECRET_DBHOST="x"

export SERVER_SECRET_DBNAME="x"

export SERVER_SECRET_DBUSER="x"

export SERVER_SECRET_DBPASS="x"
```

### $ touch .metabase.env

```
export MB_DB_TYPE="x"

export MB_DB_DBNAME="x"

export MB_DB_PORT="x"

export MB_DB_USER="x"

export MB_DB_PASS="x"

export MB_DB_HOST="x"

export MB_DB_FILE="x"
```

### $ touch .postgres.env

```
export POSTGRES_DB="x"

export POSTGRES_USER="x"

export POSTGRES_PASSWORD="x"
```

## Step 3: Run the following commands:

### $ chmod u+x run_docker_compose.sh

### $ ./run_docker_compose.sh
