#!/bin/python3    

"""
Problem: Given an integer, n, perform the following conditional actions:
    - If n is odd, print "Weird"
    - If n is even and in the inclusive range of 2 - 5, print "Not Weird"
    - If n is even and in the inclusive range of 6 - 20, print "Weird"
    - If n is even and greater than 20, print "Not Weird"

Input: A single line with a positive integer, n.

Constraints: 1 <= n <= 100

Output: Print "Weird" if conditions are met, and "Not Weird" if conditions are met.
"""

import random

def main():
    n =  random.randint(1,100)

    if n % 2 != 0 or n in range(6,21):
       print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__': main()
