'''
Basic Calculator
Create a function that takes two numbers and a mathematical operator + - / * 
and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
Notes
If the input tries to divide by 0, return: "Can't divide by 0!"
'''
# solution 1
def calculator(num_1, operator, num_2):

    my_dict = { 
                '*': (num_1 * num_2), 
                '+': (num_1 + num_2), 
                '-': (num_1 - num_2)
                }

    if num_1 != 0 and num_2 != 0: 
        my_dict['/'] = (num_1 / num_2)

    if num_1 == 0 or num_2 == 0 and operator == '/': 
        return('cannot divide by 0')

    if type(num_1) != int or type(num_2) != int: 
        return('invalid input for int or operator')

    elif operator not in ['/', '*', '+', '-']: 
        return('invalid operator')

    else: 
        return(my_dict[operator])

# solution 2
def calculator_2(num_1, operator, num_2):
    if num_1 == 0 or num_2 == 0 and operator == '/':
        return('cannot divide by 0')
    if type(num_1) != int or type(num_2) != int:
        return('invalid input for int or operator')
    elif operator not in ['/', '*', '+', '-']: 
        return('invalid operator')
    else:
        if operator == '/': return num_1 / num_2
        elif operator == '*': return num_1 * num_2
        elif operator == '+': return num_1 + num_2
        elif operator == '-': return num_1 - num_2

print(calculator(0, '/', 2))
print(calculator(1, '/', 2))
print(calculator(1, '+', 0))
print(calculator(1, '-', 0))
print(calculator(1, '*', 0))