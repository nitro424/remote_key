FROM ubuntu:latest
RUN apt -y update && apt -y upgrade && apt -y install apt-utils python3 python3-pip python3-venv
# RUN dnf up -y --refresh
# RUN dnf in -y python3-pip

WORKDIR /remote_key
COPY . /remote_key

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt

WORKDIR /
CMD ["/opt/venv/bin/python", "remote_key"]

