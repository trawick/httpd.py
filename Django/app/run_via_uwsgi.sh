#!/usr/bin/env bash
/home/trawick/envs/httpd.py/bin/uwsgi --scgi-socket 127.0.0.1:3006 --wsgi-file app.py --module app.wsgi --chdir /home/trawick/git/httpd.py/Django/app --virtualenv /home/trawick/envs/httpd.py
