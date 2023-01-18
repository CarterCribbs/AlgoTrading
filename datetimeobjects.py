from datetime import datetime
from datetime import timedelta


dt1 = datetime.now()
#print(f'Approach #1: {dt1}')
#print(f'Year: {dt1.year}')
#print(f'TimeZone: {dt1.tzinfo}')

# constructor
dt2 = datetime(year=2002, month=9, day=9)
#print(f'My birthday is: {dt2}')


#can extract date or time from a datetime object
#print(f'Date: {dt1.date()}')
#print(f'Type: {type(dt1.date())}')

td1 = timedelta(days=4)
#print(f'Time difference: {td1}')
td2 = timedelta(weeks=2, days=2)
#print(f'addition: {td1+td2}')
#total seocnds menthod
#print(f'Total seconds in 20 Days: {(td1+td2).total_seconds()}')

#strings to date time objects

now_str= '4-1-2023'
now = datetime.strptime(now_str, "%d-%m-%Y")
#print(now_str)
#print(now)

#creating timezone aware object
now_tz_aware = datetime.now().astimezone()
print(now_tz_aware)
print(now_tz_aware.tzinfo)
#make it time zone naive
new_tz_naive = now_tz_aware.replace(tzinfo=None)