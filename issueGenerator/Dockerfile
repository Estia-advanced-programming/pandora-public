# Container image that runs your code
FROM python:3-alpine

# Copy source folder
COPY Main/Main.py ./Main/Main.py
# Copy ressources folder
COPY Resources/Data.py ./Resources/Data.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT [ "python" ]
