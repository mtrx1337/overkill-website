FROM alpine

RUN mkdir -p /code
RUN mkdir -p /sock # uwsgi socket
RUN mkdir -p /var/www

COPY ./config/mime.types /etc
COPY ./deployment/docker/docker-entry.sh /
COPY ./src /code
COPY ./requirements.txt /code

RUN apk add --no-cache \
        python3 \
        python3-dev \
        linux-headers \
        pcre-dev \
        musl \
        musl-dev \
        build-base

RUN pip3 install -r /code/requirements.txt uwsgi

EXPOSE 8000

CMD ["/bin/sh", "/docker-entry.sh"]
