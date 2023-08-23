# 自动连接NJFU-WiFi

## 缘起

学校图书馆三楼B区的网络较差，人一多，经常断连，遂使用Python3脚本，实现网络状况的检测、自动连接WiFi以及校园网登录。

## 使用说明

1. 编写此程序使用的Python版本为3.11.2
2. 依赖：

   - requests
   - ping3

   ```bash
   pip install requests ping3
   ```

3. Ping和连接wifi的实现是调用了系统工具。Ping通过调用系统的`ping`实现；wifi连接目前只实现了Windows，通过调用`netsh`

4. 使用方法
   ```
    自动检测网络状况，并且连接校园网

    options:
      -h, --help           show this help message and exit
      --host HOST          ping的主机，用于检测网络是否连通，default=www.baidu.com
      --wifi WIFI          wifi名称
      --url URL            登录地址
      --username USERNAME  用户名 | NJFU-WiFi: w<学号> | CMCC-EDU: w<学号>@cmcc
      --password PASSWORD  密码 | 通常是身份证后六位
      --failure FAILURE    连续失败的次数，default=4，>=1
      --native-ping        使用本地的ping，否则使用ping3模块
   ```
5. 例子：cmd脚本，连接NJUF-WiFi
   ```cmd
   "D:\Program Files\Python311\python.exe" ^
   D:\codefile\code_py\njfu_wifi\main.py ^
   --wifi NJFU-WiFi ^
   --url http://121.248.150.37 ^
   --username w<学号> ^
   --password <身份证后六位> ^
   --native-ping
   pause
   ```