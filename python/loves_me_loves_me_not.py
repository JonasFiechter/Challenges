'''
Loves Me, Loves Me Not...
"Loves me, loves me not" is a traditional game in which a person plucks off all 
the petals of a flower one by one, saying the phrase "Loves me" and "Loves me 
not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" 
and "Loves me not" for every alternating petal, and return the last phrase in 
all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, 
LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"
Notes
Remember to return a string.
The first phrase is always "Loves me".
'''

#  Solution 1
def loves_me(num):
    phrase = ''
    for i in range(num):
        if i % 2 == 0: 
            if i == (num - 1):
                phrase += 'LOVES ME'
                break
            phrase += 'Loves me, '
        else: 
            if i == (num - 1):
                phrase += 'LOVES ME NOT'
                break
            phrase += 'Loves me not, '
    
    return phrase

print(loves_me(3))

#  Solution 2
def loves_me_sm(num):
    phrase = ''
    for i in range(num):
        if i % 2 == 0 and i != (num - 1): 
            phrase += 'Loves me, '
        elif i % 2 != 0 and i != (num - 1): 
            phrase += 'Loves me not, '
        else:
            if i % 2 == 0:
                phrase += 'LOVES ME'
            else:
                phrase += 'LOVES ME NOT'
    
    return phrase

print(loves_me_sm(6))

# Lets try recursion
def loves_me_rec(num, phrase=''):
    add = 'Loves me, '
    phrase += add
    num -= 1
    print(f'{phrase} {num} before if')
    if num >= 1:
        return loves_me_rec(num - 1, phrase=phrase + add.replace(', ', ' not, '))
    else: return phrase

print(loves_me_rec(3))