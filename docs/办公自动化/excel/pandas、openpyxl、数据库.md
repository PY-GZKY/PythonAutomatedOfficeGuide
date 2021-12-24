## Pandas 快速开始

安装 pandas 以及相关依赖
> 请确认已经安装了xlrd, xlwt, openpyxl 这三个包

```shell
pip install pandas==1.3.0
pip install xlrd # xlrd 版本不得高于2.0.0
pip install xlwt 
pip install openpyxl
```

```python
import pandas as pd
pd.__version__ # 1.3.0
```

## 文件的读取和写入
pandas支持多种文件格式的读取、这里主要介绍读取csv, excel, txt 文件格式、其余格式请自行扩展。
```python
import pandas as pd
df_csv = pd.read_csv('../data/xhs_chengdu.csv', r=None)
print(df_csv.head(10))
```

```python
import pandas as pd
df_csv = pd.read_csv('../data/xhs_chengdu.xlsx')
print(df_csv.head(10))
```


```python
import pandas as pd
df_csv = pd.read_csv('../data/xhs_chengdu.txt')
print(df_csv.head(10))
```



```text

```

```shell

```
> 如表格格式有错乱、笔者推荐使用 jupyter notebook 


## 常用方法的使用

## 缺失值的处理

## pandas 进阶使用

## 文件转储(与数据库交互)