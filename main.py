from time import sleep
from njfu_wifi import login, ping, connect2wifi
import logging
import argparse

def parse_arg():
    despription = "自动检测网络状况，并且连接校园网"
    parse = argparse.ArgumentParser(description=despription)
    parse.add_argument("--host", help="ping的主机，用于检测网络是否连通", default="www.baidu.com")
    parse.add_argument("--wifi", help="wifi名称", required=True)
    parse.add_argument("--url", help="登录地址", required=True)
    parse.add_argument("--username", help="用户名 | NJFU-WiFi: w<学号> | CMCC-EDU: w<学号>@cmcc", required=True)
    parse.add_argument("--password", help="密码 | 通常是身份证后六位", required=True)
    return parse.parse_args()


if __name__ == "__main__":
    
    args = parse_arg()
    
    failure = 3
    succ = 0
    logging.basicConfig(format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO)
    while True:
        try:
            result = ping(args.host)
        except:
            result = None
        if result:
            failure = 0
            succ = min(10, succ + 1)
            logging.info("pong!")
        else:
            succ = 0
            failure = failure + 1
            logging.warning("Fail Connenct to Internet")
            if failure >= 4:
                logging.info("Login Cmcc")
                try:
                    connect2wifi(args.wifi)
                    sleep(8)
                    login(args.username, args.password, args.url)
                    logging.info("Login Sucess!")
                except:
                    logging.error("Login Fail!")
        sleep(3 * max(1, succ))