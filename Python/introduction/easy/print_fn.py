#!/bin/python3

"""
Problem: Read integer N. Without using string methods, print: 123...N.

Input: First line contains number N.

Output: Output the answer: 123...N
"""

import random

def main():
    n = random.randint(1,10)
    for i in range(1,(n+1)):
        print(i,end='')

if __name__ == '__main__': main()
