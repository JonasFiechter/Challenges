'''
Code Testing Challenge: Rotate Image

Problem Statement:

You are given an n x n 2D matrix representing an image. Rotate the image by 90 
degrees (clockwise).

Write a Python function rotate_image(matrix) to solve this problem.

Sample Parameters:

    Test cases with varying input matrices.

Example:

python

matrix1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
# After rotation: 
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

matrix2 = [
  [5, 1, 9, 11],
  [2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
]
# After rotation: 
# [
#   [15, 13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7, 10, 11]
# ]

Feel free to take your time to solve this problem. Once you have a solution, you 
can compare it with the one I provide. If you have any questions or need further 
clarification, feel free to ask!
'''

def rotate_image(matrix):
    output = [[] for col in matrix]
    for row in matrix[::-1]:
        for col_index, column in enumerate(row):
            output[col_index].append(column)

    return output

if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    

    print(rotate_image(matrix1))
    print(rotate_image(matrix2))