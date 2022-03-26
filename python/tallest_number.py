'''
Tallest Skyscraper

A city skyline can be represented as a 2-D list with 1s representing buildings. 
In the example below, the height of the tallest building is 4 
(second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

Create a function that takes a skyline (2-D list of 0's and 1's) and returns 
the height of the tallest skyscraper.
Examples

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
])
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2
'''

class TallestNumber:
	def __init__(self, matrix) -> None:
		self.matrix = matrix
		self.tallest = 0
		self.body = 0
	
	def compare_columns(self):
		for n, i in enumerate(self.matrix):
			for i_2 in i:
				if i_2 == 1:
					self.tallest = n
					return len(self.matrix) - self.tallest
					


if __name__ == '__main__':
	my_matrix = (
	[[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0],
	[0, 0, 1, 0, 1, 0],
	[0, 1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1, 1]])

	my_var = TallestNumber(my_matrix)
	print(my_var.compare_columns())