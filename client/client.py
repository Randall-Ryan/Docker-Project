import socket
import os
import logging


logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

# get the host/port defined in the env file
host = os.environ["CLIENT_SECRET_HOST"]

# expected to be an int
port = int(os.environ["CLIENT_SECRET_PORT"])


class Client:
    def __init__(self, id, name, number):
        self.id = id
        self.name = name
        self.number = number
        self.random_number = None

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            _logger.debug("Client connecting to server")

            # connect & send data to server
            sock.connect((host, port))
            sock.sendall(bytes(f"{self.id},{self.name},{self.number} \n", "utf-8"))

            # receive data back from the server and shut down close server connection and set the random num
            self.random_number = int(str(sock.recv(1024), "utf-8"))


if __name__ == "__main__":
    # create two separate client connections
    client_1 = Client("1", "Randy", "56")
    _logger.debug(
        f"{client_1.name}: {client_1.number} (input) -> {client_1.random_number} (output)"
    )
    client_2 = Client("2", "Ryan", "5656")
    _logger.debug(
        f"{client_2.name}: {client_2.number} (input) -> {client_2.random_number} (output)"
    )
