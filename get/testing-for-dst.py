import pytz
import datetime
from datetime import datetime
import time

local_time = time.localtime()

# Two times to test, one in DST, one not
sometime = datetime(local_time.tm_year, local_time.tm_mon, local_time.tm_mday, local_time.tm_hour, local_time.tm_min,
                    local_time.tm_sec, tzinfo=pytz.utc)

# The timezone we want to convert to, which sometimes uses DST
target = pytz.timezone('Europe/London')

# Convert the times to the timezone, adjusing for dst
sometime_converted = target.normalize(sometime.astimezone(target));


print(dst_converted)
print(nondst_converted)
