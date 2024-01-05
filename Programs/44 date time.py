from datetime import *
import pytz
# print(datetime.now())
# x = datetime(2023,12,31,23,59,59)
# print(x)
# a = datetime.now()
# # a = datetime(2024,1,2)
# print(a.strftime("%S"))

# newtz = pytz.timezone("Asia/Calcutta")
# x = datetime.now(newtz)
# print(datetime.now(pytz.utc))
# print(x)

for key, val in pytz.country_timezones.items():
    print(key,"=",val)














