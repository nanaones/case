#! /bin/bash

export LANGUAGE=ko_KR.UTF-8 &&\
export LANG=ko_KR.UTF-8 &&\
pip3 install -r requirements.txt &&\
./CheckStandAlone.sh &&\
python3 init.py &&\
gunicorn --access-logfile  &&\
         /log/logaccess_log --error-logfile &&\
         /log/error_log -b 0.0.0.0:5000  &&\
         app:app  &&\
         -w 2 --thread 4 -k gevent &