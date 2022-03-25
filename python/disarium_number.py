'''
Disarium Number

A number is said to be Disarium if the sum of its digits raised to their 
respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
Examples

is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True

Notes
    Position of the digit is 1-indexed.
    A recursive version of this challenge can be found via this link.
'''

class Disarium:
    def __init__(self, number) -> None:
        self.number = number
    
    def is_disarium(self):
        sum_list = []
        result = 0
        for n, i in enumerate(list(str(self.number))):
            sum_list.append(int(i) ** (n + 1))
        
        for i in sum_list:
            result += i

        if result == self.number:
            return True
        else:
            return False


if __name__ == '__main__':
    var_1 = Disarium(518)
    print(var_1.is_disarium())
