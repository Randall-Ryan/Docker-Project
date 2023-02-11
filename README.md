# Randy Client/Server Docker Project

## This is a personal project demonstating a simple client/server connection setup with docker

### Step 1: Clone this repo and open project:

#### $ git clone https://github.com/Randall-Ryan/Docker-Project.git

#### $ cd Docker-Project/

### Step 2: Create two env files:

#### $ touch .client.env

```
export CLIENT_SECRET_HOST="xx"

export CLIENT_SECRET_PORT="xx"
```

#### $ touch .server.env

```
export SERVER_SECRET_PORT="xx"
```

### Step 3: run the following commands:

##### $ chmod u+x run_docker_compose.sh

##### $ ./run_docker_compose.sh
