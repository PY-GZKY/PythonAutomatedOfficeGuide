


## 常见异常

- `AttributeError`: 调用不存在的方法引发的异常
- `EOFError`:  遇到文件末尾引发的异常
- `ImportError`: 导入模块出错引发的异常
- `IndexError`: 列表越界引发的异常
- `IOError`: `I/O` 操作引发的异常，如打开文件出错等
- `KeyError`: 使用字典中不存在的关键字引发的异常
- `NameError`: 使用不存在的变量名引发的异常
- `TabError`: 语句块缩进不正确引发的异常
- `ValueError`: 搜索列表中不存在的值引发的异常
- `ZeroDivisionError`: 除数为零引发的异常


## traceback模块

> `traceback`: 打印或读取堆栈的跟踪信息

```python
try:
    1/0
except Exception as e:
    print(e)
```

首先，上面的代码只能帮助我们得到 `division by zero` 错误，但是我们并不知道是在哪个文件哪个函数哪一行出的错

```python
import traceback
try:
    1/0
except Exception as e:
    traceback.print_exc()
```

用 `traceback` 模块能自主的追溯到执行出错的准确地方

```text
Traceback (most recent call last):
  File "_.py", line 4, in <module>
    1/0
ZeroDivisionError: division by zero
```

关于 的一些基本用法:

```python
import sys, traceback

def lumberjack():
    return tuple()[0]

try:
    lumberjack()
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    # print(exc_type, exc_value, exc_traceback)

    # print("*** print_tb:")
    # traceback.print_tb(exc_traceback, limit=4, file=sys.stdout)

    # print("*** print_exception:")
    # traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)

    print("*** print_exc:")
    traceback.print_exc(limit=2, file=sys.stdout)

    print("*** format_exc:")
    format_exc = traceback.format_exc()
    print(format_exc)
```

`format_exc()` 返回字符串，`print_exc()`则直接给打印出来。即`traceback.print_exc()`与`print(traceback.format_exc())`效果是一样的。`print_exc()`还可以接受`file`参数直接写入到一个文件。比如可以像下面这样把相关信息写入到`tb.txt`文件去

```python
traceback.print_exc(file=open('tb.txt','w+'))
```

当然也可以直接打印和格式化堆栈

```python
traceback.print_stack()
print(repr(traceback.extract_stack()))
print(repr(traceback.format_stack()))
```

`traceback` 对程序运行异常的捕获或读取堆栈的跟踪信息具有很大的意义

## 如何在 `Python` 中进行代码调试

`debug`(程序调试) 是一个程序员的基本能力，同时也是一项重要的技能。
`debug`能让你正确的知道 `Python` 代码在运行过程中到底发生了什么

- `Bug` 臭虫，功能性、逻辑性错误
- `Debug` 调试程序，找到程序`bug`的过程


## `断言`和`异常`抛出

我们来看一段简单的具有潜在 `bug` 的程序

```python
def isBug(x, y):
    return x / y

print(isBug(16, 4))
```

我们都知道在进行除法的时候分母不为 `0`，当分母为 `0` 时将会抛出`异常`

```shell
In [12]: print(isBug(1, 0))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-12-5dbd93613fbe> in <module>
----> 1 print(isBug(1, 0))

<ipython-input-9-868b719664dd> in isBug(x, y)
      1 def isBug(x, y):
----> 2     return x / y
      3

ZeroDivisionError: division by zero
```

## 程序调试
#### 最简单的 `Print`
`print` 可能是你初识 `Python` 之后用的第一个函数，它能最直观的把日志信息输出到控制台。

如果我们需要更多格式和等级的日志输出，则会用到一些第三方的日志库，这里推荐  
## Pycharm断点调试