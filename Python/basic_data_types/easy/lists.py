#!/bin/python3

"""
Problem: Consider a list (list = []).
    - You can perform the following commands:
        - insert i e: insert integer e at position i
        - print: print the list
        - remove e: delete the first occurrence of integer e
        - append e: insert integer e at the end of the list
        - sort: sort the list
        - pop: pop the last element from the list
        - reverse: reverse the list
    - Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input: The first line contains an integer, n, denoting the number of commands.
    - Each line i of the n subsequent lines contains one of the commands described above.

Constraints: The elements added to the list must be integers.

Output: For each command of type print, print the list on a new line.
"""

def main():
    try:
        N = int(input())
    except Exception as e:
        print(e)
        print("Unacceptable value")
    else:
        count = 0
        while count < N:


if __name__ == '__main__': main()
