FROM python:3.10-alpine

ENV TZ=America/Bogota \
    SQLALCHEMY_DATABASE_URI=postgresql://postgres:postgres@postgres.cank2kiiek0c.us-east-1.rds.amazonaws.com/postgres

RUN mkdir -p /home/app
WORKDIR /home/app

COPY requirements.txt ./

RUN apk update \    
    && apk add gcc \
    && apk add python3-dev \
    && apk add musl-dev \
    && apk add py3-pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

RUN adduser -S remote_user
USER remote_user

EXPOSE 5007

CMD ["gunicorn", "--bind", "0.0.0.0:5007", "application:application"]
