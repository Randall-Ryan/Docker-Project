import urllib.request
import os
import logging

_logger = logging.getLogger(__name__)


# get the connection url defined in the env file
connection_url = os.environ["CLIENT_SECRET_URL"]
_logger.critical("Client connecting to server")
fp = urllib.request.urlopen(connection_url)

# decode content for hooman to read
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# print decoded server content
print(f"Decoded server content: {decodedContent}")

# close server connection
fp.close()
