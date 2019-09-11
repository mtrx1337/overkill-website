FROM alpine

EXPOSE 9000

RUN mkdir -p /var/www
RUN mkdir -p /srv/http

VOLUME /var/www
WORKDIR /srv/http

COPY ./src .

RUN apk add --no-cache \
        uwsgi-python3 \
        python3

RUN pip3 install -r requirements.txt

CMD "uwsgi", "--socket", "0.0.0.0:9000", \
             "--uid", "uwsgi", \
             "--plugins", "python3" \
             "--protocol", "uwsgi", \
             "--wsgi", "main:application"
