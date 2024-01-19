'''
Write a function or program that generates the Fibonacci sequence up to a 
specified limit. The Fibonacci sequence starts with 0 and 1, and each subsequent 
number is the sum of the two preceding ones.

Example:

Input: 10

Output: [0, 1, 1, 2, 3, 5, 8]
'''

def fibonacci(limit):
    init = [0, 1]
    value = 0
    index = 0
    while value <= limit:
        value = init[index] + init[index + 1]
        index += 1
        if value <= limit:
            init.append(value)
    
    return init


if __name__ == '__main__':
    print(fibonacci(10))