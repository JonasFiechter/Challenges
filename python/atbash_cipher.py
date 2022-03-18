'''
The Atbash cipher is an encryption method in which each letter of a word is replaced with 
its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.
Examples

atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

Notes
    Capitalisation should be retained.
    Non-alphabetic characters should not be altered.
'''

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 
'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
'X', 'Y', 'Z']

def atbash(text):
    new_text = ''
    upper = False
    for letter in text:
        if letter == letter.upper():
            upper = True
        for n, i in enumerate(alpha):
            if letter.upper() == i:
                letter = ''
                if upper:
                    new_text += alpha[(n + 1) * (-1)]
                    upper = False
                else:
                    new_text += alpha[(n + 1) * (-1)].lower()
        new_text += letter
        
    return new_text

if __name__ == '__main__':
    print(atbash('apple'))
    print(atbash('Hello world!!'))
    print(atbash('Christmas is the 25th of December'))