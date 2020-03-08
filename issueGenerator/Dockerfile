# Container image that runs your code
FROM python:3-alpine

# Copy source folder
ADD Main /Main
# Copy ressources folder
ADD Ressources /Ressources

RUN pip install pystrich

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT [ "python", "./Main/Main.py" ]
