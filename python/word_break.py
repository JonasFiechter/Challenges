'''
Problem:

Given a string s and a dictionary of words wordDict, write a function to 
determine if s can be segmented into a space-separated sequence of one or more 
dictionary words.

For example, given the string s = "leetcode" and wordDict = ["leet", "code"], 
return true because "leetcode" can be segmented into "leet code".

Implement a function:

python

def word_break(s, wordDict):
    # Your code here
    pass

# Example usage:
s = "leetcode"
wordDict = ["leet", "code"]
result = word_break(s, wordDict)
print(result)  # Expected output: True

Constraints:

    The input string s consists of lowercase English letters.
    The length of s is between 1 and 300.
    The dictionary wordDict contains distinct words, and the number of words is 
    between 1 and 1000.
    Each word in wordDict is between 1 and 20 characters long.

Note:

    You may assume no duplicates in the dictionary.
    You may use any valid data structures or algorithms to solve the problem.

This problem is a classic example of dynamic programming and can be solved using 
techniques like memoization or bottom-up DP. Try to come up with an efficient 
solution!
'''
def word_break(word_dict:list, s:str):
    segmented = []
    for word in word_dict:
        if word in s:
            new_word = s.replace(word, '')
            segmented.append(word)
            

if __name__ == '__main__':
    test_cases = [
        (["leet", "code"], "leetcode", True),                  # Example from prompt
        # (["apple", "pen"], "applepen", True),                  # Words: ["apple", "pen"]
        # (["cats", "dog", "sand", "and", "cat"], "catsandog", False),  # Cannot be segmented
        # (["apple", "banana", "orange"], "pineapple", False),   # No matching words in string
        # (["car", "ca", "rs"], "cars", True),                   # Segmented as "ca" + "rs"
        # (["aaaa", "aaa"], "aaaaaaa", False),                   # Ambiguity between "aaaa" and "aaa"
        # (["a", "aa", "aaa"], "aaaaaaa", True),                 # Segmented as "a" + "aa" + "aaa"
        # (["ab", "abc", "cd", "def", "abcd"], "abcdefabcd", True),  # Segmented as "ab" + "cd" + "abcd"
        # (["a", "b", "bb", "ccc"], "abbbccc", False),          # No valid segmentation
        # (["aaaa", "aaa", "aa"], "aaaaaaaa", False),           # Ambiguity between "aaaa" and "aaa"
        # (["a", "aa", "aaa", "aaaa"], "aaaaaaaa", False),      # Ambiguity between all options
    ]

    for word_dict, s, output in test_cases:
        if word_break(word_dict, s) == output:
            print(f'Test passed / case: {s}')
        else:
            print(f'Test failed! case: {s}')
