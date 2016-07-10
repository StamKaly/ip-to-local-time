from . import localip, db
import geoip2.database as d



def timezone(ip):
    try:
        reader = geoip2.database.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        db.update()
        sys.exit(0)
    response = reader.city(str(ip))
    tz = str(response.location.time_zone)
    return tz



def local():
    try:
        reader = geoip2.database.Reader('./db/GeoLite2-City.mmdb')
    except FileNotFoundError:
        db.update()
        sys.exit(0)
    response = reader.city(localip.localip())
    tz = str(response.location.time_zone)
    return tz
