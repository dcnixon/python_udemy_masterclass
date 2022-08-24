import sqlite3
import pytz
import pickle

# strptime method from is an SQLite function can be used to convert

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)   # does not handle timezone aware dates
# Standard library does not easily parse timezone aware dates

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                       "history.account, history.amount FROM history ORDER BY history.time"):

for row in db.execute("SELECT * FROM history"):
    print(row)

    # utc_time = row[0]
    # pickled_zone = row[3]
    # zone = pickle.loads(pickled_zone)
    # local_time = pytz.utc.localize(utc_time).astimezone(zone)
    # local_time = pytz.utc.localize(utc_time).astimezone()
    # print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()
