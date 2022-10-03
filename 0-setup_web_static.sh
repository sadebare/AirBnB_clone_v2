#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Release test" >> /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/

printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html;
        
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
}" > /etc/nginx/sites-available/default

sudo service nginx start
