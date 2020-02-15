FROM ubuntu:18.04

ENV DBMS_ADDRESS postgresql://postgres:1234@db-postgres/postgres
ENV CONFIGPATH /run/config.ini

ADD ./Docker/Start.sh /run/start.sh
ADD ./Config  /run/config
CMD ["bash", "/run/start.sh"]