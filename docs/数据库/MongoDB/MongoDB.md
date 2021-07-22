`MongoDB` 是非关系型数据库的代表，一款基于`键值储存`的高性能数据库。常作为爬虫储存数据库。

`MongoDB` 是一个基于分布式文件存储的数据库。由 `C++` 语言编写。旨在为 `WEB` 应用提供可扩展的高性能数据存储解决方案。

`MongoDB` 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

[comment]: <> (> 来自 [`runoob`]&#40;https://www.runoob.com/mongodb/mongodb-tutorial.html&#41;)

## 连接 `MongoDB`

格式: `mongodb://username:password@host:port/database`

- `mongodb://`： 固定的连接头，必须要指定。
- `username:password`： 用户名密码验证，如果密码为空可不填
- `host`： 指定`host`， `URI` 是唯一`必填`项。它指定了要连接服务器的地址。
- `port`： 指定端口，如果不填，默认为 `27017`
- `database`： 若不指定，默认打开 `test` 数据库。

## 创建`数据库`、`集合`

### 尝试创建数据库 `地下交通站`

我们使用中文命名我们的第一个数据库

```shell
> use 地下交通站
switched to db 地下交通站
> db
地下交通站
```

如果该数据库已存在则会切换到此库，如果没有，则创建。

### 查看数据库列表

```shell
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```

在 `MongoDB`中，数据库必须要有数据才能在列表中看到它，这一点和其他数据库还是有很大的不同，我们将在稍后尝试插入数据。

### 尝试创建集合 `Quotations`

```shell
> db.createCollection("Quotations")
{ "ok" : 1 }
```

这样一个`集合`就创建成功了。

查看 数据库`地下交通站` 中的所有集合

```shell
> show collections
Quotations
```

> 删库就更简单了，跑路才难 ！！

### 删除一个数据库

```shell
> use 地下交通站
switched to db 地下交通站

> db.dropDatabase()
{ "dropped" : "地下交通站", "ok" : 1 }
```

这样一个`MongoDB`数据库就没了。

### 删除一个集合

```shell
> use 地下交通站
switched to db 地下交通站
> db.Quotations.drop()  # 删除集合
```

这样数据库`地下交通站` 中的`Quotations`集合就没了 ！

## 插入文档

`MongoDB` 是一个面向文档存储的数据库，操作起来比较简单和容易。

`MongoDB` 中一条数据被视为一个`文档`，而一个表则被称为一个`集合`(`Collection`)。

`db.collection.insertOne()` 用于向集合插入一个新文档(单个`json`对象)

`db.collection.insertMany()` 用于向集合插入一个多个文档(`json`对象列表)

### 尝试插入一条数据

在数据库`地下交通站`中的`Quotations` 集合中插入一条数据

```shell
> use 地下交通站
switched to db 地下交通站

> db.Quotations.insert({
   name: '贾贵',
   description: '老子在这欠的饭钱够你吃二年的',
   createDate: '2021-04-15'
 })
WriteResult({ "nInserted" : 1 })
```

查看已插入文档记录

```shell
> db.Quotations.find({})
{ "_id" : ObjectId("6078e9743252cc07e092d204"), "name" : "贾贵", "description" : "老子在这欠的饭钱够你吃二年的", "createDate" : "2021-04-15" }
```

> 可以看到 MongoDB 集合自动帮我们生成了 _id 字段用于唯一索引 ！！

### 尝试插入多条数据

```shell
> db.Quotations.insertMany([
         {name: '黄金标',description: '这秤砣也TM炖熟了',createDate: '2021-04-15'},
         {name: '贾贵',description: '我捂着脑袋捂着脸撅着屁股就跟他打起来了',createDate: '2021-04-16'},
         {name: '黑藤',description: '你说我他么是谁，我他么是黑藤',createDate: '2021-04-16'},
         {name: '孙友福',description: '没有水就没有鱼，没有你就没有驴',createDate: '2021-04-17'}
     ])
```

```shell
> db.Quotations.find({})
{ "_id" : ObjectId("6078e9743252cc07e092d204"), "name" : "贾贵", "description" : "老子在这欠的饭钱够你吃二年的", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "这秤砣也TM炖熟了", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd9"), "name" : "贾贵", "description" : "我捂着脑袋捂着脸撅着屁股就跟他打起来了", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "你说我他么是谁，我他么是黑藤", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
```

## 更新文档

### 尝试更新 `name` 字段(单条文档)

```shell
> db.Quotations.update({'name':'黑藤'},{$set:{name: '黑藤',description: '天下汉奸一般蠢',createDate: '2021-04-16'}})
```

更改生效

```shell
> db.Quotations.find({})                                                                                 1-04-16'}})
{ "_id" : ObjectId("6078e9743252cc07e092d204"), "name" : "贾贵", "description" : "老子在这欠的饭钱够你吃二年的", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "这秤砣也TM炖熟了", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd9"), "name" : "贾贵", "description" : "我捂着脑袋捂着脸撅着屁股就跟他打起来了", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" } 
```

### 尝试更新所有文档

```shell
> db.Quotations.update({'name':'贾贵'},{$set: {name: '贾贵',description: '这我哪知道呀！我知道她长的嘿！',createDate: '2021-04-16'}},{multi:true})
```

```shell
> db.Quotations.find({})                                                                                     
{ "_id" : ObjectId("6078e9743252cc07e092d204"), "name" : "贾贵", "description" : "这我哪知道呀！我知道她长的嘿！", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "这秤砣也TM炖熟了", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd9"), "name" : "贾贵", "description" : "这我哪知道呀！我知道她长的嘿！", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
```

这里我们将 `multi` 参数设置成 `True`，意味着将更新所有匹配查询条件的文档

发现所有`name` 为`贾贵`的语录都改变了

### 不存在则新增

设置 `upsert` 参数为`True`， 更新不存在则新增。

```shell
> db.Quotations.update({'name':'濑川'},{$set:{ 'name' : '濑川', 'description' : '去东关，捣乱的干活'}},{upsert:true})
```

```shell
> db.Quotations.find({})                                             
{ "_id" : ObjectId("6078e9743252cc07e092d204"), "name" : "贾贵", "description" : "这我哪知道呀！我知道她长的嘿！", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "这秤砣也TM炖熟了", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd9"), "name" : "贾贵", "description" : "这我哪知道呀！我知道她长的嘿！", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078ee01249a48b5bb83b936"), "name" : "濑川", "description" : "去东关，捣乱的干活" }
```

发现新增了一条 `name` 为 `濑川` 的文档记录

与此同时， 我建议 使用 `update_one` 方法更新单个文档， 使用 `update_many`  方法更新多个文档

## 删除文档

### 删除匹配查询条件的所有文档

```shell
> db.Quotations.remove({'name':'贾贵'})
WriteResult({ "nRemoved" : 2 })
```

```shell
> db.Quotations.find({})    
{ "_id" : ObjectId("6078ebd395708b77ad7a8bd8"), "name" : "黄金标", "description" : "这秤砣也TM炖熟了", "createDate" : "2021-04-15" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078ee01249a48b5bb83b936"), "name" : "濑川", "description" : "去东关，捣乱的干活" }
```

这样就把 `name` 为 `贾贵`的所有文档记录全都干掉了

### 删除集合中所有文档

```shell
> db.Quotations.remove({})
```

`{}` 表示无条件，默认移除全部文档，等价于删除此集合。

## 查询文档

`MongoDB` 查询数据的通用语法

`db.collection.find(query, projection)`

### 条件查询

指定非 `_id` 字段 查询

```shell
> use 地下交通站
switched to db 地下交通站
> db.Quotations.find({},{'_id':0})
{ "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "name" : "濑川", "description" : "去东关，捣乱的干活" }
{ "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
{ "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```

为了美化输出，可以使用 `pretty()` 方法，此方法对 `sql` 事务不起到任何意义

```shell
db.Quotations.find({},{'_id':0}).pretty()
```

#### `AND` 查询

查询 [ `name` 为 `黄金标` ] 并且 [ `createDate` 为 `2021-04-26` ] 的所有文档记录

```shell
> db.Quotations.find({"name":"黄金标", "createDate":"2021-04-26"})
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```

#### `OR` 查询

查询 [ `name` 为 `贾贵` ] 或者 [ `description` 为 `天下汉奸一般蠢` ] 的所有文档记录

```shell
> db.Quotations.find({$or:[{"name":"贾贵"},{"description": "天下汉奸一般蠢"}]})
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
```

可以看到在这里 `OR` 查询使用了显式操作(`$or` 后接条件列表)， `OR`操作一定是显式的，不存在隐式的`OR`操作。

而上面的 `AND`查询 操作是不是可以尝试也写成 显式操作

```shell
> db.Quotations.find({$and:[{"name":"黄金标"},{"createDate": "2021-04-26"}]})
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```

> 发现也是可以的 ！！
> 

#### `AND` 和 `OR` 联合使用

查询 [ `createDate` 为 `2021-04-18` ] 并且 [ [ `name` 为 `贾贵` ]  或者 [ `description` 为 `天下汉奸一般蠢` ] ] 的所有文档记录

伪sql语句表述为:

`where createDate='2021-04-18' AND (name = '贾贵' OR description = '天下汉奸一般蠢')`

```shell
> db.Quotations.find({"createDate": "2021-04-18", $or: [{"name": "贾贵"},{"description": "天下汉奸一般蠢"}]})
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
```

## 高级查询

### 范围查询、正则查询

- `$lt`   小于
- `$gt`   大于
- `$lte`  小于等于
- `$gte`  大于等于
- `$ne`   不等于
- `$in`   在范围内
- `$nin`  不在范围内

查询创建时间 `大于` `2021-04-17` 的所有文档记录

```shell
> db.Quotations.find({"createDate" : {$gt : "2021-04-17"}})
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```

查询 [ `name` 不等于 `黄金标` ]  并且 [ `createDate` 小于 `2021-04-26` ] 的所有文档记录

```shell
> db.Quotations.find({"name" : {$ne : "黄金标"},"createDate":{$lt : "2021-04-26"}})
{ "_id" : ObjectId("6078ebd395708b77ad7a8bda"), "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "_id" : ObjectId("6078ebd395708b77ad7a8bdb"), "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
```

查询 [ `name` 包含 `黄金标`、`贾贵` ]  并且 [ `createDate` 大于 `2021-04-02` ] 的所有文档记录

```shell
> db.Quotations.find({"name" : {$in : ["黄金标","贾贵"]},"createDate":{$gt : "2021-04-02"}})
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```

- `$regex`   匹配正则
- `$exists`  属性是否存在
- `$type` 类型判断
- `$mod` 数字模操作
- `$text` 文本查询
- `$where` 高级条件查询

利用正则语句匹配 `name` 中带有 `金标` 的所有文档

```shell
> db.Quotations.find({"name":{"$regex":"金标"}})
{ "_id" : ObjectId("6078f0e31e12a856cf9525da"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "_id" : ObjectId("6078f2091e12a856cf9525dd"), "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
```

利用正则语句匹配 以 `我` 开头的 `description` 的所有文档

```shell
> db.Quotations.find({"description":{"$regex":"^我"}})
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
```

利用正则语句匹配 以 `我` 开头、以 `屎` 结尾 `description` 的所有文档

```shell
> db.Quotations.find({"description":{"$regex":"^我.*屎$"}})
{ "_id" : ObjectId("6078f2091e12a856cf9525dc"), "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
```

> 更多高级查询用法各位读者请参考 MongoDB 官方文档

## 聚合函数

### 排序

在 `MongoDB` 中使用 `sort()` 方法对数据进行排序，
`sort()` 方法可以通过参数指定排序的字段， 并使用 `1` 和 `-1` 来指定排序的方式， 其中 `1` 为升序排列，而 `-1` 是用于降序排列。

我们总是喜欢用`时间`维度来排序集合中的文档

```shell
> db.Quotations.find({},{"_id":0}).sort({"createDate":-1})
{ "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。" }
{ "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎" }
{ "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17" }
{ "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16" }
{ "name" : "濑川", "description" : "去东关，捣乱的干活" }
```

### 分组

```shell
db.Quotations.aggregate({$group:{_id:{name:"$name"}}})
```

根据 `name` 和 `description` 字段进行分组

```shell
db.Quotations.aggregate({
    $group:{
        _id:{name:"$name",description:"$description"}
}})
```

由于我们现有集合文档的字段中并没有可计算的数值

我们尝试添加一个集合字段并先赋值为空

```shell
db.Quotations.update({},{$set:{"forceValue": ""}},{multi:true})
```

添加随机值

```shell
db.Quotations.update({"name":"黑藤"},{$set:{"forceValue": Math.random()*100}},{multi:true})
db.Quotations.update({"name":"孙友福"},{$set:{"forceValue": Math.random()*100}},{multi:true})
db.Quotations.update({"name":"濑川"},{$set:{"forceValue": Math.random()*100}},{multi:true})
db.Quotations.update({"name":"黄金标"},{$set:{"forceValue": Math.random()*100}},{multi:true})
db.Quotations.update({"name":"贾贵"},{$set:{"forceValue": Math.random()*100}},{multi:true})
```

结果如下

```text
{ "name" : "黑藤", "description" : "天下汉奸一般蠢", "createDate" : "2021-04-16", "forceValue" : 14.796604243632927 }
{ "name" : "孙友福", "description" : "没有水就没有鱼，没有你就没有驴", "createDate" : "2021-04-17", "forceValue" : 43.71427504449847 }
{ "name" : "濑川", "description" : "去东关，捣乱的干活", "forceValue" : 41.53502198761502 }
{ "name" : "黄金标", "createDate" : "2021-04-26", "description" : "刘副官你记住了，让皇军先尿。", "forceValue" : 21.887495918176125 }
{ "name" : "贾贵", "createDate" : "2021-04-18", "description" : "我啐他一脸狗屎", "forceValue" : 94.18697675337746 }
```


由于要用到分组，我们需要多添加几条文档数据
```shell
db.Quotations.insertMany([
         {name: '黄金标',description: '我黄某人为官一任就得保一方平安',forceValue:Math.random()*100,createDate: '2021-04-11'},
         {name: '贾贵',description: '皇军没来的时候，你欺负我，皇军来了你还欺负我，那皇军不是TM白来了吗',forceValue:Math.random()*100,createDate: '2021-04-14'},
         {name: '黑藤',description: '全东亚乃至全亚洲都找不到第二张想你这么一张空前绝后的脸来',forceValue:Math.random()*100,createDate: '2021-04-22'},
         {name: '贾贵',description: '这我哪知道啊，我就知道她长得嘿',forceValue:Math.random()*100, createDate: '2021-04-19'}
     ])
```

### 分组使用聚合函数

常用聚合函数
- `$sum`
- `$avg`
- `$max`
- `$min`
- `$first`
- `$last`


根据 `name` 分组并使用 `$sum` 函数求和，得到一下结果

- `$match` 查询条件 
- `$group` 根据字段分组(可以是多字段) + 聚合函数 

```shell
> db.Quotations.aggregate(
...     {"$match":{"createDate":{"$gt":"2021-04-07"}}},
...     {"$group":{"_id":"$name",'forceValue':{"$sum":"$forceValue"}}},
... )
{ "_id" : "贾贵", "forceValue" : 204.22774268609504 }
{ "_id" : "黄金标", "forceValue" : 121.14812944012357 }
{ "_id" : "黑藤", "forceValue" : 91.2583132098972 }
{ "_id" : "孙友福", "forceValue" : 43.71427504449847 }
```

这相当于在 `Mysql` 中执行

```shell
select id,sum(forceValue) from Quotations where createDate > "2021-04-07" group by name;  
```

`$avg` 求平均

```shell
> db.Quotations.aggregate(
...     {"$match":{"createDate":{"$gt":"2021-04-07"}}},
...     {"$group":{"_id":"$name",'forceValue':{"$avg":"$forceValue"}}},
... )
{ "_id" : "贾贵", "forceValue" : 68.07591422869835 }
{ "_id" : "黄金标", "forceValue" : 60.574064720061784 }
{ "_id" : "黑藤", "forceValue" : 45.6291566049486 }
{ "_id" : "孙友福", "forceValue" : 43.71427504449847 }
```

### 多字段分组
根据 `createDate` + `name` 进行分组之后求和
```shell
> db.Quotations.aggregate(
... ...     {"$match":{"createDate":{"$gt":"2021-04-07"}}},
... ...     {"$group":{"_id":{"createDate":"$createDate","name":"$name"},'forceValue':{"$sum":"$forceValue"}}},
... ... )
{ "_id" : { "createDate" : "2021-04-11", "name" : "黄金标" }, "forceValue" : 99.26063352194744 }
{ "_id" : { "createDate" : "2021-04-16", "name" : "黑藤" }, "forceValue" : 14.796604243632927 }
{ "_id" : { "createDate" : "2021-04-17", "name" : "孙友福" }, "forceValue" : 43.71427504449847 }
{ "_id" : { "createDate" : "2021-04-18", "name" : "贾贵" }, "forceValue" : 94.18697675337746 }
{ "_id" : { "createDate" : "2021-04-26", "name" : "黄金标" }, "forceValue" : 21.887495918176125 }
{ "_id" : { "createDate" : "2021-04-14", "name" : "贾贵" }, "forceValue" : 81.9931941785778 }
{ "_id" : { "createDate" : "2021-04-22", "name" : "黑藤" }, "forceValue" : 76.46170896626427 }
{ "_id" : { "createDate" : "2021-04-19", "name" : "贾贵" }, "forceValue" : 28.04757175413979 }
```
 :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada: :tada:

> 我不能再继续写下去了，`MongoDB` 的基础入门就介绍到这里 :beer:

> 更多教程请参考 [MongoDB官方文档](https://mongodb.net.cn/)

