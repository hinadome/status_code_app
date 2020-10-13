#!/bin/sh
sudo yum update
sudo yum install python3
sudo amazon-linux-extras install nginx1
sudo yum install git
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
sudo cp nginx.conf /etc/nginx/
sudo service nginx start
