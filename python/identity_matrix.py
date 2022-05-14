'''
identity Matrix
An identity matrix is defined as a square matrix with 1s running from the top left 
of the square to the bottom right. The rest are 0s. The identity matrix has applications 
ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n 
dimensions. For this challenge, if the integer is negative, return the mirror image of 
the identity matrix of n x n dimensions.. It does not matter if the mirror image is 
left-right or top-bottom.

Examples
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []
'''

'''
identity Matrix
An identity matrix is defined as a square matrix with 1s running from the top left 
of the square to the bottom right. The rest are 0s. The identity matrix has applications 
ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n 
dimensions. For this challenge, if the integer is negative, return the mirror image of 
the identity matrix of n x n dimensions.. It does not matter if the mirror image is 
left-right or top-bottom.

Examples
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []
'''


class Matrix:
    def __init__(self, integer) -> None:
        self.integer = integer
        self.matrix = []

    def new_line_for_negative(self, current_line):
        line = []
        for column in range(-1, self.integer -1, -1):
            if column == current_line:
                line.append(1)
            else: 
                line.append(0)
        print(line)
        return line

    def new_line(self, current_line):
        line = []
        for column in range(self.integer):
            if column == current_line:
                line.append(1)
            else:
                line.append(0)
        print(line)

    def id_matrix(self):
        current_line = 0
        if self.integer < 0:
            current_line = self.integer
            for line in range(self.integer * (-1)):
                self.matrix.append(self.new_line_for_negative(current_line))
                current_line += 1
        else:
            for line in range(self.integer):
                self.matrix.append(self.new_line(current_line))
                current_line += 1


if __name__ == '__main__':
    a = Matrix(30)
    a.id_matrix()