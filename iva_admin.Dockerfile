FROM python:3.11.0-alpine3.16

WORKDIR /app

COPY iva_admin/reqs.txt /app
COPY iva_admin/main.py /app

RUN apk update; apk upgrade -y;  pip install -r reqs.txt

EXPOSE 8003/tcp

CMD flask run main:app --reload -h 0.0.0.0 -p 8003