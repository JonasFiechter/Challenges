'''
Censor Words Longer Than Four Characters
Create a function that takes a string and censors words over four characters with .

Examples
censor("The code is fourty") ➞ "The code is **"

censor("Two plus three is five") ➞ "Two plus ** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa  1234 "
Notes
Don't censor words with exactly four characters.
If all words have four characters or less, return the original string.
The amount of * is the same as the length of the word.
'''

def censor(phrase):
    list_of_words = phrase.split(' ')

    for index, word in enumerate(list_of_words):
        if len(word) > 4:
            list_of_words[index] = '**'
            
    return ' '.join(list_of_words)

# print(censor("The code is fourty"))

def censor_2(phrase, i=0):
    if len(phrase.split(' ')[i]) > 4:
        phrase = phrase.replace(phrase.split(' ')[i], '**')
    if (i + 1) == len(phrase.split(' ')):
        return phrase
    else:
        return censor_2(phrase, i+1)

print(censor_2("The code is fourty"))