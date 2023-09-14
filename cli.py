from monitor_wifi import Monitor
import click
import logging
from time import sleep

@click.command()
@click.option("--host", type=str, default="www.baidu.com", help="ping的主机，用于检测网络是否连通，default=www.baidu.com")
@click.option("--wifi", type=str, help="wifi名称", required=True)
@click.option("--url", type=str, help="登录地址", required=True)
@click.option("--username", type=str, help="用户名 | NJFU-WiFi: w<学号> | CMCC-EDU: w<学号>@cmcc", required=True)
@click.option("--password", type=str, help="密码 | 通常是身份证后六位", required=True)
@click.option("--tolorant_failure", type=click.IntRange(1, 10), default=4 ,help="连续失败的次数，default=4")
@click.option("--native-ping", is_flag=True)
def main(host:str, wifi:str, url:str, 
                username:str, password:str, 
                tolorant_failure:int, native_ping:bool):
    logging.basicConfig(format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO)
    monitor = Monitor(wifi=wifi, url=url, 
                      username=username, password=password, 
                      tolorant_failure=tolorant_failure, native_ping=native_ping,
                      host=host)
    pinging = monitor.pinging()
    while True:
        code = next(pinging)
        if code > 0:
            logging.info("pong!")
        elif abs(code) >= monitor.tolorant_failure :
            try:
                monitor.connectiong()
                sleep(5 + 2 * (abs(code) - monitor.tolorant_failure))
                monitor.logining()
                logging.info("Login Sucess!")
            except Exception as e:
                logging.error(e)
        sleep(1 if code < 0 else code)



if __name__ == "__main__":
    main()