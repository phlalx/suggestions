# pyspark contains a standalone spark implem
# export SPARK_HOME=/usr/local/lib/python3.6/dist-packages/pyspark
# export PYSPARK_PYTHON=python3 

from pyspark import SparkContext
import redis

sc = SparkContext.getOrCreate()
rrd = sc.textFile("requests.txt")

rrd1 = rrd.map(lambda x: (x, 1))
rrd2 = rrd1.reduceByKey(lambda x, y : x + y)

def prefixes(x):
  w, n = x
  res = []
  for i in range(len(w) + 1):
    res.append((w[:i], [ (n, w) ]))
  return res

rrd3 = rrd2.flatMap(prefixes)

def g(x, y):
  u = x + y
  u.sort(reverse = True)
  return u[:10]

rrd4 = rrd3.reduceByKey(g)

def remove_freq(x):
  k, l = x
  return k, " ".join([ w for (_, w) in l ])

rrd5 = rrd4.map(remove_freq)

def to_redis(x):  
  try:
    pass
    red = redis.Redis(host="10.0.2.2", db=0, socket_connect_timeout=2, socket_timeout=2)
    w, l = x
    red.set(w, l)
  except:
    pass

rrd5.foreach(to_redis)
