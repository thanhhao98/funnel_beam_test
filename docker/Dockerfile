FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./swagger_server /usr/src/app/swagger_server

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]