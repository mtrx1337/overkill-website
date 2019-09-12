FROM alpine

EXPOSE 9000

RUN mkdir -p /var/www
RUN mkdir -p /srv/http

VOLUME /var/www
WORKDIR /srv/http

COPY ./src .
COPY ./requirements.txt .

ENV UWSGI_PROFILE=core
RUN apk add --no-cache \
        python3 \
        python3-dev \
        linux-headers \
        pcre-dev \
        musl \
        musl-dev \
        build-base \
        uwsgi-python3

RUN pip3 install -r requirements.txt

CMD ["uwsgi", "app.ini"]
