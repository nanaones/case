FROM python:3.8

RUN apt-get update -y
RUN apt-get install -y build-essential git python3-pip 
RUN pip3 install --upgrade pip 

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN python3 init.py
CMD ["gunicorn", "-b 0.0.0.0:5000", "-k gevent", "src.runner:app"]