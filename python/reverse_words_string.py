'''
Reverse Words in a String
Given an input string, reverse the string word by word.

Examples
reverse_words("the sky is blue") ➞ "blue is sky the"

reverse_words("  hello world!  ") ➞ "world! hello"

reverse_words("a good   example") ➞ "example good a"
Notes
A word is defined as a sequence of non-space characters.
The input string may contain leading or trailing spaces. However, your 
reversed string should not contain leading or trailing spaces.
Try to solve this in linear time.
'''

#   smart solution
# def reverse_words(string):
#     return [i for i in string.split(' ')[::-1] if i]


def reverse_words(string):
    words_list = []
    temp_word = ''

    for letter in string:
        if letter != ' ':
            temp_word += letter
        elif ' ' and temp_word:
            words_list.append(temp_word)
            temp_word = ''
        else:
            continue
            
    if temp_word:
        words_list.append(temp_word)

    return ' '.join(words_list[::-1])

print(reverse_words("the sky is blue"))
print(reverse_words("  hello world!  "))
print(reverse_words("a good   example"))