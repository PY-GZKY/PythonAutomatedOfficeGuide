我们使用 `Pymongo`作为`Python`与`MongoDB`的连接库，实际上他是最好用的扩展库了。

## 安装 Pymongo

```shell
pip install Pymongo
```

## 连接数据库

### 连接本地`MongoDB`

假如你在本地机器安装了`MongoDB`数据库，使用一下初始化连接代码

```python
# -*- coding: utf-8 -*-
import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["地下交通站"]
```

使用 `MongoClient` 对象，指定连接的 `URL` 地址和数据库名。

当然我们也可以通过指定各个连接参数来初始化对象

```python
# -*- coding: utf-8 -*-
import pymongo

mongo_client = pymongo.MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]
```

## 插入文档

我们指定一个集合`Quotations`并添加一些数据

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

item = {"name": "黄金标", "description": "你今天最要紧的公务，就是挨这顿揍", "createDate": "2021-04-17"}
if db["Quotations"].insert_one(item):
    print("成功存储到MONGODB .... done")
else:
    print("存储到MONGODB失败 .... fail")
```

> 如果需要单步执行，我建议你通过 `ipython` 解释器运行


```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

item_list = [
    {"name": "贾贵", "description": "我啐他一脸狗屎", "createDate": "2021-04-18"},
    {"name": "黄金标", "description": "我们是用枪的时候少，用腿的时候多，我们不嫌自己的枪不好，只恨爹妈少生了两条腿", "createDate": "2021-04-19"},
]
if db["Quotations"].insert_many(item_list):
    print("成功存储到MONGODB .... done")
else:
    print("存储到MONGODB失败 .... fail")
```

查看`Quotations`集合文档

```shell
> db.Quotations.find({})
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "这秤砣也TM炖熟了", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078ee01249a48b5bb83b936"), "name" : "濑川", "description" : "去东关，捣乱的干活" }
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "description" : "你今天最要紧的公务，就是挨这顿揍", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "description" : "我啐他一脸狗屎", "createDate" : "2021-04-18" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "description" : "我们是用枪的时候少，用腿的时候多，我们不嫌自己的枪不好，只恨爹妈少生了两条腿", "createDate" : "2021-04-19" }
```
发现已经成功插入了3条文档

> 通过以上运行结果可以知道当 `MongoDB` 指定数据库或集合的时候，如果该数据库或集合不存在，则`自动创建`。当然必须有数据插入时才会真正生效 ！！

## 更新文档

### 更新满足查询条件的第一个文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

item = {"name": "黄金标", "description": "刘副官你记住了，让皇军先尿。", "createDate": "2021-04-23"}
db["Quotations"].update_one({"name": item["name"]}, {"$set": item}, upsert=True)
```

```shell
> db.Quotations.find({})
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "刘副官你记住了，让皇军先尿。", "createDate" : "2021-04-23" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078ee01249a48b5bb83b936"), "name" : "濑川", "description" : "去东关，捣乱的干活" }
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-17", "description" : "你今天最要紧的公务，就是挨这顿揍" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-19", "description" : "我们是用枪的时候少，用腿的时候多，我们不嫌自己的枪不好，只恨爹妈少生了两条腿" }
```
发现文档已经更新成功，只更新了满足匹配条件的第一个文档

### 更新满足查询条件的多个文档

更新集合中的多个文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

item = {"name": "黄金标", "description": "刘副官你记住了，让皇军先尿。", "createDate": "2021-04-26"}
db["Quotations"].update_many({"name": item["name"]}, {"$set": item}, upsert=True)
```

```shell
> db.Quotations.find({})
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "刘副官你记住了，让皇军先尿。", "createDate" : "2021-04-26" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078ee01249a48b5bb83b936"), "name" : "濑川", "description" : "去东关，捣乱的干活" }
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```
这样我们就把所有 `name` 为 `黄金标` 的文档全部更新为 `item`


## 删除文档

### 删除满足条件的第一个文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

name = "黑藤"
db["Quotations"].delete_one({"name": name})
```

### 删除满足查询条件的多个文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

name = "黄金标"
db["Quotations"].delete_many({"name": name})
```

如果查询条件为空`{}`，则删除集合中的所有文档，等价于删除一个集合 ！！

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

name = "海水可凉"
db["Quotations"].delete_many({})
```

### 查询并删除文档，匹配单条文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

