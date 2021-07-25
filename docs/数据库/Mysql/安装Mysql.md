## 安装 MySQL

笔者认为`Windows` 并不适合安装 `MySQL5.7`  :smile: 

推荐 `MySQL8.0`
安装过程选择界面化安装即可，你甚至不必动用 `cmd` 命令来启动 `MySQL`，只需要把 `MYSQL` 加到 `Windows` 服务并设置开机即可，这里不在详述


### `Linux` 安装 `MySQL5.7` 
> 你知道，我总是愿意用 `Centos` 来代表 `Linux` 系统，我认为它是最好的 `Linux` 服务器 ！！



[MySQL 5.7 下载](https://cdn.mysql.com/Downloads/MySQL-5.7/mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar)


进入下载目录解压文件
```shell
tar -xvf mysql-5.7.29-1.el7.x86_64.rpm-bundle.tar
```

查看原有 `MySQL` 版本，避免 `MySQL` 残留，如果是第一次安装直接忽略即可。
```shell
rpm -qa|grep mariadb
```
删除`MySQL` 残留，不存在则不用管它。
```shell
rpm -e --nodeps mariadb-libs-5.5.60-1.el7_5.x86_64
```

赋予该目录可执行权限，建议 `644` 即可，别一上来就 `777`，这很危险。
```shell
chmod -R 644 mysql
```



`rpm` 安装 `MySQL` 依赖包

```shell
rpm -ivh mysql-community-common-5.7.29-1.el7.x86_64.rpm 
rpm -ivh mysql-community-libs-5.7.29-1.el7.x86_64.rpm 
rpm -ivh mysql-community-client-5.7.29-1.el7.x86_64.rpm 
rpm -ivh mysql-community-server-5.7.29-1.el7.x86_64.rpm 
```

如果安装过程中报了 `GPG keys` 的错误

请在命令后面加上 `--force --nodeps` 参数，重新安装即可。


### `MySQL` 配置文件
 
进入`/etc/my.cnf`并加上如下语句

```shell
skip-grant-tables
character_set_server=utf8
init_connect='SET NAMES utf8'
```

`注意第一行配置了免密登陆，配置成功后记得注释掉再重启 MySQL，否则将后悔莫及`

`注意第一行配置了免密登陆，配置成功后记得注释掉再重启 MySQL，否则将后悔莫及`

`注意第一行配置了免密登陆，配置成功后记得注释掉再重启 MySQL，否则将后悔莫及`



启动`MySQL`服务

```shell
$ systemctl start mysqld.service
```

此时黑窗口键入 `mysql` 可成功进入 `mysql` 客户端

设置宿主机密码，注意是本地密码而非远程连接密码
```shell
update mysql.user set authentication_string=password('123456') where user='root';
flush privileges;
```

推出 `mysql` 客户端并 `stop` 服务

```shell
$ systemctl stop mysqld.service
```

回到 `/etc/my.cnf` 配置文注释掉免密登陆的那一行，并重新启动 `mysql` 服务

```shell
$ systemctl start mysqld.service
```

发现再次进入客户端需要指定用户名密码登陆，也就是我们上面设置的用户密码了。

当然了，`123456` 这个密码连你看起来都有些不太好，`mysql` 在密码设置方面做了一些限制，一些不符合预期的密码不会被通过 ！！

如果你执意使用简单(弱密码)的话，请做下全局设置:

```shell
set global validate_password_policy=LOW;
set global validate_password_length=4;
flush privileges;
```

### 暴露 `3306` 端口

```shell
firewall-cmd --zone=public --add-port=3306/tcp --permanent
firewall-cmd --reload
```

如果你使用的是一些云服务商的服务器(比如阿里云、腾讯云)，请登陆控制台设置开放 `3306` 端口即可

### 允许远程登陆
我们并不会每次都登陆云服务器去进行数据库操作，这就需要允许其他机器远程登陆宿主机。

```shell
grant all privileges on *.* to 'root'@'%' identified by '654321' with grant option;
flush privileges;
```

> 注意这里的密码有别于前面设置的宿主机本地登陆的密码。

> 至此，`MySQL` 部署完毕 ！！
