#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

SERVER_CONFIG=\
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
   
    root /var/www/html;
    index index.html;
    location /redirect_me {
        return 301 https://www.youtube.com/;
    }

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"
bash -c "echo -e '$SERVER_CONFIG' > /etc/nginx/sites-enabled/default"
service nginx restart
