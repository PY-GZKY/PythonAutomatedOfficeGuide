
## 安装 `Python`

基于 `Anaconda` 搭建 `Python` 环境


### 安装`Anaconda`

不管是`Windows`或`Linux(Mac)` 系统都推荐使用`Anaconda`搭建`Python`环境，这是一个绝佳的选择。

`Windows` 下安装 `Anaconda` 看起来只需要傻瓜式操作，最后再把它放入环境变量即可，这里不在详述 :smile:

### `Linux` 下安装`Anaconda`

这里以`Centos7`为例
```shell
$ yum update &&
  yum -y install wget &&
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&
  bash ./Miniconda3-latest-Linux-x86_64.sh
```

由于某些原因，默认的`anaconda` 站点`wget`可能会比较慢，可以选择国内的镜像源平台进行安装，比如清华源就很优秀。

> [清华镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/)

选择你适应的平台和系统版本，`wget` 下载至本地即可。

```shell
$ wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.03-Linux-x86_64.sh
```

至于安装步骤，一路按确认键即可，配置环境变量并让它生效

```shell
vi /etc/profile
```
在文件最尾端加入一下路径，比如我把安装目录放在了 `root` 下

```shell
PATH=$PATH:/root/anaconda3/bin
export PATH
```
```shell
$ source /etc/profile
```

查看当前的 Python 环境
```shell
[root@gzky_gz ~] conda --version
conda 4.9.2
[root@gzky_gz ~] python
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

> 至此，Anaconda安装完毕 ！！


### `pip` 包管理工具

我们使用 `pip` 作为`Python`的包管理工具，安装 `anaconda` 完毕之后，我们
可以在黑窗口中键入 
`pip -V` 来查看 pip 版本

## 安装依赖库

在 Python 中，我们可以通过 pip 工具进行第三方库的安装，这也是最快、最简单的安装方式。

```shell
pip install PyMysql
```

但是由于一些第三方扩展存放于海外服务器，由于众所周知的原因我们无法通过正常手段获取，可以使用 -i 参数
指定源，加速安装扩展库:
```shell
pip install PyMysql -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## `Python` 虚拟环境

成功安装 `Python` 之后默认只提供一个版本，比如 `Python3.7`

> 这对于习惯切换多版本开发的小伙伴可就不太友好了 ！！

所以，为了兼容不同`Python`版本共同开发，我们需要使用 `Python` 虚拟环境

由于我们前面是使用 `conda` 搭建的 `Python` 环境，而 `conda` 也提供了 `Python`的虚拟环境，可以切换到不同的`Python`
版本进行开发，不同版本之间相互隔离，是一个独立的操作环境 ！！

这里假设读者本地默认安装了 `Python3.7` 版本

### 创建一个新的虚拟环境

```shell
# Python 3.6  
$ conda create -n venv_3.6 python=3.6   

# Python 3.8 
$ conda create -n venv_3.8 python=3.8
```

其中 `-n` 指定了虚拟环境的名称，可以随便起，后面跟着 `Python` 和指定`版本号`

查看创建的虚拟环境列表

```shell
> conda env list
# conda environments:
#
base                  *  D:\conda3
venv_3.6                 D:\conda3\envs\venv_3.6
venv_3.8                 D:\conda3\envs\venv_3.8
```

> 可以看到刚才创建的环境已经有了

### 激活并进入虚拟环境

```shell
Linux:   source activate venv
Windows: activate venv
```

### 安装 `pipenv`

```shell
pip install pipenv
```

进入新的虚拟环境会发现很多第三方工具和扩展包需要重新安装，比如 `PyMysql` 等等

想往常一样执行 `pip install pymysql` 安装第三方扩展即可

### 删除一个现有的虚拟环境

```shell
# 将清空所有
conda remove --name venv --all 
```

> 注意，如果是`Pycharm`编辑器的话可以将设置中的项目控制中的`Python`解释器路径更改为 `venv` 的路径，更改生效后，这就意味着你已经进入了新的`Python`版本环境


## 编辑器

在 `Python` 中我们推荐使用 `Pycharm` 编辑器来进行代码开发，这也是现在最主流的`Python` 编辑器了。

如果你经常和数据表格打交道，我强烈建议你使用 `Jupyter NoteBook`。



## `Node` | `Npm`

> `nodejs`： [https://nodejs.org/en/download](https://nodejs.org/en/download/)

这里主要说说 `Linux` 下如何安装 `Node` 和 `Npm`，`windows` 安装 `node` 不再赘述。

- 进入官方下载页面后，根据自己系统选择 `Linux Binaries (x64)` 或 `Linux Binaries (ARM)`，我这里是
`Linux Binaries (x64)`，下载到本地后`解压`即可。

- `Linux` 一般的软件存放目录是 `/opt`，我们把它存在这里。
- 软链接到 `/usr/local/bin/` 目录，为了能够全局作用与 `node` 和 `npm`，我们还需要将其软链接到 `/usr/local/bin/` 目录


```shell
sudo ln -s /opt/node/bin/node /usr/local/bin/node
sudo ln -s /opt/node/bin/npm /usr/local/bin/npm
```

- 如果`软链接`不可用或失效，可以直接将 `/opt/node` 加入到环境变量中

```shell
vi /etc/profile
```

添加至最后一行即可
```shell
export PATH=$PATH:/opt/node/bin
```

生效
```shell
source /etc/profile
```

验证，查看版本信息
```shell
node -V
npm -V
```
