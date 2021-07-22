`debug`(程序调试) 是一个程序员的基本能力，同时也是一项重要的技能。
`debug`能让你正确的知道 `Python` 代码在运行过程中到底发生了什么

- `Bug` 臭虫，功能性、逻辑性错误
- `Debug` 调试程序，找到程序`bug`的过程


### 如何在 `Python` 中进行代码调试

### `Log`、`Print`

#### 最简单的 `Print`
`print` 可能是你初识 `Python` 之后用的第一个函数，它能最直观的把日志信息输出到控制台。

如果我们需要更多格式和等级的日志输出，则会用到一些第三方的日志库，这里推荐  





### `断言`和`异常`抛出

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
### 断点调试