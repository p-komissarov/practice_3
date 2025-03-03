from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=7))
ct = datetime.now(tz)
print(ct)