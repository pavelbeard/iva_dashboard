FROM python:3.11.0-alpine3.16

WORKDIR /app

COPY server_mon/reqs.txt /app
COPY server_mon/main.py /app

RUN apk update; apk upgrade -y; pip install -r reqs.txt

EXPOSE 8000/tcp

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000