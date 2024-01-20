'''
Code Testing Challenge: Valid Parentheses

Problem Statement:

Given a string containing just the characters '(', ')', '{', '}', '[', and ']', 
determine if the input string is valid. An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Write a Python function is_valid_parentheses(s) to solve this problem.

Sample Parameters:

    Test cases with varying input strings, both valid and invalid.

Example:

python

s1 = "()"
# Output: True

s2 = "()[]{}"
# Output: True

s3 = "(]"
# Output: False

s4 = "([)]"
# Output: False

s5 = "{[]}"
# Output: True


Feel free to take your time to solve this problem. Once you have a solution, you 
can compare it with the one I provide. If you have any questions or need further 
clarification, feel free to ask!
'''

def is_valid_parentheses(s):
    map_parentesis = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    opened = []
    for char in s:
        if char in map_parentesis.values():
            opened.append(char)
        if char in map_parentesis.keys() and map_parentesis[char] not in opened:
            return False
        elif char in map_parentesis.keys() and map_parentesis[char] == opened[-1]:
            opened.remove(map_parentesis[char])

    return True if not opened else False

if __name__ == '__main__':
    s1 = "()"
    print(is_valid_parentheses(s1))
    # Output: True

    s2 = "()[]{}"
    print(is_valid_parentheses(s2))
    # Output: True

    s3 = "(]"
    print(is_valid_parentheses(s3))
    # Output: False

    s4 = "([)]"
    print(is_valid_parentheses(s4))
    # Output: False

    s5 = "{[]}"
    print(is_valid_parentheses(s5))
    # Output: True