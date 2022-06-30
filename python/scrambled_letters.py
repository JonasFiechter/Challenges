'''
Scrambled Letters
Write a function that receives a list of words and a mask. Return a list of 
words, sorted alphabetically, that match the given mask.

Examples
scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "*re**") ➞ 
["creed"]

scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "***") ➞ 
["dee", "ree"]

Notes
The length of a mask will never exceed the length of the longest word in the 
word list.
'''

def scrambled(_list, mask):
    scrambled_list = []
    for w in sorted([w for w in _list if len(w) == len(mask)]):
        match = True
        for index, letter in enumerate(w):
            if letter != mask[index] and mask[index] != '*':
                match = False
                break
        
        if match:
            scrambled_list.append(w)

    return scrambled_list
                
            

    # return scrambled_list

scrambled(["red", "dreee", "ceder", "reed", "creed", "decree"], "*re**")
scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "***")