del_result = db["Quotations"].find_one_and_delete({'name': '黄金标', })
print(del_result)
```

删除并返回了结果

```shell
{'_id': ObjectId('6078ebd395708b77ad7a8bd8'), 'name': '黄金标', 'description': '刘副官你记住了，让皇军先尿。', 'createDate': '2021-04-26'}
```

运用场景的话多见于将`MongoDB`作为`队列`使用， 如果你有一些存在于`MongoDB`集合中的 `URL` 队列，可将 `MongoDB`作为中间队列使用， 实际上已经有不少人既将`MongoDB`用于`数据储存`、又将`mongoDB`作为`中间队列`使用。

删除集合

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

db["Quotations"].drop()
```

## 查询文档

### 查询集合中第一个文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

first_doc = db["Quotations"].find_one()
print(first_doc)
```

### 查询集合中所有文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

all_docs = db["Quotations"].find({})
for doc in all_docs:
    print(doc)
```

### 查询指定字段的数据

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

all_docs = db["Quotations"].find({}, {"_id": 0})
for doc in all_docs:
    print(doc)
```

`0` 表示我们忽略了` _id` 字段的输出，除了 `_id` 你不能在一个对象中同时指定 `0` 和 `1`，如果你设置了一个字段为 `0`，则其他都为 `1`，反之亦然

输出结果

```text
{'name': '黑藤', 'description': '天下汉奸一般蠢', 'createDate': '2021-04-16'}
{'name': '孙友福', 'description': '没有水就没有鱼，没有你就没有驴', 'createDate': '2021-04-17'}
{'name': '濑川', 'description': '去东关，捣乱的干活'}
{'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。'}
{'name': '贾贵', 'createDate': '2021-04-18', 'description': '我啐他一脸狗屎'}
{'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。'}
```

### 查询条件

`and` 操作

查询出`name` 为 `黑藤`、`description`为`天下汉奸一般蠢` 的所有文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

query = {"name": "黑藤", "description": "天下汉奸一般蠢"}
all_docs = db["Quotations"].find(query, {"_id": 0})
for doc in all_docs:
    print(doc)
```
得到 `1` 条结果
```shell
{'name': '黑藤', 'description': '天下汉奸一般蠢', 'createDate': '2021-04-16'}
```

`or` 操作

查询出`name` 为 `黄金标`或 `description` 为 `探清水河` 的所有文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]
query = {"$or": [{"name": "海水可凉"}, {"description": "刘副官你记住了，让皇军先尿。"}]}
all_docs = db["Quotations"].find(query)
for doc in all_docs:
    print(doc)
```
得到 `2` 条结果
```shell
{'_id': ObjectId('6078f0e31e12a856cf9525da'), 'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。'}
{'_id': ObjectId('6078f2091e12a856cf9525dd'), 'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。'}
```

### 联合使用

查询匹配 [ `name` 为 `黄金标` 并且 `description` 为 `刘副官你记住了，让皇军先尿。` ] 或者
[ `createDate` 为`2021-04-18` ] 的文档

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]
query = {"$or": [{"name": "黄金标", "description": "刘副官你记住了，让皇军先尿。"}, {"createDate": "2021-04-18"}]}
all_docs = db["Quotations"].find(query)
for doc in all_docs:
    print(doc)
```
得到一下结果
```shell
{'_id': ObjectId('6078f0e31e12a856cf9525da'), 'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。'}
{'_id': ObjectId('6078f2091e12a856cf9525dc'), 'name': '贾贵', 'createDate': '2021-04-18', 'description': '我啐他一脸狗屎'}
{'_id': ObjectId('6078f2091e12a856cf9525dd'), 'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。'}
```

### 范围查询、正则查询

- `$lt`   小于
- `$gt`   大于
- `$lte`  小于等于
- `$gte`  大于等于
- `$ne`   不等于
- `$in`   在范围内
- `$nin`  不在范围内

搜索查询时间于 `1990-03-03` 之后的所有文档
```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]
all_docs = db["Quotations"].find({'createDate': {'$gt': '1990-03-03'}})
for doc in all_docs:
    print(doc)
```

- `$regex`   匹配正则
- `$exists`  属性是否存在
- `$type` 类型判断
- `$mod` 数字模操作
- `$text` 文本查询
- `$where` 高级条件查询


### 高级用法

#### 排序
在 `MongoDB` 中使用 `sort()` 方法对数据进行排序， `sort()` 方法可以通过参数指定排序的字段， 并使用 `1` 和 `-1` 来指定排序的方式， 其中 `1` 为升序排列，而 `-1` 是用于降序排列。

我们总是喜欢用`时间`维度来排序集合中的文档

```shell
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]
all_docs = db["Quotations"].find({'createDate': {'$gt': '2021-03-03'}}).sort("createDate",-1)
for doc in all_docs:
    print(doc)
```

