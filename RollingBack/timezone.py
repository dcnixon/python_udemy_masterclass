import pytz
import datetime

help(datetime.datetime)
help(pytz)

print(pytz.utc.localize(datetime.datetime.utcnow()))
print(datetime.datetime.now().astimezone())
# print(datetime.datetime.now().tzname())
# print(local_time.astimezone())