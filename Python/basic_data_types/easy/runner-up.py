#!/bin/python3

"""
Problem: Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input: The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints:
    - 2 <= n <= 10
    - -100 <= A[i] <= 100

Output: Print the runner-up score.
"""

import random

def main():
    n = random.randint(2,100)
    arr = [random.randint(0,10) for iter in range(n)]

    sarr = set(arr) # remove duplicate values
    sarr.remove(max(sarr)) # remove the max value
    print(max(sarr)) # print the new max value
    print(arr)


if __name__ == '__main__': main()
