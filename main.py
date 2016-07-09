import get.db as db
import get.dbhash as dbhash
import get.localip as localip
import get.localt as localt
import get.timezone as timezone



print(localip.localip())
print(timezone.local())
print(timezone.timezone("37.6.241.211"))
# localt (= local time) doesnt work yet
