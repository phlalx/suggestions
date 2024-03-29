# pyspark contains a standalone spark implem
# export SPARK_HOME=/usr/local/lib/python3.6/dist-packages/pyspark
# export PYSPARK_PYTHON=python3 

from pyspark import SparkContext
import redis

def prefixes(x):
  w, n = x
  res = []
  for i in range(len(w) + 1):
    res.append((w[:i], [ (n, w) ]))
  return res

def g(x, y):
  u = x + y
  u.sort(reverse = True)
  return u[:10]

def remove_freq(x):
  k, l = x
  return k, " ".join([ w for (_, w) in l ])

def to_redis(x):  
  try:
    pass
    red = redis.Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
    w, l = x
    red.set(w, l)
  except:
    pass

def fill_redis():
  sc = SparkContext.getOrCreate()
  rrd = sc.textFile("requests.txt")
  rrd1 = rrd.map(lambda x: (x, 1))
  rrd2 = rrd1.reduceByKey(lambda x, y : x + y)
  rrd3 = rrd2.flatMap(prefixes)
  rrd4 = rrd3.reduceByKey(g)
  rrd5 = rrd4.map(remove_freq)
  rrd5.foreach(to_redis)

if __name__ == "__main__":
  fill_redis()
