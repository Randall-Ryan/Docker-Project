import socketserver
import os
import logging
import random
import psycopg2
import pandas as pd

# set logger
logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

# set env vars
port = int(os.environ["SERVER_SECRET_PORT"])
db_host = os.environ["SERVER_SECRET_DBHOST"]
db_name = os.environ["SERVER_SECRET_DBNAME"]
db_user = os.environ["SERVER_SECRET_DBUSER"]
db_pass = os.environ["SERVER_SECRET_DBPASS"]


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Request handler class for server
    """

    def handle(self):
        """
        Handles a client request
        Parses info and creates a user in db with respective info
        returns a random int back to the client
        """
        _logger.debug("Handling random num calculation request")

        # TODO: rework this
        self.data = self.request.recv(1024).strip().decode("ascii")

        # do some parsing
        client_data = self.data.split(",")
        user_id = int(client_data[0])
        user_name = client_data[1]
        user_original_num = int(client_data[2])
        random_num = get_random_num(user_original_num)

        _logger.debug(f"Creating user {user_name}")
        # create the user with info passed from client
        create_user(user_id, user_original_num, random_num, user_name)

        # send the random num back to the client
        self.request.sendall(str(random_num).encode())


def get_random_num(num: int) -> int:
    """
    Takes in an int and returns a random int between 0 and num

    args:
        int: num
    returns:
        int: random num
    """
    return random.randint(0, num)


def create_user(id, o_num, r_num, name) -> None:
    """
    Makes a connection to the database in order to make execute queries
    Manually creates a test user in the db
    Closes db connection

    args:
        int: unique id of user, primary key in table
        int: original number
        int: random number
        str: name of user

    returns:
        None
    """
    # make db connection
    conn = psycopg2.connect(
        host=db_host, database=db_name, user=db_user, password=db_pass
    )
    cursor = conn.cursor()

    # add the user with all respective info
    cursor.execute(
        f"""
        INSERT INTO test_users (id, original_num, random_num, name)
        VALUES ({id}, {o_num}, {r_num}, '{name}');
        """
    )
    conn.commit()

    _logger.debug(f"Created user with id: {id}")

    # close db connection
    conn.close()
    cursor.close()


def create_tables(tables) -> None:
    """
    Makes a connection to the database in order to make execute queries
    Manually creates db tables
    Closes db connection

    args:
        list: a list of tables that should be created
            expected options:
                - test_users
                - test_animals
                - test_food
    returns:
        None
    """

    # make db connection
    conn = psycopg2.connect(
        host=db_host, database=db_name, user=db_user, password=db_pass
    )
    cursor = conn.cursor()

    # check if the table should be created
    if "test_users" in tables:
        # create the user table
        cursor.execute(
            "CREATE TABLE test_users (id serial PRIMARY KEY, original_num integer, random_num integer, name varchar);"
        )

    # TODO: implement animals
    # create a df of animals
    data = {"names": ["cow", "chicken", "sheep"], "ages": [10, 20, 30]}
    animals_df = pd.DataFrame(data)
    _logger.debug(animals_df)

    if "test_animals" in tables:
        # create the animal table
        cursor.execute(
            "CREATE TABLE test_animals (id serial PRIMARY KEY, age integer, description varchar, name varchar);"
        )
    if "test_food" in tables:
        # create the food table
        cursor.execute(
            "CREATE TABLE test_food (id serial PRIMARY KEY, calories integer, name varchar);"
        )

    # update db
    conn.commit()

    # close db connection
    conn.close()
    cursor.close()


if __name__ == "__main__":
    # start the server with the given port
    with socketserver.TCPServer(("", port), MyTCPHandler) as server:
        # hard coded list of the tables that should get created
        tables = ["test_users", "test_animals"]
        create_tables(tables)

        # keeps server running/waits for requests from client
        server.serve_forever()
