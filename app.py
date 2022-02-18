import os

from flask import Flask
from rediscluster import RedisCluster

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


startup_nodes = [{"host": os.environ['REDIS_HOST_1'], "port": "6379"},
                 {"host": os.environ['REDIS_HOST_2'], "port": "6379"},
                 {"host": os.environ['REDIS_HOST_3'], "port": "6379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True,skip_full_coverage_check=True)
rc.set("foo", "bar")
print(rc.get("foo"))


if __name__ == '__main__':
    app.run()
