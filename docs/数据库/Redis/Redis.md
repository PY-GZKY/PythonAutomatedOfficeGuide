## Redis 队列

```shell
pip install redis
```

```python
# coding=utf-8
import redis

class RedisQueue(object):

    def __init__(self, **redis_kwargs):
        self.__db = redis.Redis(host='127.0.0.1', port=6379, db=6, password=None)

    # 返回队列大小
    def qsize(self, name):
        return self.__db.llen(name)

    # 判断队列用尽
    def empty(self,name):
        return self.qsize(name) == 0

    # rpush进去或者lpush都可以
    def put(self, name, item):
        self.__db.rpush(name, item)

    def sadd(self, name, v_):
        self.__db.sadd(name, v_)

    def spop(self, name):
        return self.__db.spop(name)

    def get_set_count(self, name):
        return self.__db.scard(name)

    def set_empty(self, name):
        return self.get_set_count(name) == 0

    # get出来
    def get(self, name, block=True, timeout=5):
        if block:
            item = self.__db.blpop(name, timeout=timeout)
        else:
            item = self.__db.lpop(name)
        return item

    # 直接lpop()
    def get_nowait(self):
        return self.get(False)

# if __name__ == '__main__':
#     R = RedisQueue()
#     R.sadd()

```

