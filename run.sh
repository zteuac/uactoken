#!/bin/bash
set -e
export TZ=Asia/Shanghai
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
 
service nginx restart

cd /usr/local/tomcat/bin
./startup.sh

crontab /usr/local/tomcat/tomcat_cron
crontab -l
service crond start

echo "start sleep........."
while [ 1 ]
do
        sleep 300
done
