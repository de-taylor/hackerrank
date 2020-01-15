#!/bin/python3

"""
Problem: You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z.

Input: Four integers, X, Y, Z, and N on four separate lines, respectively.

Constraints: Print the list in lexicographic increasing order.

Output: An ordered list of all possible outputs.
"""

import random

def main():
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    n = random.randint(1,10)

    # list comprehension
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])

if __name__ == '__main__': main()
