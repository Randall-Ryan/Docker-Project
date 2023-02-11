# Randy Client/Server Docker Project

### This is a personal project demonstating a simple client/server connection setup with docker-compose

## Step 1: Clone this repo and open project:

### $ git clone https://github.com/Randall-Ryan/Docker-Project.git

### $ cd Docker-Project/

## Step 2: Create two env files:

### $ touch .client.env

```
export CLIENT_SECRET_HOST="xx"

export CLIENT_SECRET_PORT="xx"
```

### $ touch .server.env

```
export SERVER_SECRET_PORT="xx"

export SERVER_SECRET_DBHOST="xx"

export SERVER_SECRET_DBNAME="xx"

export SERVER_SECRET_DBUSER="xx"

export SERVER_SECRET_DBPASS="xx"
```

### $ touch .metabase.env

```
export MB_DB_TYPE="xx"

export MB_DB_DBNAME="xx"

export MB_DB_PORT="xx"

export MB_DB_USER="xx"

export MB_DB_PASS="xx"

export MB_DB_HOST="xx"

export MB_DB_FILE="xx"
```

### $ touch .postgres.env

```
export POSTGRES_DB="xx"

export POSTGRES_USER="xx"

export POSTGRES_PASSWORD="xx"
```

## Step 3: Run the following commands:

### $ chmod u+x run_docker_compose.sh

### $ ./run_docker_compose.sh
