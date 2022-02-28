'''
Create a class with a few functions like these examples.

magic.replace("string", 'char', char') is a function that replaces all of the specified characters
with different specified characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string with truncated spaces at both the 
beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are between the 
specified indexes. If the length of the new list is 0, return -1.
'''


class Magic:
    def __init__(self):
        pass

    def replace_letter(string, character, new_character):  # Traditional method to replace
        new_string = ''
        for c in string:
            if c == character:
                new_string += new_character
            else:
                new_string += c
        return new_string

    def replace_comprehension(string, character, new_character):  # Alternative method to replace 
        return ''.join(c.replace(character, new_character) for c in string)

    def str_length(string):        
        return len(string)

    def list_slice(string:str, tuple:tuple):
        if len(string) == 0:
            return -1
        return string[tuple[0]:tuple[1]]

    def trim(string):
        return ' ' + string + ' '


if __name__ == '__main__':
    var = 'Beyond files and things'
    print(Magic.replace_letter(var, 'a', '#'))
    print(Magic.replace_comprehension(var, 'a', '@'))
    print(Magic.str_length(f'length of string: {var}'))
    print(Magic.list_slice(var,(2, 4)))
    print(Magic.trim(var))