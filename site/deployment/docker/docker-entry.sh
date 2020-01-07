uwsgi \
    -s /tmp/site.sock \
    --vacuum \
    --die-on-term \
    --enable-threads \
    --threads 4 \
    --python-path /code \
    --plugins-dir /usr/lib/uwsgi/ \
    --master \
    #--http 0.0.0.0:8000 \
    --manage-script-name \
    --mount /=app:app
    --uid = http \
    --gid = http
