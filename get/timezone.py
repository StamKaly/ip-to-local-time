from . import localip
import geoip2.database as d



def timezone(ip):
    reader = d.Reader('./db/GeoLite2-City.mmdb')
    response = reader.city(str(ip))
    tz = str(response.location.time_zone)
    return tz



def local():
    reader = d.Reader('./db/GeoLite2-City.mmdb')
    response = reader.city(localip.localip())
    tz = str(response.location.time_zone)
    return tz
