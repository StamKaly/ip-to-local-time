from . import timezone, csvreader
from datetime import datetime
import pytz
import time


def ip2lt(ip):
    '''
    Returns the local time of the IP given
    '''
    # Check if the IP is valid
    try:
        # Check if the IP is in the main database
        try:
            target_tz = pytz.timezone(timezone.timezone(ip))
        except pytz.exceptions.UnknownTimeZoneError:
            # If it isn't check the secondary database
            if csvreader.ip(ip) is not None:
                target_tz = pytz.timezone(csvreader.ip(ip))
            else:
                # If it's not in the secondary database exit
                return "Unable to detect given IP's time zone neither in the time zone database nor\nin the IP database, add the IP into the database!"
        # Get GMT time, convert it to the specific time zone and return the time
        utcdate = time.gmtime()
        target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, utcdate.tm_hour, utcdate.tm_min, 0, tzinfo=pytz.utc)
        conversion = target_tz.normalize(target_dt.astimezone(target_tz))
        timestr = str(conversion)
        dt, t = timestr.split(' ')
        tim = t[:5]
        return tim
    # If it isn't exit
    except ValueError:
        return "Please enter a valid IP address!"
    # All the definitions below follow the same logic
    




def gmt2lt(ip, hours, minutes):
    '''
    Converts and returns IP's local time to given GMT time
    '''
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        return "Please input actual time!"
    if (hours <= 23 and
        minutes <= 59):
        try:
            try:
                target_tz = pytz.timezone(timezone.timezone(ip))
            except pytz.exceptions.UnknownTimeZoneError:
                if csvreader.ip(ip) is not None:
                    target_tz = pytz.timezone(csvreader.ip(ip))
                else:
                    return "Unable to detect given IP's time zone neither in the time zone database nor\nin the IP database, add the IP into the database!"
            utcdate = time.gmtime()
            target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
            conversion = target_tz.normalize(target_dt.astimezone(target_tz))
            timestr = str(conversion)
            dt, t = timestr.split(' ')
            tim = t[:5]
            return tim
        except ValueError:
            return "Please enter a valid IP address!"
    else:
        return "Please input actual time!"



def gmt2mt(hours, minutes):
    '''
    Converts and returns your local time  to given GMT time
    '''
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        return "Please input actual time!"
    if (hours <= 23 and
        minutes <= 59):
        try:
            target_tz = pytz.timezone(timezone.local())
        except pytz.exceptions.UnknownTimeZoneError:
            if csvreader.ip(ip) is not None:
                target_tz = pytz.timezone(csvreader.ip(ip))
            else:
                return "Unable to detect your time zone neither in the time zone database nor\nin the IP database, add the IP into the database!"
        utcdate = time.gmtime()
        target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
        conversion = target_tz.normalize(target_dt.astimezone(target_tz))
        timestr = str(conversion)
        dt, t = timestr.split(' ')
        tim = t[:5]
        return tim
    else:
        return "Please input actual time!"




def ip2lt2(time_zone):
    '''
    Returns local time of the given time zone
    '''
    try:
        target_tz = pytz.timezone(time_zone)
    except pytz.exceptions.UnknownTimeZoneError:
        return "Unable to detect given time zone, please try again!"
    utcdate = time.gmtime()
    target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, utcdate.tm_hour, utcdate.tm_min, 0, tzinfo=pytz.utc)
    conversion = target_tz.normalize(target_dt.astimezone(target_tz))
    timestr = str(conversion)
    dt, t = timestr.split(' ')
    tim = t[:5]
    return tim




def gmt2lt2(time_zone, hours, minutes):
    '''
    Converts and returns time zone's local time to given GMT time
    '''
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        return "Please input actual time!"
    if (hours <= 24 and
        minutes <= 59):
        try:
            target_tz = pytz.timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            return "Unable to detect given time zone, please try again!"
        utcdate = time.gmtime()
        target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
        conversion = target_tz.normalize(target_dt.astimezone(target_tz))
        timestr = str(conversion)
        dt, t = timestr.split(' ')
        tim = t[:5]
        return tim
    else:
        return "Please input actual time!"
