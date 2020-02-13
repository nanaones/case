#! /bin/bash

echo $DBMS_ADDRESS &&\
echo $DBMS_PORT &&\
echo $CONFI_GPATH &&\
/docker/CheckStandAlone.sh &&\
git clone https://github.com/nanare/wanted &&\
cd  /wanted/ &&\
python3 -m pip install -r requirements.txt &&\
gunicorn --access-logfile  &&\
         /log/logaccess_log --error-logfile &&\
         /log/error_log -b 0.0.0.0:5000  &&\
         main:app  &&\
         -w 2 --thread 4 -k gevent &