from get import db
from get import dbhash
from get import localip
from get import localt
from get import timezone



db.db()
print(localip.localip())
print(timezone.local())
print(timezone.timezone("37.6.241.211"))
print(localt.localt("37.6.241.211"))

# Put any IP in functions localt (= local time) and timezone to get the results ^^
