FROM python:3.6
WORKDIR /code

EXPOSE 5000
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt && \
    groupadd uwsgi && useradd -g uwsgi uwsgi &&

COPY . /code

RUN python manage.py migrate
CMD [ "uwsgi", "--ini", "app.ini"]