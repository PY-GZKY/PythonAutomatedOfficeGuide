> 一些比较常见的配置

![Selenium](https://img.shields.io/badge/Selenium-3.7+-blue)
![Pyppeteer](https://img.shields.io/badge/Pyppeteer-3.7+-blue)
![Appium](https://img.shields.io/badge/Python-3.7+-blue)


![openpyxl](https://img.shields.io/badge/openpyxl-10-brightgreen)
![xlwings](https://img.shields.io/badge/xlwings-3+-blue)
![Python-docx](https://img.shields.io/badge/docx-2-blue)
![pptx](https://img.shields.io/badge/pptx-3.7+-blue)
![PyPDF2](https://img.shields.io/badge/PyPDF2-3.7+-blue)
![Email](https://img.shields.io/badge/Email-3.7+-blue)


![Requests](https://img.shields.io/badge/Requests-3.7+-blue)
![lxml](https://img.shields.io/badge/lxml-3.7+-blue)

## `CentOS` 系统 `python` 默认版本 `python2` 改为 `python/python3`

　CentOS中如果安装有yum，一般会有python2的某个版本。
 
一般而言如果没有环境覆盖之前、命令行键入`python`，出现的是`python2`的环境


```shell
[root@instance-hrnebyqu src]# python
Python 2.7.5 (default, Apr 11 2018, 07:36:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
　
```

实际上输入 `python/python2` 出来的环境都是 `python2` 版本。而这显然不是我们想要的。


我们希望将`python`这个`shell`指令连接到`python3`的版本。

这里首先装`python3`，然后将`python`连接到`python3`上。(见`初始化-安装`章节)

本质上就是一个软链接的指向。

由于路径添加到了`bash_profile`文件中的`PATH`中了，因此`环境变量`不需要再改了。


```shell
vim ~/.bash_profile
```
把 `Python3` 的路径加上，然后重载 `bash_profile`这个文件

接着修改bashrc这个文件
```shell
vim ~/.bashrc
```

将 `python2` 和 `python3` 的路径都写上，并将 `python` 指定为 `python3`

```shell
alias python2=/usr/bin/python
alias python3=/usr/local/python3/bin/python3
alias python=/usr/local/python3/bin/python3
```

当然了，如果你安装的事 `conda` 环境，这里加入你的安装路径是 `/root/miniconda3/bin/python`
那么:
```shell
alias python2=/usr/bin/python
alias python=/root/miniconda3/bin/python
```

最后让他生效即可
```shell
source  ~/.bashrc
```
> 这样，命令行开 python 就是 python3 的环境了。

```shell
[root@instance-hrnebyqu src]# python
Python 3.9.0 (default, Jul  4 2019, 12:00:29) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.　　
```
