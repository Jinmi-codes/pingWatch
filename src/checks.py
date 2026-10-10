import requests
import socket
from urllib.parse import urlparse
from enums import Status


class Target:
    def __init__(self, name, status, http_code, time, ):
        self.name = name
        self.status = status
        self.http_code = http_code
        self.time = time
        

def check_dns(url):
    raw_host = urlparse(url).hostname
    try:
        socket.getaddrinfo(raw_host)
        status = True
    except:
        status = False  
    
    return status

def status_check(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        # 404/500 requests
        status = Target(url, Status.DEAD,r.status_code, r.elapsed )
        return status
    except requests.exceptions.Timeout:
        # timed out requests
        status = Target(url, Status.TIMEOUT,r.status_code, r.elapsed )
        return status
    except requests.exceptions.RequestException:
        status = Target(url, Status.BAD,r.status_code, r.elapsed )
        return status
    status = Target(url, Status.SUCCESS,r.status_code, r.elapsed )
    return status
            
        
