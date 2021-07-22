我们使用 `Pymysql` 作为 `Python` 和 `Mysql` 的连接库。

## 安装 `PyMysql`

```shell
pip install PyMysql
```

默认安装最新版本即可。

## 连接 `Mysql` 数据库

### 初始化连接

```python
# -*- coding: utf-8 -*-
import pymysql

dbinfo = {
    "host": "localhost",  # mysql主机
    "user": "root",  # 用户名
    "password": None,  # m密码
    "db": "hello_life"  # 数据库
}


def init():
    db = pymysql.connect(**dbinfo)
    return db
```

## 插入数据

往 `Quotations` 表添加一些数据

```shell
# -*- coding: utf-8 -*-
import pymysql
import time

dbinfo = {
    "host": "localhost",  # mysql主机
    "user": "root",  # 用户名
    "password": None,  # m密码
    "db": "hello_life"  # 数据库
}


def init_connect():
    db = pymysql.connect(**dbinfo)
    return db


def insert_data(db, itemList):
    cursor = db.cursor()  # 游标对象
    for item in itemList:
        sql = "insert into `Quotations` (`name`,`description`,`createDate`) values (%s,%s,%s)"
        cursor.execute(sql, (item["name"], item["description"], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))  # 执行sql语句
    db.commit()  # 提交事务


if __name__ == '__main__':
    db = init_connect()
    itemList = [
        {"name": "杨boss", "description": "小老弟你怎么回事儿"},
        {"name": "张老板", "description": "这谁顶得住啊"}
    ]
    insert_data(db, itemList)
```

### 一次性插入多条数据
```python
# -*- coding: utf-8 -*-
import pymysql
import time

dbinfo = {
    "host": "localhost",  # mysql主机
    "user": "root",  # 用户名
    "password": None,  # m密码
    "db": "hello_life"  # 数据库
}

def init_connect():
    db = pymysql.connect(**dbinfo)
    return db

def insert_many_data(db, itemList):
    cursor = db.cursor()  # 游标对象
    sql = "insert into `Quotations` (`name`,`description`,`createDate`) values (%s,%s,%s)"
    cursor.executemany(sql, itemList)  # 执行sql语句
    db.commit()  # 提交事务


if __name__ == '__main__':
    db = init_connect()
    itemList = [
        {"name": "杨boss", "description": "小老弟你怎么回事儿","createDate":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())},
        {"name": "张老板", "description": "这谁顶得住啊","createDate":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
    ]
    insert_many_data(db, [tuple(item.values()) for item in itemList])
    db.close()
```


通过上面的实例我们可以知道大概的执行流程是

- 初始化连接 `Mysql`
- 生成`游标对象`用于执行事务操作
- `execut` 方法传入的是 `sql` 语句
- `提交`事务并`关闭`连接

> 其中通用的做法是你只要写好 `sql` 语句就可以对 `Mysql` 起到同样的作用

诸如
```python
insert_sql = 'INSERT INTO Quotations (name, description, createDate) VALUES ("小妮", "今天的饭还没白嫖，还不能下班", NOW());'
update_sql = "UPDATE Quotations SET description='我从来没有见过这么废物的人' WHERE name='杨老板';"
delete_sql = "DELETE FROM Quotations WHERE name='陈梦游';"
```

## 查询数据

```python
import pymysql

dbinfo = {
    "host": "localhost",  # mysql主机
    "user": "root",  # 用户名
    "password": None,  # m密码
    "db": "hello_life"  # 数据库
}

def init_connect():
    db = pymysql.connect(**dbinfo)
    return db

def query_data(cursor):
    sql = "select * from Quotations;"
    cursor.execute(sql)  # 执行sql语句
    datas = cursor.fetchall() # 获取全部数据
    for data in datas:
        print(data)

if __name__ == '__main__':
    db = init_connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)  # 游标对象
    query_data(cursor)
    cursor.close()
    db.close()
```

