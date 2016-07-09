from requests import get
from gzip import open as unzip






def db():
    dburl = "http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"
    response = get(dburl)
    with open("./db/GeoLite2-City.mmdb.gz", 'wb') as handle:
        for data in response.iter_content(1024):
            handle.write(data)
    with unzip("./db/GeoLite2-City.mmdb.gz", 'rb') as infile:
        with open("./db/GeoLite2-City.mmdb", 'wb') as outfile:
            outfile.write(infile.read())
