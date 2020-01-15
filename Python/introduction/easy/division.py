#!/bin/python3

"""
Problem: Read two integers and print two lines. The first line should contain integer division a//b. The second line should contain float division, a/b.
- No rounding

Input: First line should have integer a, second line should have integer b.

Output: Print the two divisions as described above.
"""

def main():
     a = int(input())
     b = int(input())

     print(a//b)
     print(a/b)

if __name__ == '__main__': main()
