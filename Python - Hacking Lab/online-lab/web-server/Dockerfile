FROM python:3.8-alpine

# Install psycopg2

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

WORKDIR /app

ADD ./app/requirements.txt requirements.txt 
RUN python -m pip install -r requirements.txt

ADD ./app ./
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]