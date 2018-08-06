Suggestions
-----------

Propose possible query completions based on a log of past queries. 

This is very basic and was done as an opportunity to play with docker, spark and redis.

The web app which uses [flask](http://flask.pocoo.org), [pyspark](https://spark.apache.org/docs/0.9.0/api/pyspark/index.html), [redis-py](https://redis-py.readthedocs.io/en/latest/) and is based on the [docker tutorial](https://docs.docker.com/get-started/). It is implemented as simple REST API with an AJAX client.

Launch redis with:

    docker run -p 6379:6379 redis

Launch server with:

    make

To use Spark embedded in `pyspark`:

    export SPARK_HOME=$(pip3 show pyspark | grep ^Location | awk '{print $2}')/pyspark
    export PYSPARK_PYTHON=python3    

The application should be available at `http://localhost:5000/index.html`.

Alternatively, one can build a docker image and deploy it.

    make docker-build 
    make docker-start-stack

## TODO

The docker stack doesn't set up spark properly. Either install java in the suggestions Dockerfile or set up a Spark service, using for instance `sequenceiq:spark`.

This doesn't scale. Set up a redis cluster and a spark cluster.

## Resources

https://medium.com/@umerfarooq_26378/web-services-in-python-ef81a9067aaf

