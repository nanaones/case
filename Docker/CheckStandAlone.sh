#! /bin/bash
echo $IS_STAND_ALONE
if [ $IS_STAND_ALONE == false ]; then
    git clone https://github.com/vishnubob/wait-for-it /wait &&\
    # wait-for-it
    chmod +x ./wait/wait-for-it.sh &&\
    echo "wait for DB" &&\
    ./wait/wait-for-it.sh $DBMS_ADDRESS:$DBMS_PORT 

elif [ $IS_STAND_ALONE == true ]; then
    mkdir /logs/
fi
echo `ls /config`