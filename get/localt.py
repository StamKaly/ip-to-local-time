from . import timezone, csvreader
from datetime import datetime
import pytz
import time
import sys


def ip2lt(ip):
    '''
    Return the local time of the IP given
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
                print("Unable to detect given IP's time zone neither in the time zone database nor\nin the IP database, add the IP into the database!")
                sys.exit(0)
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
        print("Please enter a valid IP address!")
        sys.exit(0)
    # All the definitions below follow the same logic
    




def gmt2lt(ip, hours, minutes):
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        print("Please input actual time!")
        sys.exit(0)
    if (hours <= 24 and
        minutes <= 59):
        try:
            try:
                target_tz = pytz.timezone(timezone.timezone(ip))
            except pytz.exceptions.UnknownTimeZoneError:
                if csvreader.ip(ip) is not None:
                    target_tz = pytz.timezone(csvreader.ip(ip))
                else:
                    print("Unable to detect given IP's time zone neither in the time zone database nor\nin the IP database, add the IP into the database!")
                    sys.exit(0)
            utcdate = time.gmtime()
            target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
            conversion = target_tz.normalize(target_dt.astimezone(target_tz))
            timestr = str(conversion)
            dt, t = timestr.split(' ')
            tim = t[:5]
            return tim
        except ValueError:
            print("Please enter a valid IP address!")
            sys.exit(0)
    else:
        print("Please input actual time!")
        sys.exit(0)



def gmt2mt(hours, minutes):
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        print("Please input actual time!")
        sys.exit(0)
    if (hours <= 24 and
        minutes <= 59):
        try:
            try:
                target_tz = pytz.timezone(timezone.local())
            except pytz.exceptions.UnknownTimeZoneError:
                if csvreader.ip(ip) is not None:
                    target_tz = pytz.timezone(csvreader.ip(ip))
                else:
                    print("Unable to detect your time zone neither in the time zone database nor\nin the IP database, add the IP into the database!")
                    sys.exit(0)
            utcdate = time.gmtime()
            target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
            conversion = target_tz.normalize(target_dt.astimezone(target_tz))
            timestr = str(conversion)
            dt, t = timestr.split(' ')
            tim = t[:5]
            return tim
        except ValueError:
            print("Please enter a valid IP address!")
            sys.exit(0)
    else:
        print("Please input actual time!")
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




def gmt2lt2(time_zone, hours, minutes):
    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        print("Please input actual time!")
        sys.exit(0)
    if (hours <= 24 and
        minutes <= 59):
        try:
            try:
                target_tz = pytz.timezone(time_zone)
            except pytz.exceptions.UnknownTimeZoneError:
                print("Unable to detect given time zone, please try again!")
                sys.exit(0)
            utcdate = time.gmtime()
            target_dt = datetime(utcdate.tm_year, utcdate.tm_mon, utcdate.tm_mday, hours, minutes, 0, tzinfo=pytz.utc)
            conversion = target_tz.normalize(target_dt.astimezone(target_tz))
            timestr = str(conversion)
            dt, t = timestr.split(' ')
            tim = t[:5]
            return tim
        except ValueError:
            print("Please enter a valid IP address!")
            sys.exit(0)
    else:
        print("Please input actual time!")
        sys.exit(0)
