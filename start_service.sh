#!/bin/sh
source venv/bin/activate
test=`which python`
echo ${test}
echo `pwd`
pip install -r requirements.txt
#export FLASK_APP=server.py
#python -m flask run --host=0.0.0.0
gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi -m 007 --timeout 300
