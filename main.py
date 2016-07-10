from get import db
from get import dbhash
from get import localip
from get import localt
from get import timezone



db.download()
print(localip.localip())
print(timezone.local())
print(timezone.timezone("37.6.241.211"))
print(localt.ip2tz("37.6.241.211"))


