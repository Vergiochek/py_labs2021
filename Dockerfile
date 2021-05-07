FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD povezlo.py /usr/src/app

CMD ["python", "povezlo.py"]
