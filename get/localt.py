from . import timezone, localip
import pytz
from datetime import datetime
from time import localtime
import geoip2.database
import sys


def localt(ip):
    reader = geoip2.database.Reader('./db/GeoLite2-City.mmdb')
    try:
        my_ip = localip.localip()
        myip = reader.city(my_ip)
        local_tz = pytz.timezone(str(myip.location.time_zone))
    except pytz.exceptions.UnknownTimeZoneError:
        print("Unable to detect your local time zone, try using\n'localt.localt2(your time zone, ip)' instead")
        sys.exit(0)
    try:
        tz = timezone.timezone(ip)
        resp_tz = pytz.timezone(tz)
    except pytz.exceptions.UnknownTimeZoneError:
        print("Unable to detect given IP's time zone")
        sys.exit(0)
    local_time = localtime()
    local_dt = local_tz.localize(
        datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                 local_time.tm_sec, 0))
    resp_dt = local_dt.astimezone(resp_tz)
    fmt = '%H:%M'
    return resp_dt.strftime(fmt)


def localt2(your_time_zone, ip):
    reader = geoip2.database.Reader('./db/GeoLite2-City.mmdb')
    try:
        local_tz = pytz.timezone(str(your_time_zone))
    except pytz.exceptions.UnknownTimeZoneError:
        print("Unable to detect your local time zone in the database, please try again!")
        sys.exit(0)
    try:
        tz = timezone.timezone(ip)
        resp_tz = pytz.timezone(tz)
    except pytz.exceptions.UnknownTimeZoneError:
        print("Unable to detect given IP's time zone")
        sys.exit(0)
    local_time = localtime()
    local_dt = local_tz.localize(
        datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                 local_time.tm_sec, 0))
    resp_dt = local_dt.astimezone(resp_tz)
    fmt = '%H:%M'
    return resp_dt.strftime(fmt)
