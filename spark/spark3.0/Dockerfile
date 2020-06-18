FROM debian:stretch
MAINTAINER Premiseo "https://premiseo.com"
# github link to follow

RUN apt-get update \
 && apt-get install -y locales vim procps wget \
 && dpkg-reconfigure -f noninteractive locales \
 && locale-gen C.UTF-8 \
 && /usr/sbin/update-locale LANG=C.UTF-8 \
 && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
 && locale-gen 

# Users with other locales should set this in their derivative image
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN groupadd -g 1001 docker
RUN useradd -u 1001 -g docker -G root docker

RUN apt-get update \
 && apt-get install -y curl unzip \
    python3 python3-setuptools \
   && curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py \
   && python3 ./get-pip.py \
   && ln -s /usr/bin/python3 /usr/bin/python \
   && ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip3 install py4j

# Install python package
RUN pip3 install numpy pandas matplotlib jupyter statsmodels sparkmeasure

# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-pythonhashseed
ENV PYTHONHASHSEED 0
ENV PYTHONIOENCODING UTF-8
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# JAVA
RUN apt-get update \
&& apt-get install -y openjdk-8-jdk 
	
# SCALA & SBT
ENV SCALA_VERSION "2.11.12" 
ENV SCALA_HOME /usr/scala-${SCALA_VERSION} 
ENV	SBT_VERSION "1.3.10" 
ENV	SBT_HOME /usr/sbt 
ENV	PATH ${SCALA_HOME}/bin:${SBT_HOME}/bin:${PATH}

RUN curl -sL --retry 3 \
	"http://www.scala-lang.org/files/archive/scala-${SCALA_VERSION}.tgz" \
	| gunzip \
	| tar x -C /usr/

RUN curl -sL --retry 3 \
    "https://piccolo.link/sbt-${SBT_VERSION}.tgz" 	\
    | gunzip \
	| tar x -C /usr/

RUN chown -R root:root "${SBT_HOME}" 
RUN chown -R root:root "${SCALA_HOME}"
	
# This next command makes SBT download all JARs necessary to run so using SBT the first time isn't so painful.
RUN echo "exit" | sbt    

# HADOOP
ENV HADOOP_VERSION 3.2.0
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH $PATH:$HADOOP_HOME/bin

RUN curl -sL --retry 3 \
  "http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" \
 | gunzip \
 | tar -x -C /usr/ \
&& rm -rf $HADOOP_HOME/share/doc \
&& chown -R root:root $HADOOP_HOME

# SPARK
ENV SPARK_VERSION 3.0.0-preview2
#ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-hadoop3.2
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}
ENV  SPARK_DIST_CLASSPATH="/jars/*:$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*:$HADOOP_HOME/share/hadoop/client/*"

ENV PATH $PATH:${SPARK_HOME}/bin
RUN curl -sL --retry 3 \
  "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/${SPARK_PACKAGE}.tgz" \
  | gunzip \
  | tar x -C /usr/ \
 && mv /usr/$SPARK_PACKAGE $SPARK_HOME \
 && chown -R root:root $SPARK_HOME


RUN apt-get update
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /*.deb 

WORKDIR $SPARK_HOME
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
