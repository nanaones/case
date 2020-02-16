#! /bin/bash

echo $DBMS_ADDRESS &&\
echo $DBMS_PORT &&\
apt update && apt install -y git python3.7 python3-pip locales&&\
export LANGUAGE=ko_KR.UTF-8 &&\
export LANG=ko_KR.UTF-8 &&\
git clone http://github.com/nanaones/case &&\
cd  ./case &&\
python3.7 -m pip install -r requirements.txt &&\
python3 init.py &&\
gunicorn --access-logfile  &&\
         /log/logaccess_log --error-logfile &&\
         /log/error_log -b 0.0.0.0:5000  &&\
         app:app  &&\
         -w 2 --thread 4 -k gevent &