from . import localip, db
import geoip2.database as d
import sys



def timezone(ip):
    '''
    Returns the time zone of the given IP
    '''
    try:
        # Check if the database exists
        reader = d.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        # If it doesn't download it and exit
        db.update()
        sys.exit(0)
    # Look up the IP in the database and return it
    response = reader.city(str(ip))
    tz = str(response.location.time_zone)
    return tz



def local():
    '''
    Returns local time zone
    '''
    try:
        # Check if the database exists
        reader = d.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        # If it doesn't download it and exit
        db.update()
        sys.exit(0)
    # Look up the local IP in the database and return it
    response = reader.city(localip.localip())
    tz = str(response.location.time_zone)
    return tz
