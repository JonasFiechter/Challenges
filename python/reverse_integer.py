'''
Challenge: Reverse Integer

Given a signed 32-bit integer x, reverse its digits. Return 0 if the result 
overflows the 32-bit signed integer range.

Write a Python function reverse_integer(x) to solve this problem.
Example:

python

x = 123

# Output: 321

python

x = -123

# Output: -321

python

x = 120

# Output: 21

Constraints:

    The input integer is a 32-bit signed integer, within the range 
    [−2^31, 2^31 − 1].

Feel free to take your time to solve this problem. Once you have a solution, you 
can compare it with the one I provide. If you have any questions or need further 
clarification, feel free to ask!

'''

def reverse_integer(x):
    reverse = ''
    negative = False
    while True:
        print(x)
        if x > 0:
             negative = True
             n = x % 10
             x = x // 10
        else:
             n = x % -10
             x = x // -10
        print(f'N -> {n}')
        if n < 0:
            reverse += str(n*(-1))
        else:
            reverse += str(n)
        print(x)
        if x == 0 or x == -1:
            if negative:
                return int('-' + reverse)
            return int(reverse)
    

if __name__ == '__main__':
    # reverse_integer(123)
    print(reverse_integer(-123))
    # reverse_integer(120)