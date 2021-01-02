
1. create docker file

docker file content:
FROM redis
CMD [ "redis-server"]

Build docker image:
docker build -t "docker-redis" .

Run docker image:
docker run -it --rm -p 6379:6379 "docker-redis"

################

create a simple python program to ensure our non-container items can connect to redis:

Create virtual environment
virtualenv venv

activate virtual environmet.
.\venv\Scripts\activate

Run pip install redis:
This command does not install the redis server, it just installs a redis connector that we can use in python.

pip install redis

Create test_redis.py

Content of test_redis.py file:

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
setter = r.set('foo', 'bar')
getter = r.get('foo')

print(setter, getter)

Run test_redis.py:
python test_redis.py

output:
1. True b'bar' => redis is running correctly
2. No connection could be made because the target machine actively refused it. => means your version of redis is either (1) not running 
or (2) running incorrectly or (3) you got the port number wrong.
