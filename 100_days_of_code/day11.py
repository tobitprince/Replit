"""
This module calculates the number of seconds in a year and a leap year based on user input.
"""

DAYS_IN_YEAR = 365
DAYS_IN_LEAPYEAR = 366
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

days_this_year = int(input("How many days are in this year?"))

RESULT = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
LEAPYEAR_RESULT = DAYS_IN_LEAPYEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

if days_this_year == 366:
    print("Number of seconds in a leap year are", LEAPYEAR_RESULT)
else:
    print("Number of seconds in a year are", RESULT)
