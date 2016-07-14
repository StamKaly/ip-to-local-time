from . import localip, db
import geoip2.database as d



def timezone(ip):
    '''
    Returns the time zone of the given IP
    '''
    try:
        # Check if the database exists, look up the local IP in the database and return it
        reader = d.Reader('./db/GeoLite2-City.mmdb')
        response = reader.city(str(ip))
        tz = str(response.location.time_zone)
        return tz
    except FileNotFoundError:
        # If it doesn't download it and exit
        db.update()
    


def local():
    '''
    Returns local time zone
    '''
    try:
        # Check if the database exists, look up the local IP in the database and return it
        reader = d.Reader('./db/GeoLite2-City.mmdb')
        response = reader.city(localip.localip())
        tz = str(response.location.time_zone)
        return tz
    except FileNotFoundError:
        # If it doesn't download it and exit
        db.update()