得到结果
```text
(1, '小妮', '今天的饭还没白嫖，还不能下班', datetime.datetime(2021, 4, 16, 0, 0))
(3, '杨boss', '我从来没有见过这么废物的人', datetime.datetime(2021, 4, 16, 0, 0))
(5, '小妮', '现在接驳车人太多了，还不能下班', datetime.datetime(2021, 4, 16, 12, 0, 46))
(6, '杨老板', '废物', datetime.datetime(2021, 4, 16, 12, 0, 46))
(7, '陈梦游', '这都是潜在需求来的', datetime.datetime(2021, 4, 16, 12, 0, 46))
(8, '陈梦游', '我跟你们两个谈一下', datetime.datetime(2021, 4, 16, 12, 0, 46))
(9, '陈梦游', '你扯淡', datetime.datetime(2021, 4, 16, 12, 0, 46))
(10, '杨老板', '别吧', datetime.datetime(2021, 4, 16, 13, 29, 2))
(11, '陈梦游', '低标准', datetime.datetime(2021, 4, 16, 13, 29, 28))
(12, '杨boss', '小老弟你怎么回事儿', datetime.datetime(2021, 4, 16, 14, 26, 47))
(13, '张老板', '这谁顶得住啊', datetime.datetime(2021, 4, 16, 14, 26, 47))
```

可以看到它直接返回了一个`元组`对象，
这和我们预想的结果有些不同，一般情况下我们需要由键值对组成的 `json` 对象，也就是 `Python` 中的`字典`了。

在游标中指定 `pymysql.cursors.DictCursor` ，把结果输出为 `dict` 对象
```python
cursor = db.cursor(pymysql.cursors.DictCursor) 
```

得到结果
```text
{'id': 1, 'name': '小妮', 'description': '今天的饭还没白嫖，还不能下班', 'createDate': datetime.datetime(2021, 4, 16, 0, 0)}
{'id': 3, 'name': '杨boss', 'description': '我从来没有见过这么废物的人', 'createDate': datetime.datetime(2021, 4, 16, 0, 0)}
{'id': 5, 'name': '小妮', 'description': '现在接驳车人太多了，还不能下班', 'createDate': datetime.datetime(2021, 4, 16, 12, 0, 46)}
{'id': 6, 'name': '杨老板', 'description': '废物', 'createDate': datetime.datetime(2021, 4, 16, 12, 0, 46)}
{'id': 7, 'name': '陈梦游', 'description': '这都是潜在需求来的', 'createDate': datetime.datetime(2021, 4, 16, 12, 0, 46)}
{'id': 8, 'name': '陈梦游', 'description': '我跟你们两个谈一下', 'createDate': datetime.datetime(2021, 4, 16, 12, 0, 46)}
{'id': 9, 'name': '陈梦游', 'description': '你扯淡', 'createDate': datetime.datetime(2021, 4, 16, 12, 0, 46)}
{'id': 10, 'name': '杨老板', 'description': '别吧', 'createDate': datetime.datetime(2021, 4, 16, 13, 29, 2)}
{'id': 11, 'name': '陈梦游', 'description': '低标准', 'createDate': datetime.datetime(2021, 4, 16, 13, 29, 28)}
{'id': 12, 'name': '杨boss', 'description': '小老弟你怎么回事儿', 'createDate': datetime.datetime(2021, 4, 16, 14, 26, 47)}
{'id': 13, 'name': '张老板', 'description': '这谁顶得住啊', 'createDate': datetime.datetime(2021, 4, 16, 14, 26, 47)}
```

- `cursor.fetchall()` 获取全部结果
- `cursor.fetchone()`  获取符合条件的第 1 条结果
- `cursor.fetchmany(2)` 获取 2 条结果

关闭游标和数据库连接释放资源

- `cursor.close()`
- `db.close()`


## 数据回滚

在 `Python` 中，我们可以通过`捕捉异常`来进行事务的`回滚`操作
```python
import pymysql

dbinfo = {
    "host": "localhost",  # mysql主机
    "user": "root",  # 用户名
    "password": None,  # m密码
    "db": "hello_life"  # 数据库
}

def init_connect():
    db = pymysql.connect(**dbinfo)
    return db

def query_data(cursor):
    sql = "select title from Quotations;"
    try:
        cursor.execute(sql)  # 执行sql语句
        for data in cursor.fetchall(): # 获取全部数据
            print(data)
    except Exception as e:
        print(str(e))
        db.rollback()

if __name__ == '__main__':
    db = init_connect()
    cursor = db.cursor(pymysql.cursors.DictCursor)  # 游标对象
    query_data(cursor)
    cursor.close()
    db.close()
```

查询一个不存在的字段，得到回滚信息
```python
(1054, "Unknown column 'title' in 'field list'")
```


