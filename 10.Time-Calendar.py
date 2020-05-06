# Time and Calendar
import time 

time.
#####################################
Index	Attribute	Values
0	  tm_year	    0000, ...., 2018, ..., 9999
1	  tm_mon	    1, 2, ..., 12
2	  tm_mday	    1, 2, ..., 31
3	  tm_hour	    0, 1, ..., 23
4	  tm_min	    0, 1, ..., 59
5	  tm_sec	    0, 1, ..., 61
6	  tm_wday	    0, 1, ..., 6; Monday is 0
7	  tm_yday	    1, 2, ..., 366
8	  tm_isdst      0, 1 or -1
######################################

#No of tricks(seconds) from 12.00 am, 1 st Jan 1970
tricks = time.time()
print('no of tricks :',tricks)

# check the time difference use for pgm execution/response time etc..
t1=time.time()
t2=time.time()
t2-t1

t=time.localtime()
t
type(t)
t[0]
t[6]

time.asctime( time.localtime(time.time()) )
# for the above same we can use time.asctime()
# asctime is to get the time in readable format.
time.asctime()

time.timezone

time.tzname 

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

# Sleep
print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

tricks = time.time()
print(tricks)

result = time.localtime(1586139085)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

result = time.gmtime(1586139085)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)


##################################
%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - month [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 61]
###################################
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)



#*********************CALENDER******************************

import calendar
calendar.
calendar.calendar(1250)
calendar.calendar(2019)

calendar.isleap(2016)
calendar.monthcalendar(2020,4)
calendar.monthcalendar(2020,04)  # Does not accept 04  #
calendar.firstweekday()
t=calendar.weekday(2018,8,1) 
t


