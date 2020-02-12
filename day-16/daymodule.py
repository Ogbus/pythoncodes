from datetime import datetime
from datetime import date
# print(dir(datetime))

# Get the current day, month, year, hour, minute and timestamp from time date module
today = datetime.now()
print(today)
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
second = today.second
timestamp = today.timestamp()
print(day, month, year, hour, minute)
print('timestamp:', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Format the current date using in this format: "%m/%d/%Y, %H:%M:%S")
now_today = datetime.now()
time = now_today.strftime("%H:%M:%S")
print('current time', time)
year_time = now_today.strftime("%m/%d/%y, %H:%M:%S")
print('Current yeear and time', year_time)
year_timee = now_today.strftime("%d/%m/%y, %H:%M:%S")
print('Current yeear and time', year_timee)

# Today is 5 December, 2019. Change this time string to time.
string_date = "11 February, 2020"
print('string_date', string_date)
date_object = datetime.strptime(string_date, "%d %B, %Y")
print('date_object', date_object)

# Calculate the time difference from now to new year.
currrent_day = date(year=2020, month=2, day=11)
new_yaer = date(year=2021, month=1, day=1)
remain_date_to_new_year = new_yaer - currrent_day
print(remain_date_to_new_year)

# Calculate the time difference between 1 January 1970 and now.
old_date = date(year=1970, month=1, day=1)
currrent_date = date(year=2020, month=2, day=11)
difference_in_date = currrent_date - old_date
print(difference_in_date)