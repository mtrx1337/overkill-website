FROM alpine

RUN apk add --no-cache \
        python3 \
        python3-dev \
        linux-headers \
        pcre-dev \
        musl \
        musl-dev \
        build-base \
        uwsgi \
        uwsgi-python

RUN mkdir -p /etc/nginx
RUN mkdir -p /code

COPY ./deployment/nginx/nginx.conf /etc/nginx
COPY . /code

EXPOSE 8000

CMD ["/bin/sh", "/code/deployment/docker/docker-entry.sh"]
