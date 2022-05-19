'''
Get Students with Names and Top Notes
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } 
and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
Notes
'''
import time

#                      DICT STRUCTURE
#             string    %     string      %
#             key:    value , key:     value
johns_dict = {"name": "John", "notes": [3, 5, 4]}
max_dict = {"name": "Max", "notes": [1, 4, 6]}
zygmund_dict = { "name": "Zygmund", "notes": [1, 2, 3] }


def top_note_hard_mode(dict):
    max_note = 0
    for note in dict['notes']:
        if note > max_note:
            max_note = note
    
    return max_note

def top_note_hard_mode(dict):
    print('funcao faz outra coisa')

