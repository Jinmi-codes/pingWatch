import requests
import socket
from urllib.parse import urlparse
from enums import Status


def check_dns(url):
    raw_host = urlparse(url).hostname
    try:
        socket.getaddrinfo(raw_host)
        status = True
    except:
        status = False  
    
    return status

def status_check(url):
    status = ""
    r = requests.get(url)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        # 404/500 requests
        status = Status.DEAD
        return status
    except requests.exceptions.Timeout:
        # timed out requests
        status = Status.TIMEOUT
        return status
    except requests.exceptions.RequestException:
        status = Status.BAD
        return status
    status = Status.SUCCESS
    return status
        