from matrix import Matrix

# reads a sudoku from a .sdk file (http://www.sadmansoftware.com/sudoku/faq19.php)
def readFromFile(path):
	sudoku = Sudoku()
	file = open(path, "r")
	y = 0
	for line in file:
		if line.startswith("#"):
			pass
		else:
			for i in range(9):
				c = line[i]
				nr = int(c) if c != '.' else 0
				sudoku.set(i, y, nr)
			y += 1
	file.close()
	return sudoku

# copy sudoku so that it doesn't reference the original and can be modified
def copy(original):
	sudoku = Sudoku()
	for y in range(9):
		for x in range(9):
			sudoku.set(x, y, original.get(x, y))
	return sudoku

# saves a sudoku to a .sdk file (http://www.sadmansoftware.com/sudoku/faq19.php)
def save(sudoku, path):
	file = open(path, "w")
	string = sudoku.toString()
	file.write(string.replace("0", "."))
	file.close()

# Sudoku is a 9 x 9 matrix.
# Values should be from 0 to 9.
# Value of 0 means the cell is empty and a space will be shown instead.
# Values are assumed to be in that range and will not be checked.
# Entering a wrong value will result in visual/logical bugs.
# Before inserting a value should be checked with the canPut function.
class Sudoku(Matrix):
	def __init__(self):
		Matrix.__init__(self, 9, 9)

	# Checks if the value can be placed into the sudoku at the coordinates x and y.
	# Before inserting a value should be checked with the canPut function.
	def canPut(self, x, y, value):
		x = int(x)		# make sure values are integers
		y = int(y)
		value = int(value)
		if self.get(x, y) != 0:				# check if empty
			return False
		for i in range(9):
			if self.get(x, i) == value:  	# check Row
				return False
			if self.get(i, y) == value:  	# check Collumn
				return False
		x = (x // 3) * 3	# find the top left of the 3x3 square to check
		y = (y // 3) * 3
		for yIterator in range(3):      	# check Square
			for xIterator in range(3):
				if self.get(x + xIterator, y + yIterator) == value:
					return False
		return True
