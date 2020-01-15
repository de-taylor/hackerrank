#!/bin/python3

"""
Problem: Read an integer, n. For all non-negative i < n, print i**2.

Input: One integer, n.

Constraints: 1 <= n <= 20

Output: Print n lines, one for each value i.
"""

import random

def main():
    n = random.randint(1,21)
    for i in range(0,n): print(i**2)

if __name__ == '__main__': main()
