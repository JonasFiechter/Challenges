'''
Write a function that takes a positive integer num and calculates how many dots exist in a 
pentagonal shape around the center dot on the Nth iteration.

You can see the first iteration is only a single dot. On the second, there are 6 
dots. On the third, there are 16 dots, and on the fourth there are 31 dots.
'''


class PengagonalNumber:
    def __init__(self, number):
        self.number = number
    
    def create(self):
        center = 1
        border = 0

        for i in range(self.number - 1):
            center += border
            border += 5
        return (center + border)


def main(number):
    p = PengagonalNumber(number=number)
    print(p.create())


if __name__ == '__main__':
    number = int(input('Place a number: '))
    main(number)

