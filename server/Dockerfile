# grab the lastest python version
FROM python:latest

# must import the 'server.py' and 'index.html' file.
ADD server.py /server/

ADD requirements.txt .

# install pip requirements (and pass the flag to hide the warning for installing packages as root user)
RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install -r requirements.txt --root-user-action=ignore

# change base dir to /server
WORKDIR /server/
