from os.path import isfile, isdir
from os import makedirs
from hashlib import md5
from requests import get
from gzip import open as unzip


def download():
    '''
    Downloads the database
    '''
    # Get the data in the database file from the site and save it in memory
    dburl = "http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"
    response = get(dburl)
    # Write data saved in memory to a local file
    with open("./db/GeoLite2-City.mmdb.gz", 'wb') as handle:
        for data in response.iter_content(1024):
            handle.write(data)
    # Extract the compressed database file
    with unzip("./db/GeoLite2-City.mmdb.gz", 'rb') as infile:
        with open("./db/GeoLite2-City.mmdb", 'wb') as outfile:
            outfile.write(infile.read())

def update():
    '''
    Update the database
    '''
    # Check if the database exists
    if (isfile("./db/GeoLite2-City.mmdb") is True):
        # Get current's database hash and save it to memory
        BLOCKSIZE = 13107200
        hasher = md5()
        with open("./db/GeoLite2-City.mmdb", 'rb') as database:
            buf = database.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = database.read(BLOCKSIZE)
        # Get hash from the web and save it to memory
        dbhashurl = get("http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.md5")
        dbhash = str(dbhashurl.text)
        # If the two hashes differ, download the database
        if (dbhash != hasher.hexdigest()):
            download()
            message = print("Database updated successfully!")
            return message
        # If the two hashes are the same exit without downloading
        elif (dbhash == hasher.hexdigest()):
            message = print("Database is already up-to-date.")
            return message
    # If it doesn't download it
    else:
        # Check if the database directory exists
        if (isdir("./db") is True):
            # If it does just run the download
            print("Database was not found, please wait while it is being\ndownloaded...")
            download()
        else:
            # If it doesn't create the database path and then run download
            print("Path './db' was not found, please wait while it is being\ncreated and the database is being downloaded...")
            makedirs("db")
            download()
