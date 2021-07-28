## Charles

### windows
#### 安装证书
### `help` > `SSLProxying` > `Install Charles root Certificate` > `本地` > `受信任的`

---

#### 设置所有SSL代理
`Proxy` > `SSL Proxying Settings` > 勾选 `Enable SSL Proxying` > `Add`  > `Host:*,Port:443`  > `ok`

---
#### android(7.0以下)

### `wifi` > `长按` > `修改网络` > `高级选项` > `代理` > `手动` > `主机ip,charles端口`
    
---
#### 证书
- 访问 `chls.pro/ssl` 安装
- 证书下载后手机`设置` > `安全` > `安装证书`
---

#### iphone

- 访问 `chls.pro/ssl` 安装
- `设置` > `通用` > `关于本机` > `信任证书设置` > `设置相应证书`

---
## Mitmproxy
### windows
`pip install mitmproxy`

#### `windows` 不支持 `mitmproxy`
可以用 `mitmweb` 代替

---

#### 安装证书
```shell
cmd >mitmdump
C:\Users\Administrator\.mitmproxy > 双击 mitmproxy-ca.p12 安装
```

---

### android

### `wifi` > `长按` > `修改网络` > `高级选项` > `代理` > `手动` > `主机ip,mitmdump 端口`

---

#### 证书安装
- 访问 `mitm.it` 安装
- 证书下载后手机 `设置` > `安全` > `安装证书`

