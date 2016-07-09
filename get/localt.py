from . import timezone, localip
import pytz
from datetime import datetime
from time import localtime


def localt(ip):
    tz = timezone.timezone(ip)
    resp_tz = pytz.timezone(tz)
    my_ip = localip.localip()
    local_tz = pytz.timezone(my_ip)
    local_time = localtime()
    local_dt = local_tz.localize(
        datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                 local_time.tm_sec, 0))
    resp_dt = local_dt.astimezone(resp_tz)
    fmt = '%H:%M'
    return resp_dt.strftime(fmt)




# Testing, also close the imports of local when testing
'''
ip = "46.101.20.237"
my_ip = "37.6.241.211"
tz = "Europe/London"
#tz = timezone.timezone(ip)
resp_tz = pytz.timezone(tz)
#my_ip = localip.localip()
local_tz = pytz.timezone(my_ip)
local_time = localtime()
local_dt = local_tz.localize(
    datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
             local_time.tm_sec, 0))
resp_dt = local_dt.astimezone(resp_tz)
fmt = '%H:%M'
print(resp_dt.strftime(fmt))
'''
