'''
Tic Tac Toe
Given a 3x3 matrix of a completed tic-tac-toe game, create a function that 
returns whether the game is a win for "X", "O", or a "Draw", where "X" and "O" 
represent themselves on the matrix, and "E" represents an empty spot.

Examples
tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]) ➞ "X"

tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]) ➞ "O"

tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]) ➞ "Draw"
Notes
Make sure that if O wins, you return the letter "O" and not the integer 0 (zero) 
and if it's a draw, make sure you return the capitalised word "Draw". If you 
return "X" or "O", make sure they're capitalised too.
'''

def tic_tac_toe(matrix):
    diagonals = [[], []]
    columns = [[], [], []]
    d1 = [(0, 0), (1, 1), (2, 2)]
    d2 = [(0, 2), (1, 1), (2, 0)]
    c1, c2, c3 = [
        [(0, 0), (1, 0), (2, 0)], 
        [(0, 1), (1, 1), (2, 1)], 
        [(0, 2), (1, 2), (2, 2)]]

    #check line
    for line in matrix:
        if line.count('X') == 3:
            return 'X'
        elif line.count('O') == 3:
            return 'O'
    
    # check diagonal and colums
    for x_index, line in enumerate(matrix):
        for y_index, mark in enumerate(line):
            if (x_index, y_index) in d1:
                diagonals[0].append(mark)
            elif (x_index, y_index) in d2:
                diagonals[1].append(mark)
            if (x_index, y_index) in c1:
                columns[0].append(mark)
            elif (x_index, y_index) in c2:
                columns[1].append(mark)
            elif (x_index, y_index) in c3:
                columns[2].append(mark)

    for diagonal in diagonals:
        if diagonal.count('X') == 3:
            return 'X'
        elif diagonal.count('O') == 3:
            return 'O'
        
    for column in columns:
        if column.count('X') == 3:
            return 'X'
        elif column.count('O') == 3:
            return 'O'

    return "Draw"
    

if __name__ == '__main__':
    print(tic_tac_toe(
        [
            ["X", "O", "X"],
            ["O", "X",  "O"],
            ["O", "X",  "X"]
        ]
    ))
    print(tic_tac_toe(
        [
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["E", "X", "X"]
        ]
    ))
    print(tic_tac_toe(
        [
            ["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "X", "O"]
        ]
    ))
    print(tic_tac_toe(
        [
            ["X", "X", "E"],
            ["X", "O", "E"],
            ["E", "O", "X"]
        ]
    ))