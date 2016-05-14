'''
Problem 19: Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.

And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime

is_done = False
year = 1901
month = 1
num_of_sundays = 0
while not is_done:
    if datetime.datetime(year, month, 1).weekday() == 6:
        num_of_sundays += 1
        
    if year > 2000: 
        is_done = True
        
    if month >= 12: 
        month = 1
        year += 1
    else:
        month += 1

print num_of_sundays