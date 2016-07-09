from . import timezone, localip
import pytz
from datetime import datetime
from time import localtime
import geoip2.database


def localt(ip):
    reader = geoip2.database.Reader('./db/GeoLite2-City.mmdb')
    tz = timezone.timezone(ip)
    resp_tz = pytz.timezone(tz)
    my_ip = localip.localip()
    myip = reader.city(my_ip)
    local_tz = pytz.timezone(str(myip.location.time_zone))
    local_time = localtime()
    local_dt = local_tz.localize(
        datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                 local_time.tm_sec, 0))
    resp_dt = local_dt.astimezone(resp_tz)
    fmt = '%H:%M'
    return resp_dt.strftime(fmt)
