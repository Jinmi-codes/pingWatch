import requests
import socket
from urllib.parse import urlparse
from enums import Status


class Target:
    def __init__(self, name, url, timeout=None, status=None, http_code=0, time=0  ):
        self.name = name
        self.status = status
        self.http_code = http_code
        self.time = time
        self.url = url
        self.timeout = timeout
        
   
    
    def status_check(self):
        
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            time = "hey"
            self.status = Status.SUCCESS
            self.http_code = r.status_code
            self.time = str(r.elapsed).split(":")[2]
        except requests.exceptions.HTTPError:
            self.status = Status.DEAD
            self.http_code = r.status_code
            self.time = str(r.elapsed).split(":")[2]
        except requests.exceptions.Timeout:
            self.status = Status.TIMEOUT
            self.http_code = 500
            self.time = self.timeout
        except requests.exceptions.RequestException:
            self.status = Status.BAD
            self.http_code = 500
            self.time = 0
            
        
        

    
        

def check_dns(url):
    raw_host = urlparse(url).hostname
    try:
        socket.getaddrinfo(raw_host)
        status = True
    except:
        status = False  
    
    return status

