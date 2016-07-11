from os.path import isfile, isdir
from os import makedirs
from hashlib import md5
from requests import get
from gzip import open as unzip


def download():
    dburl = "http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"
    response = get(dburl)
    with open("./db/GeoLite2-City.mmdb.gz", 'wb') as handle:
        for data in response.iter_content(1024):
            handle.write(data)
    with unzip("./db/GeoLite2-City.mmdb.gz", 'rb') as infile:
        with open("./db/GeoLite2-City.mmdb", 'wb') as outfile:
            outfile.write(infile.read())

def update():
    if (isfile("./db/GeoLite2-City.mmdb") is True):
        # Get current's database hash
        BLOCKSIZE = 13107200
        hasher = md5()
        with open("./db/GeoLite2-City.mmdb", 'rb') as database:
            buf = database.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = database.read(BLOCKSIZE)
        # Get hash from the web
        dbhashurl = get("http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.md5")
        dbhash = str(dbhashurl.text)
        if (dbhash != hasher.hexdigest()):
            download()
            message = print("Database updated successfully!")
            return message
        elif (dbhash == hasher.hexdigest()):
            message = print("Database is already up-to-date.")
            return message
        else:
            message = print("Unknown error while identifying hashes")
            return message
    else:
        if (isdir("./db") is True):
            print("Database was not found, please wait while it is being\ndownloaded...")
            download()
        else:
            print("Path './db' was not found, please wait while it is being\ncreated and the database is being downloaded...")
            makedirs("db")
            download()
