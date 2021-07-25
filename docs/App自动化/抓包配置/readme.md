## Charles

    windows
        安装证书
            help-->SSLProxying-->Install Charles root Certificate-->本地-->受信任的
        设置所有SSL代理
            Proxy-->SSL Proxying Settings-->勾选Enable SSL Proxying-->Add-->Host:*,Port:443-->ok
        关闭公用网络防火墙

    android(6.0以下)
        连接
        wifi-->长按-->修改网络-->高级选项-->代理：手动-->主机名：主机ip,端口：charles端口，在Proxying Settings
        证书

            1.访问chls.pro/ssl安装
            2.证书下载后手机设置--> 安全--> 安装证书

    iphone
        设置ip和端口
        访问chls.pro/ssl安装
        设置 --> 通用 --> 关于本机 --> 信任证书设置 -->设置相应证书


## Mitmproxy
    windows
        pip install mitmproxy

        windows不支持mitmproxy
        可以用mitmweb代替

        安装证书
            cmd >mitmdump
            C:\Users\Administrator\.mitmproxy -->双击mitmproxy-ca.p12安装

        android
            连接
            主机名：局域网ip 
            端口：mitmproxy端口

            证书安装
                1.访问 mitm.it安装
                2.证书下载后手机 设置--> 安全--> 安装证书

        iphone
            设置 ip 和 端口
            访问 chls.pro/ssl 安装
            设置 --> 通用 --> 关于本机 --> 信任证书设置 -->设置相应证书