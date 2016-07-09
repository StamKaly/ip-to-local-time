from requests import get

def localip():
    ipurl = get('http://ip.42.pl/raw')
    ip = str(ipurl.text)
    return ip
