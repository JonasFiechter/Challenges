'''
Write a function that takes the base and height of a triangle and return its area.
'''

class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def triangle_area(self):
        return (self.x * self.y) / 2


if __name__ == '__main__':
    var = Triangle(10, 10)
    print(var.triangle_area())