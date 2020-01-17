<a href="https://docs.docker.com/compose/">docker-compose example</a>

To create a simplistic standalone cluster with docker-compose:

<pre>docker-compose up</pre>

The SparkUI will be running at <b>http://${YOUR_DOCKER_HOST}:8080</b> with one worker listed. To run pyspark, exec into a container:

<pre>docker exec -it spark_master_1 /bin/bash
bin/pyspark</pre>

To run SparkPi, exec into a container:

<pre>docker exec -it spark_master_1 /bin/bash
bin/run-example SparkPi 10</pre>
