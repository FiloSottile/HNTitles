FROM ubuntu

MAINTAINER Filippo Valsorda <fv@filippo.io>

# Update APT cache
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update  # 2013-11-22

# Set the locale
RUN apt-get install -y language-pack-en
RUN update-locale LANG=en_US.UTF-8

# Install common packages - remember to start cron from supervisord
RUN apt-get install -y joe less curl wget cron net-tools

RUN apt-get install -y python python-pip git
RUN git clone https://github.com/FiloSottile/HNTitles.git
RUN cd HNTitles && pip install -r requirements.txt

CMD ["bash", "-c", "cd HNTitles && python tweep.py"]
