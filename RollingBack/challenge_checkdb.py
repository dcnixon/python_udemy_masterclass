import sqlite3
# import pytz

# strptime method from is an SQLite function can be used to convert

db = sqlite3.connect("accountsChal.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)   # does not handle timezone aware dates
# Standard library does not easily parse timezone aware dates

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                       "history.account, history.amount FROM history ORDER BY history.time"):

for row in db.execute("SELECT * FROM history"):
    print(row[0], row[1], row[2:])

    # utc_time = row[0]
    # local_time = pytz.utc.localize(utc_time).astimezone()
    # print("{}\t{}".format(utc_time, local_time))

db.close()
