sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default1
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/test
cd /home/box/web/ask
sudo gunicorn -c /etc/gunicorn.d/test ask.wsgi:application &
