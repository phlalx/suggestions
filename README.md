Suggestions
-----------

Simple suggestion system. Records queries submitted by user, and propose
completions based on most-frequent previous queries.

Python REST API with AJAX client.

Launch redis with:

    docker run -p 6379:6379 redis

Fill redis using (set redis IP:port in `mapreduce.py`):

    python3 mapreduce.py

Launch server with:

    make

Then in another terminal

    open -a safari http://localhost:5000

Resources
---------

https://redis-py.readthedocs.io/en/latest/
https://medium.com/@umerfarooq_26378/web-services-in-python-ef81a9067aaf
http://flask.pocoo.org/docs/1.0/api/
https://docs.docker.com/get-started/part2/#build-the-app
https://spark.apache.org/docs/0.9.0/api/pyspark/index.html

https://blogs.oracle.com/scoter/networking-in-virtualbox-v2
https://superuser.com/questions/310697/connect-to-the-host-machine-from-a-virtualbox-guest-os