'''
Valid Division
Create a function that takes a division equation d and checks if it will return 
a whole number without decimals after dividing.

Examples
valid_division("6/3") ➞ True

valid_division("30/25") ➞ False

valid_division("0/3") ➞ True
Notes
Return "invalid" if division by zero.
'''

def valid_division(equation):
    try:
        result = equation.split('/')[0] % equation.split('/')
    except:
        return 'invalid'
    return False if result else True


print(valid_division("6/3"))
print(valid_division("30/25"))
print(valid_division("0/3"))