#!/bin/sh
# Wait for DB to start up
until nc -z -w 4 db 3306
do
    echo "Can't connect to mysql"
    sleep 3
done
echo "CREATE DATABASE powerdns" | mysql -u root --password=root -h db
cd dnsaas
pip install -e .
pip install -r requirements/dev.txt
dnsaas syncdb --noinput
dnsaas migrate --noinput
dnsaas loaddata test
echo "from django.contrib.auth.models import User; User.objects.create_superuser('dnsaas', 'dnsaas@example.com', 'dnsaas')" | dnsaas shell
dev_dnsaas runserver 0.0.0.0:8080
