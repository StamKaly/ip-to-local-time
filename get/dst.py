from . import timezone
import pytz
from datetime import datetime
import time



def dst_timeconvert(ip, hours, minutes):
    target_tz = pytz.timezone(timezone.timezone(ip))
    utcdate = time.gmtime()
    target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
    conversion = target_tz.normalize(target_dt.astimezone(target_tz))
    timestr = str(conversion)
    dt, t = timestr.split(' ')
    tim = t[:5]
    return tim
	
	
	

def dst_convert(ip):
    target_tz = pytz.timezone(timezone.timezone(ip))
    utcdate = time.gmtime()
    target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, utcdate.tm_hour, utcdate.tm_min, 0, tzinfo=pytz.utc)
    conversion = target_tz.normalize(target_dt.astimezone(target_tz))
    timestr = str(conversion)
    dt, t = timestr.split(' ')
    tim = t[:5]
    return tim

