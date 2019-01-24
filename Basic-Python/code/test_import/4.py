import time

nowTime = time.time()
print(nowTime) # 1548304818.442229
print(time.localtime(nowTime)) # time.struct_time(tm_year=2019, tm_mon=1, tm_mday=24, tm_hour=12, tm_min=41, tm_sec=51, tm_wday=3, tm_yday=24, tm_isdst=0)
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 2019-01-24 12:43:38
