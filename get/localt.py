from . import timezone, localip
from datetime import datetime
import pytz
import time
import sys


def ip2lt(ip):
    try:
        try:
            target_tz = pytz.timezone(timezone.timezone(ip))
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect given IP's time zone, try using\n'localt.ip2lt2(time zone)' instead")
            sys.exit(0)
        utcdate = time.gmtime()
        target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, utcdate.tm_hour, utcdate.tm_min, 0, tzinfo=pytz.utc)
        conversion = target_tz.normalize(target_dt.astimezone(target_tz))
        timestr = str(conversion)
        dt, t = timestr.split(' ')
        tim = t[:5]
        return tim
    except ValueError:
        print("Please enter a valid IP address!")
        sys.exit(0)
    

def ip2lt2(time_zone):
    try:
        try:
            target_tz = pytz.timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            print("Unable to detect given time zone, please try again!")
            sys.exit(0)
        utcdate = time.gmtime()
        target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, utcdate.tm_hour, utcdate.tm_min, 0, tzinfo=pytz.utc)
        conversion = target_tz.normalize(target_dt.astimezone(target_tz))
        timestr = str(conversion)
        dt, t = timestr.split(' ')
        tim = t[:5]
        return tim
    except ValueError:
        print("Please enter a valid IP address!")
        sys.exit(0)
