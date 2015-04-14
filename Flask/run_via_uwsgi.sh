#!/usr/bin/env bash
VENV=/home/trawick/envs/httpd.py
${VENV}/bin/uwsgi --scgi-socket 127.0.0.1:3005 --wsgi-file app.py --callable app --chdir /home/trawick/git/httpd.py/Flask --virtualenv ${VENV}
