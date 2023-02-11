import http.server
import socketserver
import os
import logging

_logger = logging.getLogger(__name__)

# define handler for requests from client
handler = http.server.SimpleHTTPRequestHandler

# get the port
port = int(os.environ["SERVER_SECRET_PORT"])

# start the server with the given port
with socketserver.TCPServer(("", port), handler) as httpd:
    _logger.critical(f"Starting server running on port: {port}")
    # keeps the server running/waits for requests from client
    httpd.serve_forever()
