FROM python:3.11-alpine

COPY requirements.txt /
RUN python -m pip install -Ur requirements.txt

COPY . /src
ENTRYPOINT ["python", "/src/main.py"]
