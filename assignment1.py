#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Vatanveer Singh". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Vatanveer Singh
Semester: <Fall <2024>
Description: <fill this in>
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year, otherwise False."
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month:int, year:int) -> int:
    "Return the maximum number of days in the given month of a specific year."
    if month == 2:  # February
        return 29 if leap_year(year) else 28
    elif month in {4, 6, 9, 11}:  # April, June, September, November
        return 30
    else:
        return 31  # All other months have 31 days

def after(date: str) -> str:
    '''
    Return the date for the next day of the given date in DD/MM/YYYY format.
    '''
    day, month, year = (int(x) for x in date.split('/'))
    day += 1  # Increment to next day

    if day > mon_max(month, year):
        day = 1  # Reset day to 1
        month += 1
        if month > 12:  # Check for year rollover
            month = 1
            year += 1
    return f"{day:02}/{month:02}/{year}"

def before(date: str) -> str:
    "Return the date for the previous day in DD/MM/YYYY format."
    day, month, year = (int(x) for x in date.split('/'))
    day -= 1  # Move to the previous day

    if day < 1:  # If the day goes below 1, move back a month
        month -= 1
        if month < 1:  # If month goes below 1, move back a year
            month = 12
            year -= 1
        day = mon_max(month, year)  # Set day to max of the previous month

    return f"{day:02}/{month:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "Check if the date is valid and in the DD/MM/YYYY format."
    try:
        day, month, year = map(int, date.split('/'))
        if year < 1 or month < 1 or month > 12:
            return False
        return 1 <= day <= mon_max(month, year)
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "Return the date after moving forward or backward by num days."
    current_date = start_date
    if num > 0:
        for _ in range(num):
            current_date = after(current_date)
    else:
        for _ in range(-num):
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    
    start_date = sys.argv[1]
    num_days_str = sys.argv[2]
    
    if not valid_date(start_date) or not num_days_str.lstrip('-').isdigit():
        usage()
    
    num_days = int(num_days_str)
    end_date = day_iter(start_date, num_days)
    day_name = day_of_week(end_date)
    print(f"The end date is {day_name}, {end_date}.")
