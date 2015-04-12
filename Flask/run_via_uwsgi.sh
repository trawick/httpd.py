#!/usr/bin/env bash
/home/trawick/envs/httpd.py/bin/uwsgi --scgi-socket 127.0.0.1:3005 --wsgi-file app.py --callable app --chdir /home/trawick/git/httpd.py/Flask --virtualenv /home/trawick/envs/httpd.py
