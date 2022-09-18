'''
Find the Highest Integer in the List Using Recursion
Create a function that finds the highest integer in the list using recursion.

Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8
Notes
Please use the recursion to solve this (not the max() method).
'''

def find_highest(arg: list, index: int = 0, higher: int = 0):
    limit = len(arg) - 1

    if arg[index] > higher:
        higher = arg[index]

    if index == limit:
        return higher
    
    else:
        return find_highest(arg, index + 1, higher)

list_1 = [12, 3, 4, 50, 6]
print(find_highest(list_1))