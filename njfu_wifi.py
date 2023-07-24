import requests
import platform
import subprocess

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

# 登录
def login(username:str, password:str, url:str) -> str:
    data = {
            "DDDDD":f"{username}",
            "upass": password,
            "R1":"0",
            "R2":"",
            "R3":"0",
            "R6":"0",
            "para":"00",
            "0MKKey":"123456"
    }
    return requests.post(url=url, data=data, headers=headers).text

# Ping, 检测网络连通性
def ping(host:str) -> bool:
    parm = '-n' if platform.system().lower() == 'windows' else '-c'
    return subprocess.run(['ping', host, parm, '1'], stdout=subprocess.PIPE).returncode == 0

# 连接WiFi
def connect2wifi(name:str):
    match platform.system().lower():
        case 'windows':
            subprocess.run(['netsh', 'wlan', 'connect', f'name={name}'])
        case _:
            raise NotImplementedError()
