#! /bin/bash

export LANGUAGE=ko_KR.UTF-8 &&\
export LANG=ko_KR.UTF-8 &&\
pip3 install -r requirements.txt &&\
./CheckStandAlone.sh &&\
python3 init.py
