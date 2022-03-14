#!/bin/bash

yum update -y

yum install -y wget
yum install -y unzip
yum install -y python
yum install -y pip
pip3 install flask boto3


output : { all : '| tee -a /var/log/cloud-init-output.log' }

wget https://github.com/arno-hartmann/aws-fc-api-balancing-scaling/archive/refs/heads/main.zip

unzip main 

cd aws-fc-api-balancing-scaling-main

python3 -m venv venv

. venv/bin/activate

export FLASK_APP=flaskr
export FLASK_ENV=development
# flask run --host=0.0.0.0 --port=80
flask run --host=0.0.0.0