from requests import get

def localip():
    '''
    Returns local IP
    '''
    # Get and return data from the site 
    ipurl = get('http://ip.42.pl/raw')
    ip = str(ipurl.text)
    return ip
