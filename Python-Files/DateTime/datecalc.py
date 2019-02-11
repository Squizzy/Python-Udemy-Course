import time

print(time.gmtime(0))  # output are named tuples - in utc

# print(time.localtime())  # output are tuples

# print(time.time())  # number of second since start of epoch (1/1/1970)

time_here = time.localtime()
print(time_here)
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)
