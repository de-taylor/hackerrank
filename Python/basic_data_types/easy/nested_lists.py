#!/bin/python3

"""
Problem: Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
    - If there are any students with the same grade, print their names alphabetically.

Input: 
    - First line contains an integer, N, the number of students.
    - The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints:
    - 2 <= N <= 5
    - There will now always be 1+ students with the second lowest grade.

Output: Print the names of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""

from operator import itemgetter

def main():
    # accept student input
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    
    # sort students with itemgetter
    stu_sort = sorted(students, key=itemgetter(1,0))

    # identify the second lowest grade
    for n,s in stu_sort:
        if s == stu_sort[0][1]: continue
        else:
            seclow = s
            break

    # print, in order, the names of those who have the second lowest score
    for n,s in stu_sort: 
        if s == seclow: print(n)

if __name__ == '__main__': main()
