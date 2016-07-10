from . import timezone, localip, db
import pytz
from datetime import datetime
from time import localtime
import geoip2.database as d
import sys


def ip2lt(ip):
    try:
        reader = d.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        db.update()
        sys.exit(0)
    try:
        try:
            my_ip = localip.localip()
            myip = reader.city(my_ip)
            local_tz = pytz.timezone(str(myip.location.time_zone))
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect your local time zone, try using\n'localt.ip2lt2(your time zone, ip)' instead")
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
    except ValueError:
        print("Please insert a valid IP Address")
        sys.exit(0)
    return resp_dt.strftime(fmt)


def ip2lt2(your_time_zone, ip):
    try:
        reader = d.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        db.update()
        sys.exit(0)
    try:
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
    except ValueError:
        print("Please insert a valid IP Address")
        sys.exit(0)
    return resp_dt.strftime(fmt)


def tz2lt2(your_time_zone, time_zone):
    try:
        reader = d.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        db.update()
        sys.exit(0)
    try:
        try:
            local_tz = pytz.timezone(str(your_time_zone))
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect your local time zone in the database, please try again!")
            sys.exit(0)
        try:
            resp_tz = pytz.timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect given time zone in the database, please try again!")
            sys.exit(0)
        local_time = localtime()
        local_dt = local_tz.localize(
            datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                     local_time.tm_sec, 0))
        resp_dt = local_dt.astimezone(resp_tz)
        fmt = '%H:%M'
    except ValueError:
        print("Please insert a valid IP Address")
        sys.exit(0)
    return resp_dt.strftime(fmt)




def tz2lt(time_zone):
    try:
        reader = d.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        db.update()
        sys.exit(0)
    try:
        try:
            my_ip = localip.localip()
            myip = reader.city(my_ip)
            local_tz = pytz.timezone(str(myip.location.time_zone))
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect your local time zone, try using\n'localt.tz2lt2(your time zone, time zone)' instead")
            sys.exit(0)
        try:
            resp_tz = pytz.timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect given time zone in the database, please try again!")
            sys.exit(0)
        local_time = localtime()
        local_dt = local_tz.localize(
            datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                     local_time.tm_sec, 0))
        resp_dt = local_dt.astimezone(resp_tz)
        fmt = '%H:%M'
    except ValueError:
        print("Please insert a valid IP Address")
        sys.exit(0)
    return resp_dt.strftime(fmt)
