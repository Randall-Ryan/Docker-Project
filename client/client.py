import socket
import os
import logging

_logger = logging.getLogger(__name__)

# get the host/port defined in the env file
host = os.environ["CLIENT_SECRET_HOST"]

# expected to be an int
port = int(os.environ["CLIENT_SECRET_PORT"])


class Client:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.random_number = None
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            _logger.critical("Client connecting to server")

            # connect & send data to server
            sock.connect((host, port))
            sock.sendall(bytes(self.number + "\n", "utf-8"))

            # receive data back from the server and shut down close server connection and set the random num
            self.random_number = int(str(sock.recv(1024), "utf-8"))


if __name__ == "__main__":
    # create two separate client connections
    client_1 = Client("Randy", "56")
    client_2 = Client("Ryan", "5656")

    _logger.critical(
        f"{client_1.name}: {client_1.random_number} (input) -> {client_1.random_number} (output)"
    )

    _logger.critical(
        f"{client_2.name}: {client_2.random_number} (input) -> {client_2.random_number} (output)"
    )
