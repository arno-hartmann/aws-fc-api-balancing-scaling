#!/bin/bash

yum update -y

yum install -y python
yum install -y pip
pip3 install flask


mkdir fridaychallenge

cd fridaychallenge
python3 -m venv venv

. venv/bin/activate



mkdir flaskr

#cat flaskr/__init__.py <<EOF
## wget -> github.com

#cat getFilesFromS3Util.py <<EOF



export FLASK_APP=flaskr
export FLASK_ENV=development
# flask run --host=0.0.0.0 --port=80
flask run --host=0.0.0.0