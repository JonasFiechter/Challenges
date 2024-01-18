'''
Challenge: Longest Common Prefix

Write a Python function longest_common_prefix(words) that takes a list of words 
as input and returns the longest common prefix of the words.
Example:

python

words1 = ["flower", "flow", "flight"]
# Output: "fl"

words2 = ["dog", "racecar", "car"]
# Output: ""

Explanation:

    For words1, the longest common prefix is "fl" as it is the common prefix of 
    all three words.
    For words2, there is no common prefix among the words, so the output is an 
    empty string.

Constraints:

    The input list of words is non-empty and consists only of lowercase English 
    letters.

Feel free to take your time to solve this problem. Once you have a solution, you 
can compare it with the one I provide. If you have any questions or need further 
clarification, feel free to ask!
'''

def longest_common_prefix(words):
    final_prefix = ''
    for index, letter in enumerate(words[0]):
        temp_prefix = letter
        print(f'Current letter - {letter}')
        try:
            for word in words:
                print(f'word - {word} | ')
                if word[index] == letter:
                    temp_prefix = letter
                else:
                    temp_prefix = ''
                    break
        except IndexError:
            break

        final_prefix += temp_prefix
    
    print(final_prefix)
    return final_prefix



if __name__ == '__main__':
    words1 = ["flower", "flow", "flight"]
    # Output: "fl"

    words2 = ["dog", "racecar", "car"]
    # Output: ""

    longest_common_prefix(words1)
    longest_common_prefix(words2)