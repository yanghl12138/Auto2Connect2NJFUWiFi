from time import sleep
import njfu_wifi
import logging
import click


@click.command()
@click.option("--host", type=str, default="www.baidu.com", help="ping的主机，用于检测网络是否连通，default=www.baidu.com")
@click.option("--wifi", type=str, help="wifi名称", required=True)
@click.option("--url", type=str, help="登录地址", required=True)
@click.option("--username", type=str, help="用户名 | NJFU-WiFi: w<学号> | CMCC-EDU: w<学号>@cmcc", required=True)
@click.option("--password", type=str, help="密码 | 通常是身份证后六位", required=True)
@click.option("--tolorant_failure", type=click.IntRange(1, 10), default=4 ,help="连续失败的次数，default=4")
@click.option("--native-ping", is_flag=True)
def moniterwifi(host:str, wifi:str, url:str, 
                username:str, password:str, 
                tolorant_failure:int, native_ping:bool):
    if native_ping:
        ping = njfu_wifi.ping
    else:
        import ping3
        ping = ping3.ping
        
    failure = tolorant_failure - 1
    succ = 0
    logging.basicConfig(format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO)
    while True:
        try:
            result = ping(host)
        except:
            result = False
        if result:
            failure = 0
            succ = succ + 1
            logging.info("pong!")
        else:
            succ = 0
            failure = failure + 1
            logging.warning("Fail Connenct to Internet")
            if failure >= tolorant_failure:
                logging.info(f"Login {wifi}")
                try:
                    njfu_wifi.connect2wifi(wifi)
                    sleep(8)
                    njfu_wifi.login(username, password, url)
                    logging.info("Login Sucess!")
                    failure = 0
                except:
                    logging.error("Login Fail!")
        sleep(min(max(1, succ), 10)) # 1 <= succ <= 10
    

    
    