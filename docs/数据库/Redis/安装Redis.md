### 安装`gcc`依赖

由于 `redis` 是用 C 语言开发，安装之前必先确认是否安装 `gcc` 环境（`gcc -v`），
如果没有安装，执行以下命令进行安装

```shell
yum install -y gcc 
```

### 下载并解压安装包
这里以 `/usr/local/redis-5.0.3` 目录为例
```shell
wget http://download.redis.io/releases/redis-5.0.3.tar.gz
tar -zxvf redis-5.0.3.tar.gz
```

###  解压目录、编译、安装

编译安装到 `/usr/local/redis`
```shell
cd redis-5.0.3
make
make install PREFIX=/usr/local/redis
```

 

### 启动服务
```shell
cd /usr/local/redis/bin/
./redis-server
```

### 后台启动

从 `redis` 的源码目录中复制 `redis.conf` 到 `redis` 的安装目录
```shell
cp /usr/local/redis-5.0.3/redis.conf /usr/local/redis/bin/
```

```shell
vi redis.conf
```
修改 `redis.conf` 文件，把 `daemonize no` 改为 `daemonize yes` (后台驻留)

搜索 `requirepass` 并修改密码项 `requirepass 你的密码`


### 配置文件启动
```shell
./redis-server ./redis.conf
```

现在就可以`后台启动`并开启`远程连接`了，连接密码就是配置文件中设置的 `requirepass`

> 需要注意的是 `config set requirepass test123` 在`配置文件`启动时并`不会生效`，二者并无关联。

 