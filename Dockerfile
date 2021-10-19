FROM ubuntu:20.04

LABEL maintainer="uk <uk@domain.com>"

# By default, listen on port 5000
EXPOSE 5000

# Update packages
RUN apt update; apt dist-upgrade -y

# Install packages
RUN apt install -y python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENV FLASK_APP __init__.py
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]