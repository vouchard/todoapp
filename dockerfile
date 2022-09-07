
# pull official base image
FROM python:3.8-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/usr/src/app
ENV APP_HOME=/usr/src/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME



RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static

WORKDIR /app
COPY ./ /app/
EXPOSE 8000

ENV env_todo='dev'
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
ENTRYPOINT ["python3","manage.py","runserver","0.0.0.0:8700"]


# copy project
#WORKDIR /app
#COPY ./ /app/