from datetime import datetime, timedelta

ts = 1655294400
datetime_dt = datetime.fromtimestamp(ts) + timedelta(hours=3)
print(datetime_dt.time())