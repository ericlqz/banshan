#!/bin/sh
yaourt -S libevent
yaourt -S python2-webpy
yaourt -S mysql-python
pip2 install virtualenv
virtualenv ./env
source ./env/bin/activate
pip install uwsgi
deactivate
