import pytz
import datetime
from pytz import timezone
from datetime import datetime

# Two times to test, one in DST, one not
dst_time = datetime(2016,2,4, 3,0,0, tzinfo=pytz.utc)
nondst_time = datetime(2016,8,4, 3,0,0, tzinfo=pytz.utc)

# The timezone we want to convert to, which sometimes uses DST
target = timezone('US/Eastern')

# Convert the times to the timezone, adjusing for dst
dst_converted = target.normalize(dst_time.astimezone(target));
nondst_converted = target.normalize(nondst_time.astimezone(target));

fmt = '%H%M'

print(dst_converted(fmt))
print(nondst_converted(fmt))
