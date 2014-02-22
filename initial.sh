#!/bin/sh
yaourt -S libevent
pip2 install virtualenv
virtualenv ./env
source ./env/bin/activate
pip install uwsgi
deactivate
