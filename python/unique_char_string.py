'''
Code Testing Challenge: First Unique Character in a String

Problem Statement:

Given a string, find the first non-repeating character and return its index. If 
it doesn't exist, return -1.

Write a Python function first_unique_char(s) to solve this problem.

Sample Parameters:

    Test cases with varying input strings.

Example:

python

s1 = "leetcode"
# Output: 0 (Explanation: 'l' is the first non-repeating character at index 0.)

s2 = "loveleetcode"
# Output: 2 (Explanation: 'v' is the first non-repeating character at index 2.)

s3 = "aabbcc"
# Output: -1 (Explanation: There is no non-repeating character.)
'''

def first_unique_char(s):
    count_list = [char for char in s]
    for index, char in enumerate(s):
        if count_list.count(char) < 2:
            return index

    return -1 

if __name__ == '__main__':
    print(first_unique_char('leetcode'))
    print(first_unique_char('loveleetcode'))
    print(first_unique_char('aabbcc'))