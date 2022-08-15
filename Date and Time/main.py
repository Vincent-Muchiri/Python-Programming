from datetime import datetime, timedelta

# ------------------------------------ TODO Converting a string to date and time ---------------------------------------
string = "2022-05-28T10:30:00+02:00"

# TODO Split the string time and remove the characters after +
dt_string = string.split("+")[0]

# TODO Convert the string to datetime object considering date is in dd/mm/yyyy format
date_time = datetime.strptime(dt_string, "%Y-%m-%dT%H:%M:%S")

# TODO Get the time and date separately
time = date_time.time()
date = date_time.date()
# print("Date =", date)
# print("Time = ", time)

# # Considering date is in mm/dd/yyyy format
# dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
# print("dt_object2 =", dt_object2)

# -------------------------------------- TODO Using UNIX (incremental time) timestamp ----------------------------------
# TODO Getting the current date and time
current_datetime = datetime.now()

# TODO Getting the timestamp
current_timestamp = datetime.timestamp(current_datetime)

# print("Date and time is:", dt)
# print("Timestamp is:", ts)


# TODO Using time library to get timestamp
from time import time

other_ts = time()
# print(other_ts)


# TODO Convert timestamp to 24-Hr format date and time for the current timezone
# convert to datetime
current_datetime = datetime.fromtimestamp(current_timestamp, tz=None)
print("The date and time is:", current_datetime)

# ------------------------------------------------------- UTC ----------------------------------------------------------
# TODO Convert timestamp to UTC
print(current_timestamp)
current_utc = datetime.utcfromtimestamp(current_timestamp).time()
print("The current utc time is = ", current_utc)

# TODO Convert datetime object to UTC
import pytz

# Get current time in local timezone
local_dt = datetime.now()
print('Current Local Time: ', local_dt)
# Convert local to UTC timezone
dt_utc = local_dt.astimezone(pytz.UTC)
print('Current time in UTC Time-zone: ', dt_utc)

# ----------------------------------------------------- TIMESTAMPS -----------------------------------------------------
from_date_ts = 1653598800
to_date_ts = 1653685199

# TODO Convert the timestamps to dates
from_date_utc = datetime.utcfromtimestamp(from_date_ts)
to_date_utc = datetime.utcfromtimestamp(to_date_ts)

print(to_date_utc, from_date_utc)

# TODO Get tomorrow's date
tomorrow_date = datetime.today() + timedelta(days=1)

# TODO Create a custom date
from_year = datetime.now().year
from_month = datetime.now().month
from_day = datetime.now().day

to_year = tomorrow_date.year
to_month = tomorrow_date.month
to_day = tomorrow_date.day

from_date = datetime(year=from_year, month=from_month, day=from_day, hour=20, minute=59, second=59)
to_date = datetime(year=to_year, month=to_month, day=to_day, hour=21, minute=0, second=0)
print(from_date, to_date)

# TODO Convert the datetime object to timestamps
from_date_ts = datetime.timestamp(from_date)
to_date_ts = datetime.timestamp(to_date)
print(from_date_ts, to_date_ts)
