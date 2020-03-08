# Container image that runs your code
FROM python:3-alpine

# Copy source folder
ADD Main /Main
# Copy ressources folder
ADD Resources /Resources
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT [ "python" ]
