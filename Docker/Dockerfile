FROM ubuntu:18.04

ENV DBMS_ADDRESS postgresql://postgres:1234@db-postgres/postgres

ADD ./Docker/Start.sh /run/start.sh

CMD ["bash", "/run/start.sh"]