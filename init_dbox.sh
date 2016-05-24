sudo /etc/init.d/mysql start
mysql -uroot -e "create database defaultdb;"
mysql -uroot -e "CREATE USER 'floud' IDENTIFIED BY 'square';"