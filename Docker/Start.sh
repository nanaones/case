#! /bin/bash

apt update &&\
apt install -y vim git python3.7 &&\
echo $DBMS_ADDRESS &&\
echo $DBMS_PORT &&\
echo $CONFI_GPATH &&\
 ./CheckStandAlone.sh &&\
echo This is a test. &&\
git clone https://github.com/nanare/case &&\
cd  /wanted/ &&\
python3 -m pip install -r requirements.txt &&\
python3 init.py &&\
echo "asdsadsadasds" &&\
gunicorn --access-logfile  &&\
         /log/logaccess_log --error-logfile &&\
         /log/error_log -b 0.0.0.0:5000  &&\
         app:app  &&\
         -w 2 --thread 4 -k gevent &