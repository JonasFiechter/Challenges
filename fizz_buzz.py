"""
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown 
in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.

"""


class FizzBuzz:
    def __init__(self, number) -> None:
        self.number = number

    def divide_number(self):
        f = self.number % 3
        b = self.number % 5

        return f, b
    
    def check_number(self, f, b):
        if f + b == 0:
            return 'FizzBuzz'
        
        elif f == 0:
            return 'Fizz'
        
        elif b == 0:
            return 'Buzz'

        else:
            return str(self.number)

def main():
    while True:
        i = int(input('Place any number: '))
        result = FizzBuzz(number=i)
        f, b = result.divide_number()
        print(result.check_number(f, b))


if __name__ == '__main__':
    main()