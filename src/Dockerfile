FROM python:3.11-alpine

LABEL org.opencontainers.image.source="https://github.com/smashedr/docker-test-action"
LABEL org.opencontainers.image.description="Docker Test Action"
LABEL org.opencontainers.image.authors="smashedr"

COPY requirements.txt /
RUN python -m pip install -Ur requirements.txt

COPY . /src
ENTRYPOINT ["python", "/src/main.py"]
