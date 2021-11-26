FROM python:3.10-slim

WORKDIR /app

ADD ./app/requirements.txt requirements.txt 
RUN python -m pip install -r requirements.txt

ADD ./app ./
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]