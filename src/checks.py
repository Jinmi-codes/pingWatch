import requests
import socket
from urllib.parse import urlparse
from enums import Status


class Target:
    def __init__(self, name, url, status=None, http_code=0, time=0  ):
        self.name = name
        self.status = status
        self.http_code = http_code
        self.time = time
        self.url = url
   
    
    def status_check(self):
        
        try:
            r = requests.get(self.url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            self.status = Status.DEAD
            self.http_code = r.status_code
            self.time = r.elapsed
            return
        except requests.exceptions.Timeout:
            self.status = Status.TIMEOUT
            self.http_code = r.status_code
            self.time = r.elapsed
        except requests.exceptions.RequestException:
            self.status = Status.BAD
            self.http_code = r.status_code
            self.time = r.elapsed
            
        self.status = Status.SUCCESS
        self.http_code = r.status_code
        self.time = r.elapsed
        

    
        

def check_dns(url):
    raw_host = urlparse(url).hostname
    try:
        socket.getaddrinfo(raw_host)
        status = True
    except:
        status = False  
    
    return status

