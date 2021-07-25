## 面向对象的数据库编程
除了使用 `PyMysql`、`MysqlDB` 这些库之外，还有一种被称之为 `orm` 的概念，即`面向对象`的数据库编程。

在 `Python` 中我们经常使用 `Sqlalchemy` 


## Sqlalchemy

简单用法如下
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists,create_database

# 1)连接数据库引擎
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/blog?charset=utf8')

# 2)创建基类
Base = declarative_base()

# 3)初始化session
Session = sessionmaker(bind=engine)

# 4)创建session对象
session = Session()

# 5)创建数据库
if not database_exists(engine.url):
    create_database(engine.url)

```

### `模型类`/`实体类`

数据库中的表在编程语言中的体现，其本质就是一个 `python` 的`模型类`（在`java`和其他语言中称为`实体类`）。属性要与数据库表中的列相对应。

### 语法

大致语法如下
```shell
class MODELNAME(Base):
    __tablename__ = 'TABLENAME'
    COLUMN_NAME = Column(TYPE,OPTIONS)
```

- MODELNAME: 定义模型名称，根据表名设定
- TABLENAME: 映射到数据库中表的名字
- COLUMN_NAME: 属性名，映射到表中列的名字
- db.TYPE: 映射到列的数据类型
- OPTIONS: 列选项

#### `db.TYPE` 列类型
    类型                     python类型              说明
    Integer                 int                     普通整数，32位
    SmallInteger            int                     小范围整数，通常16位
    BigInteger              int/long                不限精度的整数
    Float                   float                   浮点数
    Numeric                 decimal.Decimal         定点数
    String                  str                     变长字符串
    Text                    str                     变长字符串，优化
    Unicode                 unicode                 变长Unicode字符串
    UnicodeText             unicode                 优化后的变长Unicode字符串
    Boolean                 bool                    布尔值
    Date                    datetime.date           日期
    Time                    datetime.time           时间
    DateTime                datetime.datetime       日期和时间

#### `OPTIONS` 列选项
    primary_key             主键
    unique                  唯一约束
    index                   创建索引
    nullable                运行为空
    default                 设置默认值

#### 基本使用
```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key = True)
    username = Column(String(30),nullable=Flase)
```

- 声明了一个用户实体类 `User`
- 映射的表名称为 `user`
- 字段 `id`(主键)、`username` 分别为 `int`、`string` 类型