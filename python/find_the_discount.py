'''
Find the Discount
Create a function that takes two arguments: the original price and the discount percentage as 
integers and returns the final price after the discount.

Alternative Text

Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
Notes
Your answer should be rounded to two decimal places.
'''


def find_discount(value, discount):
    value -= (value * (discount / 100))
    print(value)


if __name__ == '__main__':
    find_discount(1500, 50)
    find_discount(89, 20)
    find_discount(100, 75)