## 分析需求

## 分析网页、制定方案

## 编写逻辑代码

首先、我们知道携程景点的 url 有很多个，鉴于这个情况我们使用 redis 数据库作为中间队列缓存这些 url。
当然如果只有十几个、几百个 url 并且看起来程序不会被意外退出的话也可以使用 Python 自带的 List、set(或者第三方库实现的queue) 等数据结构作为 队列

redis 数据结构的话我们选择比较常用的 集合 就行。

> 假定你已经在本地或者远程主机上安装了redis 数据库，请参考前面的 redis 数据库章节

接下来可以创建一个 redis 的操作实例。

```python
# coding=utf-8
import redis

class RedisQueue(object):

    def __init__(self, **redis_kwargs):
        self.__db = redis.Redis(host='127.0.0.1', port=6379, db=15, password="admin")

    def sadd(self, name, v_):
        self.__db.sadd(name, v_)

    def spop(self, name):
        return self.__db.spop(name)

    def get_set_count(self, name):
        return self.__db.scard(name)

    def set_empty(self, name):
        return self.get_set_count(name) == 0

# if __name__ == '__main__':
#     R = RedisQueue()
#     R.sadd()
```

我们声明了 一个 sadd 和 一个 spop 方法分别用于添加队列元素和取出队列元素，
最后还实现了 set_empty 方法用于判断队列长度是否为 0

这样一来 我们提前将所有需要抓取的 url 链接放入到 redis 数据库中(这里我使用的是编号为 15 的数据库、你可以自行指定)

查看redis 数据库中的数据 .....

## 数据查看和利用



> 文档中代码仅供学习，请勿商用，作者保留著作权。