#!/bin/python3

"""
Problem: We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identiy leap years:
    - The year can be evenly divided by 4, is a leap year, unles:
        - The year can be evenly divided by 100, it is NOT a leap year, unless:
            - The year is also evenly divisible by 400. Then it is a leap year.
    - Therefore, 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, and 2300 are NOT leap years.

Task: You are given the year, and you have to write a function to check if the year is leap or not.

Input: Read y, the year to be checked.


Constraints: 1900 <= y <= 10**5

Output: Function must return boolean True or False
"""

import random

def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap

def main():
    test_cases = [1900, 2100, 2016, 2017, 4000, 10**5]

#    y = random.randint(1900,(10**5)+1) 

    for y in test_cases:
        print(y)
        print(is_leap(y))

if __name__ == '__main__': main()
