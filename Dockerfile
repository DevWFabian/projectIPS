FROM python:3.10.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /projectIPS

WORKDIR /projectIPS

ADD . /projectIPS/

RUN pip install -r requirements.txt

EXPOSE 8001

CMD  python manage.py runserver 