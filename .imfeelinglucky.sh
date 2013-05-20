#!/bin/bash
virtualenv-2.7 --no-site-packages -p `which python2.7` .
. bin/activate
ln -s profiles/development.cfg buildout.cfg
./bin/python2.7 bootstrap.py
./bin/buildout
