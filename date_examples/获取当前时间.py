from datetime import date, datetime
from time import localtime, strftime

today_date = date.today()
print(today_date)

today_time = datetime.today()
print(today_time)

local_time = localtime()
print(strftime("%Y-%m-%d %H:%M:%S", local_time))
