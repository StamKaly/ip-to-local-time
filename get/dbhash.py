from os.path import isfile
from hashlib import md5
from requests import get
import db




def dbhash():
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
            db.db()
            print("Database updated successfully!")
        elif (dbhash == hasher.hexdigest()):
            print("Database is already up-to-date.")
        else:
            print("Uknown error while identifying hashes")
    else:
        print("Database was not found")
