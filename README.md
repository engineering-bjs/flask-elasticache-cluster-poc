### Flask Python AWS Elasticache REDIS cluster POC with multiple nodes & sharding Note:- This POC done on M1 Mac chip


### Docker Build Linux 
``` 
$ docker build -t  anishdhanka/flask-elasticache-cluster-poc --no-cache --platform linux/x64 -f docker/Dockerfile .
```

### Docker Build M1 Chip  
``` 
$ docker build -t anishdhanka/flask-elasticache-cluster-poc-m1 --no-cache --platform linux/arm64/v8 -f docker/Dockerfile .
```


### Docker run 
```
docker run -d -p 5000:5000 -e REDIS_HOST_1='' -e REDIS_HOST_2='' -e REDIS_HOST_3='' -td anishdhanka/flask-elasticache-cluster-poc
```

### Code Snippet 
```
startup_nodes = [{"host": os.environ['REDIS_HOST_1'], "port": "6379"},
                 {"host": os.environ['REDIS_HOST_2'], "port": "6379"},
                 {"host": os.environ['REDIS_HOST_3'], "port": "6379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True,skip_full_coverage_check=True)
rc.set("foo", "bar")
print(rc.get("foo"))

```
