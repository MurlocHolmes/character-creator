FROM grahamdumpleton/mod-wsgi-docker:python-3.5

USER root

WORKDIR /home/app

COPY ./requirements.txt /home/app/requirements.txt

RUN pip install -r requirements.txt


