import socket
import os
import logging

_logger = logging.getLogger(__name__)

# get the host/port defined in the env file
host = os.environ["CLIENT_SECRET_HOST"]

# expected to be an int
port = int(os.environ["CLIENT_SECRET_PORT"])

# hardcoded input value
input = "56"

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        _logger.debug("Client connecting to server")

        # connect & send data to server
        sock.connect((host, port))
        sock.sendall(bytes(input + "\n", "utf-8"))

        # receive data back from the server and shut down close server connection
        received = str(sock.recv(1024), "utf-8")

    _logger.debug(f"Random num between 0 and input ({input}): {received}")
