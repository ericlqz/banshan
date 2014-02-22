#!/bin/sh
./env/bin/uwsgi -s /tmp/uwsgi.sock -w entrance -H ./env/ --chmod-socket=666
