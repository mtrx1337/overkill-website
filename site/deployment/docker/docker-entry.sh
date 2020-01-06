uwsgi \
    -s /tmp/site.sock \
    --manage-script-name \
    --mount /=app:app \
    --plugin http,python3 \
    #--virtualenv /code/venv \
    --check-static /code/src/static