## 多线程插入数据
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/22 11:53
@Auth ： wutong
@File ：mysql多线程插入.py
@IDE ：PyCharm
"""
import time
import pymysql
import threading

"""尝试使用多线程插入 1000000 条数据到 Mysql"""


class Db(object):
    def __init__(self, host=None, username=None, pwd=None, dbname=None):
        self.pool = {}
        self.host = host
        self.username = username
        self.pwd = pwd
        self.dbname = dbname

    def get_instance(self, ):
        name = threading.current_thread().name
        if name not in self.pool:
            conn = pymysql.connect(self.host, self.username, self.pwd, self.dbname)
            self.pool[name] = conn
        return self.pool[name]


class Test(object):
    def __init__(self):
        self.max_id = 100000
        self.start_id = 0
        self.db = Db('localhost', 'root', None, 'TT')
        self.lock = threading.Lock()
        self.main()

    def main(self):
        threads = []
        for i in range(10):
            t = threading.Thread(target=self.insert_data)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    def insert_data(self):
        db = self.db.get_instance()
        cursor = db.cursor()
        while True:
            if self.start_id >= self.max_id:
                break
            s = self.start_id
            with self.lock:
                # print("上锁 +1000")
                self.start_id += 10000
                if self.start_id > self.max_id:
                    self.start_id = self.max_id
            e = self.start_id

            print(f"正在插入 {s} 到 {e} 条数据")
            sql = 'insert into archives(`title`,`desc`,`createDate`,`other`) values(%s,%s,%s,%s)'
            results = [
                (f'python {i}', f'desc {i}', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), f'other {i * 12}')
                for i in range(s, e)]
            try:
                cursor.executemany(sql, results)
                db.commit()
                # print(threading.current_thread().name, ': ', sql, ': success')
            except:
                db.rollback()
                # print(threading.current_thread().name, ': ', sql, ':failed')
                raise


if __name__ == '__main__':
    Test()
```



## 多线程查询数据
```python
# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/22 11:51
@Auth ： wutong
@File ：mysql多线程.py
@IDE ：PyCharm
"""
import threading
import queue
import time
import pymysql
from DBUtils.PooledDB import PooledDB


class MysqlPool(object):

    def __init__(self):
        self.POOL = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=20,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host='localhost',
            port=3306,
            user='root',
            password=None,
            database='TT',
            charset='utf8mb4'
        )

    def __new__(cls, *args, **kw):
        '''
        启用单例模式
        :param args:
        :param kw:
        :return:
        '''
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect(self):
        '''
        启动连接
        :return:
        '''
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    def connect_close(self, conn, cursor):
        '''
        关闭连接
        :param conn:
        :param cursor:
        :return:
        '''
        cursor.close()
        conn.close()

    def fetch_all(self, args):
        '''
        批量查询
        :param sql:
        :param args:
        :return:
        '''
        print(f"{args} 开始进行查询")
        conn, cursor = self.connect()
        cursor.execute("select * from archives where id=%s", args)
        record_list = cursor.fetchall()
        self.connect_close(conn, cursor)
        return record_list

    def fetch_one(self, sql, args):
        '''
        查询单条数据
        :param sql:
        :param args:
        :return:
        '''
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.connect_close(conn, cursor)
        return result

    def insert(self, sql, args):
        '''
        插入数据
        :param sql:
        :param args:
        :return:
        '''
        conn, cursor = self.connect()
        row = cursor.execute(sql, args)
        conn.commit()
        self.connect_close(conn, cursor)
        return row


class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except:
            return None


if __name__ == '__main__':
    start = time.time()
    # 创建线程连接池
    pool = MysqlPool()
    # 创建队列，队列的最大个数及限制线程个数
    q = queue.Queue(maxsize=25)
    # 测试数据，多线程查询数据库
    for i in range(16981175, 16991175):
        # print(pool.fetch_all(i))

        # 创建线程并放入队列中
        # t = MyThread(target=tread_connection_db, args=(id,))
        t = MyThread(pool.fetch_all, args=(i,))
        q.put(t)
        # 队列队满
        if q.qsize() == 20:
            print(f"当前队列大小：{q.qsize()}")
            join_thread = []  # 用于记录线程，便于终止线程
            while q.empty() != True:  # 从对列取出线程并开始线程，直到队列为空
                t = q.get()
                join_thread.append(t)
                t.start()
            # 终止上一次队满时里面的所有线程
            for t in join_thread:
                t.join()
            for t in join_thread:
                print(t.get_result())
    end = time.time() - start
    print(end)
```