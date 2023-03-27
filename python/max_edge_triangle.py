'''
Maximum Edge of a Triangle
Create a function that finds the maximum range of a triangle's third edge, 
where the side lengths are all integers.

Examples
next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10
Notes
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.
''' 

def next_edge(side_1, side_2):
    max = (side_1 + side_2) - 1
    return max


if __name__ == "__main__":
    print(next_edge(8, 10))
    print(next_edge(5, 7))
    print(next_edge(9, 2))