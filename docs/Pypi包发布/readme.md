
## 依赖
```shell
pip install setuptools
pip install twine
```

## 打包上传
```shell
python setup.py sdist
twine upload dist/*
```

## 安装
```shell
pip install package_name
```

## setup.py demo
```python
from os import path as os_path
from setuptools import setup

import haipproxy

this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name='haipproxy',  # 包名
    python_requires='>=3.4.0', # python环境
    version=haipproxy.__version__, # 包的版本
    description="High aviariable proxy pool client for crawlers.",  # 包简介，显示在PyPI上
    long_description=read_file('README.md'), # 读取的Readme文档内容
    long_description_content_type="text/markdown",  # 指定包文档格式为markdown
    author="Resolvewang", # 作者相关信息
    author_email='resolvewang@foxmail.com',
    url='https://github.com/SpiderClub/haipproxy',
    # 指定包信息，还可以用find_packages()函数
    packages=[
        'haipproxy',
        'haipproxy.client',
        'haipproxy.utils'
    ],
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    include_package_data=True,
    license="MIT",
    keywords=['proxy', 'client', 'haipproxy'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
```