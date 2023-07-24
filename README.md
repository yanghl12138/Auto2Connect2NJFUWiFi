# 自动连接NJFU-WiFi

## 缘起

学校图书馆三楼B区的网络较差，人一多，经常断连，遂使用Python3脚本，实现网络状况的检测、自动连接WiFi以及校园网登录。

## 使用说明

1. 编写此程序使用的Python版本为3.11.2
2. 依赖：

   - requests

   ```bash
   pip install requests
   ```

3. Ping和连接wifi的实现是调用了系统工具。Ping通过调用系统的`ping`实现；wifi连接目前只实现了Windows，通过调用`netsh`

4. 使用方法
    ```
    自动检测网络状况，并且连接校园网

    options:
    -h, --help           show this help message and exit
    --host HOST          ping的主机
    --wifi WIFI          wifi名称
    --url URL            登录地址
    --username USERNAME  用户名 | NJFU-WiFi: w<学号> | CMCC-EDU: w<学号>@cmcc
    --password PASSWORD  密码 | 通常是身份证后六位
    ```
