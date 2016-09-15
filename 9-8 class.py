import math
print (math.sqrt(16))
print ('I\'m "OK".')
print ('\\\n\\')
print ('\\\t\\')
print (r'\\\t\\')
print (True and True)
print (False and 3>0)
# True or is always True
# False and is always False
age=20
if age >= 21:
    print ('Yes, you can.')
else:
    print ('Sorry.')

b = 10
c = b > 9
print (c)
print (type(c))

import time
time.time()
print (time.time())
x = time.time()
seconds_year = 60*60*24*365
years_since = (x/seconds_year)
years = int(years_since)
print (years, "years")
seconds_day = 60*60*24
days_since = (x-((seconds_year)*(years))) / seconds_day
days = int(days_since)
print (days, "days")
hour = int(seconds_day/60/60)
hours_since = (x-((seconds_year)*(years))-((seconds_day)*(days))) / seconds_hour
print (hours_since)


input()