import socketserver
import os
import logging
import random

_logger = logging.getLogger(__name__)

# get the port
port = int(os.environ["SERVER_SECRET_PORT"])


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Request handler class for server
    """

    def handle(self):
        """
        Takes a client input int and returns a random int between 0-10 back to the client
        """
        _logger.debug("Handling client request for calculating a random num")

        # 'self.request' here is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # get the data passed from the client, type cast it to an int
        client_num = int(self.data)

        # calculate a random num between 0 and client provided num
        random_num = random.randint(0, client_num)

        # send the random num back to the client
        self.request.sendall(str(random_num).encode())


if __name__ == "__main__":
    # start the server with the given port
    with socketserver.TCPServer(("", port), MyTCPHandler) as server:
        # keeps server running/waits for requests from client
        server.serve_forever()