得到结果
```text
{'_id': ObjectId('6078f0e31e12a856cf9525da'), 'name': '黄金标', 'createDate': '2021-04-26', 'description': '刘副官你记住了，让皇军先尿。', 'forceValue': 21.887495918176125}
{'_id': ObjectId('607a6f9ca27beefb4e49670d'), 'name': '黑藤', 'description': '全东亚乃至全亚洲都找不到第二张想你这么一张空前绝后的脸来', 'forceValue': 76.46170896626427, 'createDate': '2021-04-22'}
{'_id': ObjectId('607a6f9ca27beefb4e49670e'), 'name': '贾贵', 'description': '这我哪知道啊，我就知道她长得嘿', 'forceValue': 28.04757175413979, 'createDate': '2021-04-19'}
{'_id': ObjectId('6078f2091e12a856cf9525dc'), 'name': '贾贵', 'createDate': '2021-04-18', 'description': '我啐他一脸狗屎', 'forceValue': 94.18697675337746}
{'_id': ObjectId('6078ebd395708b77ad7a8bdb'), 'name': '孙友福', 'description': '没有水就没有鱼，没有你就没有驴', 'createDate': '2021-04-17', 'forceValue': 43.71427504449847}
{'_id': ObjectId('6078ebd395708b77ad7a8bda'), 'name': '黑藤', 'description': '天下汉奸一般蠢', 'createDate': '2021-04-16', 'forceValue': 14.796604243632927}
{'_id': ObjectId('607a6f9ca27beefb4e49670c'), 'name': '贾贵', 'description': '皇军没来的时候，你欺负我，皇军来了你还欺负我，那皇军不是TM白来了吗', 'forceValue': 81.9931941785778, 'createDate': '2021-04-14'}
{'_id': ObjectId('607a6f9ca27beefb4e49670b'), 'name': '黄金标', 'description': '我黄某人为官一任就得保一方平安', 'forceValue': 99.26063352194744, 'createDate': '2021-04-11'}
```

#### 分组、过滤、聚合函数

通过 `$match` 过滤数据
```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

match_dict = {"$match":{"name":"贾贵"}}
result_list = db["Quotations"].aggregate([match_dict])
for result in result_list:
    print(result)
```

结果如下

```text
{'_id': ObjectId('6078f2091e12a856cf9525dc'), 'name': '贾贵', 'createDate': '2021-04-18', 'description': '我啐他一脸狗屎', 'forceValue': 94.18697675337746}
{'_id': ObjectId('607a6f9ca27beefb4e49670c'), 'name': '贾贵', 'description': '皇军没来的时候，你欺负我，皇军来了你还欺负我，那皇军不是TM白来了吗', 'forceValue': 81.9931941785778, 'createDate': '2021-04-14'}
{'_id': ObjectId('607a6f9ca27beefb4e49670e'), 'name': '贾贵', 'description': '这我哪知道啊，我就知道她长得嘿', 'forceValue': 28.04757175413979, 'createDate': '2021-04-19'}
```

从过滤查询的结果来看，这和 
`db["Quotations"].find({"name":"贾贵"})` 并无二至。


常见聚合函数
- `$sum`
- `$avg`
- `$max`
- `$min`
- `$first`
- `$last`


将过滤后的数据根据 `createDate` 进行分组并通过聚合函数求和 `forceValue` 字段

```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

match_dict = {"$match": {"name": "贾贵"}}
group_dict = {"$group":{"_id":"$createDate","forceValue":{"$sum":"$forceValue"}}}
result_list = db["Quotations"].aggregate([match_dict,group_dict])
for result in result_list:
    print(result)
```

```text
{'_id': '2021-04-19', 'forceValue': 28.04757175413979}
{'_id': '2021-04-14', 'forceValue': 81.9931941785778}
{'_id': '2021-04-18', 'forceValue': 94.18697675337746}
```


多字段聚合
```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

match_dict = {"$match": {}}
group_dict = {"$group":{"_id": {"createDate":"$createDate","name":"$name",},"forceValue":{"$sum":"$forceValue"}}}
result_list = db["Quotations"].aggregate([match_dict,group_dict])
for result in result_list:
    print(result)
```

分组之后的文档总数
```python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, username=None, password=None)
db = mongo_client["地下交通站"]

match_dict = {"$match": {"name": "贾贵"}}
group_dict = {"$group":{"_id":"$createDate","count":{"$sum":1}}}
result_list = db["Quotations"].aggregate([match_dict,group_dict])
for result in result_list:
    print(result)
```
```text
{'_id': '2021-04-14', 'count': 1}
{'_id': '2021-04-18', 'count': 1}
{'_id': '2021-04-19', 'count': 1}
```

