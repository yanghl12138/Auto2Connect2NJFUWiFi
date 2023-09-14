from time import sleep
import njfu_wifi

import click
from dataclasses import dataclass

@dataclass
class Monitor:
    MAXCOUNT = 10
    
    # wifi
    wifi: str 
    url: str 
    
    # 用户
    username: str 
    password: str 
    
    # 运行参数
    tolorant_failure: int = 4
    native_ping:bool = False
    host:str = "www.baidu.com"
    
    def _getping(self):
        if self.native_ping:
            return njfu_wifi.ping
        else:
            import ping3
            return ping3.ping
    
    def logining(self):
        njfu_wifi.login(username=self.username, password=self.password, url=self.url)
        
    def connectiong(self):
        if not njfu_wifi.connect2wifi(self.wifi):
            raise Exception("can not connect to wifi")
    
    '''
     count in [-2 * tolerent_failure, 0) and (0, MAXCOUNT]
    '''
    def pinging(self):
        
        ping = self._getping()
        
        count = 0
        while True:
            
            try:
                result = ping(self.host)
            except:
                result = False
            
            if result:
                count = 1 if count < 0 else min(count + 1, Monitor.MAXCOUNT)
            else:
                count = -1 if count > 0 else max(count - 1, -self.tolorant_failure * 2)
                
            yield count