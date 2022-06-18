'''
C*ns*r*d Str*ngs
Someone has attempted to censor my strings by replacing every vowel with 
a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original 
uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
Notes
The vowels are given in the correct order.
The number of vowels will match the number of * characters in the censored 
string.
'''

import re

def uncensor(censored, vowels):
    vowels = [letter for letter in vowels]

    for letter in censored:
        if letter == '*':
            censored = censored.replace('*', vowels.pop(0), 1)

    return censored

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("*PP*RC*S*", "UEAE"))

# Lets try regular expressions

def uncensor_reg(censored, vowels):
    print(re.findall(r'[*]{1}.*?', censored))

uncensor_reg("Wh*r* d*d my v*w*ls g*?", "eeioeo")
