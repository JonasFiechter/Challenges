'''
Challenge: String Reversal

Write a function or program that takes a string as input and returns the 
reversed version of that string. Your implementation should reverse the 
characters of the string without using built-in reverse functions.

Example:

Input: "Hello, World!"

Output: "!dlroW ,olleH"

Feel free to implement this challenge in your preferred programming language. 
If you'd like, you can provide the solution in pseudocode or multiple languages. 
Good luck, and have fun coding!
'''

def string_reversal(my_string):
    new_string = ''
    for char in my_string[::-1]:
        new_string += char

    return new_string


if __name__ == '__main__':
    print(string_reversal("Hello, World!"))