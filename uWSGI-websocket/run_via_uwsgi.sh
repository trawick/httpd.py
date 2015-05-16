#!/usr/bin/env bash
VENV=/home/trawick/envs/httpd.py
# gevent parameter needed to support more than one websocket
# thread (i.e., set up gevent)
${VENV}/bin/uwsgi --http-socket :3007 \
  --http-raw-body \
  --gevent 4 \
  --wsgi-file app.py \
  --chdir /home/trawick/git/httpd.py/uWSGI-websocket
