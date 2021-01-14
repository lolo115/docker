FROM debian:buster
MAINTAINER Premiseo "https://premiseo.com"

# github link to follow

RUN apt-get update \
 && apt-get install -y locales vim procps wget net-tools \
 && dpkg-reconfigure -f noninteractive locales \
 && locale-gen C.UTF-8 \
 && /usr/sbin/update-locale LANG=C.UTF-8 \
 && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
 && locale-gen

# Users with other locales should set this in their derivative image
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV JUPYTER_HOME /var/tmp/jupyter

RUN mkdir $JUPYTER_HOME
RUN apt-get update \
 && apt-get install -y curl unzip \
    python3 python3-setuptools \
   && curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py \
   && python3 ./get-pip.py \
   && ln -s /usr/bin/python3 /usr/bin/python \
   && ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip3 install py4j

# Install python package
RUN pip3 install numpy scipy tensorflow scikit-learn pandas matplotlib jupyter statsmodels

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /*.deb

WORKDIR $JUPYTER_HOME
CMD ["/usr/local/bin/jupyter","notebook","--ip","0.0.0.0","--no-browser","--allow-root"]
