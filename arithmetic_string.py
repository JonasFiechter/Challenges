'''
Create a function to perform basic arithmetic operations that includes 
addition, subtraction, multiplication and division on a string number 
(e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. 
For the challenge, we are going to have only two numbers between 1 valid 
operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals 
"0" return -1.

For example:

"15 // 0"  ➞ -1
'''
import re


class arithmetic: #  Class Solution
    def __init__(self, data) -> None:
        self.data = data
        self.a = None
        self.b = None
        self.operator = None

    def separate(self):
        self.a, self.b = tuple(re.findall(r'[0-9]+', self.data))
        return self.a, self.b

    def define_operator(self):
        self.operator = re.findall(r'\+|-|\*|//', self.data)[0]
        return self.operator

    def calculate(self):
        self.separate()
        self.define_operator()
        
        if self.operator == '+': return int(self.a) + int(self.b)
        elif self.operator == '-': return int(self.a) - int(self.b)
        elif self.operator == '*': return int(self.a) * int(self.b)
        elif self.operator == '//': return int(self.a) // int(self.b)


def func_arithmetic(data):
    a, b = tuple(re.findall(r'[0-9]+', data))
    operator = re.findall(r'\+|-|\*|//', data)[0]

    if operator == '+': return int(a) + int(b)
    elif operator == '-': return int(a) - int(b)
    elif operator == '*': return int(a) * int(b)
    elif operator == '//': return int(a) // int(b)


if __name__ == '__main__':
    data='1200 * 255'
    var_1 = arithmetic(data)

    print(f'Testing results with class, data = '
          f'"{var_1.data}": {var_1.calculate()}')

    print(f'Testing results with function, data = '
          f'"{data}": {func_arithmetic(data)}')