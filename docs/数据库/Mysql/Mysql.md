`MySQL` 是一个`关系型`数据库管理系统， 由瑞典 `MySQL AB` 公司开发，目前属于 `Oracle` 公司。

`MySQL` 是一种关联数据库管理系统，关联`数据库`将数据保存在不同的`表`中， 而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

`Mysql` 是当下最主流的`关系型`数据库。


> 非严格意义上来说，`Mysql` 只需要服务端和客户端

所谓服务端就是安装的`Mysql服务`，我们需要先启动 `Mysql` 服务，然后使用客户端登陆操作`Mysql`事务。

客户端可以是命令行终端，也可以是某款强大的数据库可视化工具。

> 这里假设你已经安装了 Mysql 并成功启动，请参照 `Mysql 安装章节`

## 连接 `Mysql`

### 登陆 `Mysql` 数据库
`-h` 指定主机、`-P` 指定端口、`-u` 指定用户名、`-p` 指定密码

```shell
[root@gzky_gz ~]# mysql -uroot -p123456
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3797
Server version: 5.7.29 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

> 看到以上的提示信息意味着你已经成功进入 `Mysql` 数据库，✋ 恭喜你 ！！

键入 `exit` 离开 `Mysql`

```shell
mysql> exit
Bye
```

## 创建`数据库`、`数据表`

首先查看当前实例中的数据库列表

```shell
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| blog_db            |
| bookshop           |
| djangoDB           |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
7 rows in set (0.00 sec)
```

### 创建一个数据库 `hello_life`

```shell
mysql> create database hello_life;
Query OK, 1 row affected (0.01 sec)
```

再次查看数据库列表，发现已经创建成功

```shell
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| blog_db            |
| bookshop           |
| djangoDB           |
| hello_life         |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
8 rows in set (0.00 sec)
```

### 创建一个数据表 `Quotations`

```shell
CREATE TABLE IF NOT EXISTS `Quotations`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` VARCHAR(30) NOT NULL,
   `description` VARCHAR(100) NOT NULL,
   `createDate` DATE,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

- `NOT NULL` 说明该字段是 `非空` 字段， 在操作数据库时如果输入该字段的数据为`NULL` ，就会报错。
- `AUTO_INCREMENT` 定义列为自增的属性，一般用于主键，自增长，数值会自动加 `1`。
- `PRIMARY KEY` 关键字用于定义列为`主键`。 您可以使用多列来定义`主键`，列间以逗号分隔。
- `ENGINE` 设置存储引擎，`CHARSET` 设置编码。

```shell
mysql> use hello_life;
Database changed
mysql> 
mysql> CREATE TABLE IF NOT EXISTS `Quotations`(
    ->    `id` INT UNSIGNED AUTO_INCREMENT,
    ->    `name` VARCHAR(30) NOT NULL,
    ->    `description` VARCHAR(100) NOT NULL,
    ->    `createDate` DATE,
    ->    PRIMARY KEY ( `id` )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
Query OK, 0 rows affected (0.02 sec)
```

我们进入数据库 `hello_life` 并成功创建了数据表 `Quotations`

查看一下表结构

```shell
desc Quotations;
```

```shell
mysql> desc Quotations;
+-------------+------------------+------+-----+---------+----------------+
| Field       | Type             | Null | Key | Default | Extra          |
+-------------+------------------+------+-----+---------+----------------+
| id          | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name        | varchar(30)      | NO   |     | NULL    |                |
| description | varchar(100)     | NO   |     | NULL    |                |
| createDate  | date             | YES  |     | NULL    |                |
+-------------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

> Mysql 中以 `;` 作为 `sql` 语句的结尾

## 插入数据

```shell
mysql> INSERT INTO Quotations (name, description, createDate) VALUES ("小妮", "今天的饭还没白嫖，还不能下班", NOW());
Query OK, 1 row affected, 1 warning (0.00 sec)
```

查看表数据

```shell
mysql> select * from Quotations;
+----+--------+--------------------------------------------+------------+
| id | name   | description                                | createDate |
+----+--------+--------------------------------------------+------------+
|  1 | 小妮   | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
+----+--------+--------------------------------------------+------------+
1 row in set (0.00 sec)
```

目前为止一切顺利 :pray:

### :pencil2: 尝试插入多条数据

```shell
mysql> INSERT INTO Quotations  (name, description, createDate) VALUES 
    -> ("小妮", "今天的饭还没白嫖，还不能下班", NOW()),
    -> ("杨老板", "别吧", NOW()),
    -> ("陈梦游", "都别太晚了，都早点回去吧", NOW());
Query OK, 3 rows affected, 3 warnings (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 3
```

嗯，看起来没有问题 ！！再次查看数据表记录 :blush:

```shell
mysql> select * from Quotations;
+----+-----------+--------------------------------------------+------------+
| id | name      | description                                | createDate |
+----+-----------+--------------------------------------------+------------+
|  1 | 小妮      | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  2 | 小妮      | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  3 | 杨老板    | 别吧                                       | 2021-04-16 |
|  4 | 陈梦游    | 都别太晚了，都早点回去吧                   | 2021-04-16 |
+----+-----------+--------------------------------------------+------------+
4 rows in set (0.00 sec)
```

## 更新数据

```shell
mysql> UPDATE Quotations SET description='我从来没有见过这么废物的人' WHERE name='杨老板';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from Quotations;
+----+-----------+--------------------------------------------+------------+
| id | name      | description                                | createDate |
+----+-----------+--------------------------------------------+------------+
|  1 | 小妮      | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  2 | 小妮      | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  3 | 杨老板    | 我从来没有见过这么废物的人                 | 2021-04-16 |
|  4 | 陈梦游    | 都别太晚了，都早点回去吧                   | 2021-04-16 |
+----+-----------+--------------------------------------------+------------+
4 rows in set (0.00 sec)
```

从结果上看，`name` 为 `杨老板` 的 `description` 字段已被修改。

:pencil: 更新多个字段
```shell
mysql> UPDATE Quotations SET description='我从来没有见过这么废物的人',name='杨boss' WHERE name='杨老板';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from Quotations;
+----+-----------+--------------------------------------------+------------+
| id | name      | description                                | createDate |
+----+-----------+--------------------------------------------+------------+
|  1 | 小妮      | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  2 | 小妮      | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  3 | 杨boss    | 我从来没有见过这么废物的人                 | 2021-04-16 |
|  4 | 陈梦游    | 都别太晚了，都早点回去吧                   | 2021-04-16 |
+----+-----------+--------------------------------------------+------------+
4 rows in set (0.00 sec)
```
## 删除数据
```shell
mysql> DELETE FROM Quotations WHERE name='陈梦游';
Query OK, 1 row affected (0.00 sec)

mysql> select * from Quotations;
+----+---------+--------------------------------------------+------------+
| id | name    | description                                | createDate |
+----+---------+--------------------------------------------+------------+
|  1 | 小妮    | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  2 | 小妮    | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  3 | 杨boss  | 我从来没有见过这么废物的人                 | 2021-04-16 |
+----+---------+--------------------------------------------+------------+
3 rows in set (0.00 sec)
```
成功删除了 `name` 为 `陈梦游` 的记录

## 查询数据

`select` 的通用写法 :mag_right: 
```shell
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```

- `SELECT` 命令可以读取一条或者多条记录。
- 使用星号（`*`）来代替其他字段，`SELECT` 语句会返回表的`所有字段`数据
- 使用 `WHERE` 语句来包含任何条件。
- 使用 `LIMIT` 属性来设定返回的记录数。
- 通过 `OFFSET` 指定 `SELECT` 语句开始查询的数据偏移量。默认情况下偏移量为 `0`。多用于`分页`操作。

```shell
mysql> SELECT name FROM Quotations;
+---------+
| name    |
+---------+
| 小妮    |
| 小妮    |
| 杨boss  |
+---------+
3 rows in set (0.00 sec)
```

```shell
mysql> select * from Quotations;
+----+---------+--------------------------------------------+------------+
| id | name    | description                                | createDate |
+----+---------+--------------------------------------------+------------+
|  1 | 小妮    | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  2 | 小妮    | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
|  3 | 杨boss  | 我从来没有见过这么废物的人                 | 2021-04-16 |
+----+---------+--------------------------------------------+------------+
3 rows in set (0.00 sec)
```
```shell
mysql> select name,description from Quotations WHERE createDate='2021-04-16'; 
+---------+--------------------------------------------+
| name    | description                                |
+---------+--------------------------------------------+
| 小妮    | 今天的饭还没白嫖，还不能下班               |
| 小妮    | 今天的饭还没白嫖，还不能下班               |
| 杨boss  | 我从来没有见过这么废物的人                 |
+---------+--------------------------------------------+
3 rows in set (0.00 sec)
```
```shell
mysql> select * from Quotations WHERE createDate='2021-04-16' LIMIT 1; 
+----+--------+--------------------------------------------+------------+
| id | name   | description                                | createDate |
+----+--------+--------------------------------------------+------------+
|  1 | 小妮   | 今天的饭还没白嫖，还不能下班               | 2021-04-16 |
+----+--------+--------------------------------------------+------------+
1 row in set (0.00 sec)
```

接下来我们更改一下字段的类型，将 `createDate` 字段的 `date` 改为 `datetime` 类型
```shell
mysql> ALTER TABLE Quotations MODIFY createDate DATETIME;
Query OK, 3 rows affected (0.06 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> desc Quotations;
+-------------+------------------+------+-----+---------+----------------+
| Field       | Type             | Null | Key | Default | Extra          |
+-------------+------------------+------+-----+---------+----------------+
| id          | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name        | varchar(30)      | NO   |     | NULL    |                |
| description | varchar(100)     | NO   |     | NULL    |                |
| createDate  | datetime         | YES  |     | NULL    |                |
+-------------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

```shell
mysql> select * from Quotations;
+----+---------+--------------------------------------------+---------------------+
| id | name    | description                                | createDate          |
+----+---------+--------------------------------------------+---------------------+
|  1 | 小妮    | 今天的饭还没白嫖，还不能下班               | 2021-04-16 00:00:00 |
|  2 | 小妮    | 今天的饭还没白嫖，还不能下班               | 2021-04-16 00:00:00 |
|  3 | 杨boss  | 我从来没有见过这么废物的人                 | 2021-04-16 00:00:00 |
+----+---------+--------------------------------------------+---------------------+
3 rows in set (0.00 sec)
```

发现`createDate` 的类型已经发生了改变

我们往数据表中多添加几条数据
```shell
mysql> INSERT INTO Quotations  (name, description, createDate) VALUES 
    ->     ("小妮", "现在接驳车人太多了，还不能下班", NOW()),
    ->     ("杨老板", "废物", NOW()),
    ->     ("陈梦游", "这都是潜在需求来的", NOW()),
    ->     ("陈梦游", "我跟你们两个谈一下", NOW()),
    ->     ("陈梦游", "你扯淡", NOW());
Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0
```

看一下现在表中的数据量
```shell
mysql> select count(*) from Quotations;
+----------+
| count(*) |
+----------+
|        8 |
+----------+
1 row in set (0.00 sec)
```

### LIKE

- 可以在 `WHERE` 子句中指定任何条件。
- 可以在 `WHERE` 子句中使用`LIKE`子句。
- `LIKE` 通常与 `%` 一同使用，类似于一个元字符的搜索。
- 可以使用 `AND` 或者 `OR` 指定一个或多个条件。
- 可以在 `DELETE` 或 `UPDATE` 命令中使用 `WHERE`...`LIKE` 子句来指定条件。


查询所有 `name` 以 `老板` 结尾的数据结果
```shell
mysql> SELECT * from Quotations  WHERE name LIKE '%老板';
+----+-----------+-------------+---------------------+
| id | name      | description | createDate          |
+----+-----------+-------------+---------------------+
|  6 | 杨老板    | 废物        | 2021-04-16 12:00:46 |
+----+-----------+-------------+---------------------+
1 row in set (0.00 sec)
```


查询所有 `description` 以 `今天` 开头的数据结果
```shell
mysql> SELECT * from Quotations  WHERE description LIKE '今天%';
+----+--------+--------------------------------------------+---------------------+
| id | name   | description                                | createDate          |
+----+--------+--------------------------------------------+---------------------+
|  1 | 小妮   | 今天的饭还没白嫖，还不能下班               | 2021-04-16 00:00:00 |
|  2 | 小妮   | 今天的饭还没白嫖，还不能下班               | 2021-04-16 00:00:00 |
+----+--------+--------------------------------------------+---------------------+
2 rows in set (0.00 sec)
```


查询所有 `description` 中包含 `下班` 的数据结果
```shell
mysql> SELECT * from Quotations  WHERE description LIKE '%下班%';
+----+--------+-----------------------------------------------+---------------------+
| id | name   | description                                   | createDate          |
+----+--------+-----------------------------------------------+---------------------+
|  1 | 小妮   | 今天的饭还没白嫖，还不能下班                  | 2021-04-16 00:00:00 |
|  2 | 小妮   | 今天的饭还没白嫖，还不能下班                  | 2021-04-16 00:00:00 |
|  5 | 小妮   | 现在接驳车人太多了，还不能下班                | 2021-04-16 12:00:46 |
+----+--------+-----------------------------------------------+---------------------+
3 rows in set (0.01 sec)
```


### 与 `AND`、`OR` 结合使用

查询所有 [ `name` 为 `小妮` ] 并且 [ `description` 中包含 `接驳车` ] 的数据结果
```shell
mysql> SELECT * from Quotations  WHERE name='小妮' and description LIKE '%接驳车%';
+----+--------+-----------------------------------------------+---------------------+
| id | name   | description                                   | createDate          |
+----+--------+-----------------------------------------------+---------------------+
|  5 | 小妮   | 现在接驳车人太多了，还不能下班                | 2021-04-16 12:00:46 |
+----+--------+-----------------------------------------------+---------------------+
1 row in set (0.00 sec)
```


查询所有 [ `name` 以 `梦游` 结尾 ] 或者 [ `description` 中包含 `废物` ] 的数据结果
```shell
mysql>  SELECT * from Quotations  WHERE name LIKE '%梦游' or description LIKE '%废物%';
+----+-----------+-----------------------------------------+---------------------+
| id | name      | description                             | createDate          |
+----+-----------+-----------------------------------------+---------------------+
|  3 | 杨boss    | 我从来没有见过这么废物的人              | 2021-04-16 00:00:00 |
|  6 | 杨老板    | 废物                                    | 2021-04-16 12:00:46 |
|  7 | 陈梦游    | 这都是潜在需求来的                      | 2021-04-16 12:00:46 |
|  8 | 陈梦游    | 我跟你们两个谈一下                      | 2021-04-16 12:00:46 |
|  9 | 陈梦游    | 你扯淡                                  | 2021-04-16 12:00:46 |
+----+-----------+-----------------------------------------+---------------------+
5 rows in set (0.00 sec)
```


### 排序 `ORDER BY`

- 使用任何字段来作为排序的条件，从而返回排序后的查询结果。
- 可以设定`多个字段`来排序。
- 可以使用 `ASC` 或 `DESC` 关键字来设置查询结果是按`升序`或`降序`排列。 默认情况下，它是按`升序`排列。
- 可以添加 `WHERE`...`LIKE` 子句来设置条件。

假如我们希望用时间来排序 `Quotations` 表数据
```shell
mysql> SELECT * from Quotations ORDER BY createDate ASC;
+----+--------+--------------------------------+---------------------+
| id | name   | description                    | createDate          |
+----+--------+--------------------------------+---------------------+
|  1 | 小妮   | 今天的饭还没白嫖，还不能下班   | 2021-04-16 00:00:00 |
|  2 | 小妮   | 今天的饭还没白嫖，还不能下班   | 2021-04-16 00:00:00 |
|  3 | 杨boss | 我从来没有见过这么废物的人     | 2021-04-16 00:00:00 |
|  5 | 小妮   | 现在接驳车人太多了，还不能下班 | 2021-04-16 12:00:46 |
|  6 | 杨老板 | 废物                           | 2021-04-16 12:00:46 |
|  7 | 陈梦游 | 这都是潜在需求来的             | 2021-04-16 12:00:46 |
|  8 | 陈梦游 | 我跟你们两个谈一下             | 2021-04-16 12:00:46 |
|  9 | 陈梦游 | 你扯淡                         | 2021-04-16 12:00:46 |
| 10 | 杨老板 | 别吧                           | 2021-04-16 13:29:02 |
| 11 | 陈梦游 | 低标准                         | 2021-04-16 13:29:28 |
+----+--------+--------------------------------+---------------------+
10 rows in set (0.22 sec)
```
### 分组 `GROUP BY`

- `GROUP BY` 语句根据一个或多个列对结果集进行`分组`。
- 结合使用诸如 `COUNT`, `SUM`, `AVG` 等`聚合函数`。

统计每个人说了多少句话
```shell
mysql> SELECT name,count(*) FROM  Quotations GROUP BY name;
+--------+----------+
| name   | count(*) |
+--------+----------+
| 小妮   |        2 |
| 杨boss |        1 |
| 杨老板 |        2 |
| 陈梦游 |        4 |
+--------+----------+
4 rows in set (0.10 sec)
```

多字段分组，`人物` 并上 `时间` 之后分组
```shell
mysql> SELECT name,createDate FROM  Quotations GROUP BY name,createDate;
+--------+---------------------+
| name   | createDate          |
+--------+---------------------+
| 小妮   | 2021-04-16 00:00:00 |
| 小妮   | 2021-04-16 12:00:46 |
| 杨boss | 2021-04-16 00:00:00 |
| 杨老板 | 2021-04-16 12:00:46 |
| 杨老板 | 2021-04-16 13:29:02 |
| 陈梦游 | 2021-04-16 12:00:46 |
| 陈梦游 | 2021-04-16 13:29:28 |
+--------+---------------------+
7 rows in set (0.09 sec)
```

### `连接` 和 `UNION` 操作

## 日志

当你熟练的使用并依赖于 `Mysql` 数据库，就会有大量的事务操作。

所以学会查看 `Mysql` 日志是一项非常重要的技能，也是一种不可或缺的手段，
当你运行 `sql` 错误时，`可追溯日志`能帮助你更快速的找到报错信息。

`MySQL`的查询日志记录了所有`MySQL`数据库请求的信息。
无论这些请求是否得到了正确的执行。

默认文件名为`hostname.log`，比如你的主机名为 `TongGe`，那么默认的日志文件名称为 `TongGe.log`

默认情况下`MySQL`查询日志是关闭的，需要手动开启。

事实上 `Mysql日志`可以分为
- `错误日志`  默认开启
- `查询日志`  默认不开启
- `慢查询日志` 默认不开启
- `事务日志` 
- `二进制日志` 默认不开启

由于篇幅原因，这里不做详述。

### 查看 `Mysql` 是否开始`查询日志`文件

```shell
mysql> show variables like '%general_log%';
+------------------+------------------------------+
| Variable_name    | Value                        |
+------------------+------------------------------+
| general_log      | OFF                          |
| general_log_file | /var/lib/mysql/gzky_gz.log |
+------------------+------------------------------+
2 rows in set (0.00 sec)
```

- `general_log_file` 日志查询路径
- `general_log` 为 `off` 意味着没有开启日志文件

手动开启日志查询文件
```shell
mysql> set global general_log = on;
Query OK, 0 rows affected (0.11 sec)
```

再次查看日志开启状态
```shell
mysql> show variables like '%general_log%';
+------------------+----------------------------+
| Variable_name    | Value                      |
+------------------+----------------------------+
| general_log      | ON                         |
| general_log_file | /var/lib/mysql/gzky_gz.log |
+------------------+----------------------------+
2 rows in set (0.07 sec)
```


进入日志文件查看，大概是这样的
```shell
2021-04-16T09:32:13.349963Z      3945 Query     SELECT COUNT(1) FROM `hello_life`.`Quotations`
2021-04-16T09:32:13.358211Z      3946 Init DB   hello_life
2021-04-16T09:32:13.365344Z      3946 Query     SHOW CREATE TABLE `Quotations`
2021-04-16T09:32:13.372716Z      3946 Init DB   hello_life
2021-04-16T09:32:13.379601Z      3946 Query     SHOW CREATE TABLE `Quotations`
2021-04-16T09:32:13.387214Z      3946 Init DB   hello_life
2021-04-16T09:32:13.395007Z      3946 Query     SHOW FULL COLUMNS FROM `Quotations`
2021-04-16T09:32:13.406751Z      3945 Query     SELECT * FROM `hello_life`.`Quotations`
2021-04-16T09:32:13.440777Z      3946 Init DB   hello_life
2021-04-16T09:32:13.468873Z      3946 Query     SHOW CREATE PROCEDURE `query_data`   
2021-04-16T09:33:08.812569Z      3912 Init DB   hello_life
2021-04-16T09:33:08.821059Z      3912 Query     SHOW PROCEDURE STATUS WHERE Db = 'hello_life'
2021-04-16T09:33:08.827492Z      3912 Query     SHOW FUNCTION STATUS WHERE Db = 'hello_life'
2021-04-16T09:33:08.835250Z      3912 Query     SELECT * FROM information_schema.ROUTINES WHERE ROUTINE_SCHEMA = 'hello_life' ORDER BY ROUTINE_NAME
```

> 这样我们就能知道 `Mysql` 在某些时刻做了那些事务操作和详细的运行步骤 ！！


