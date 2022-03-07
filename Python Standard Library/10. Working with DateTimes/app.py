from datetime import datetime
import time

dt = datetime(2018, 1, 1)

print(datetime.now())
print(datetime.strptime("2018/01/01", "%Y/%m/%d"))
print(dt)

print(datetime.fromtimestamp(time.time()))

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))  # opposite of strptime

print(datetime.now() > dt)
