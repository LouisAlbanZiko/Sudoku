from sudoku import Sudoku, readFromFile
from textbox import TextBox
import board

def solve(sudoku, x, y):
	if x > 8:	# if x > 8
		y += 1	# go to next row
		x = 0
	if y > 8:			# if y > 8
		return True		# we are at the end, sudoku is solved, return
	if sudoku.get(x, y) != 0:			# if cell is not empty
		return solve(sudoku, x + 1, y)	# go to next cell
	else:
		for nr in range(1, 10):		# go through all the options
			if sudoku.canPut(x, y, nr):	# if we nr can be put
				sudoku.set(x, y, nr)	# set value
				solved = solve(sudoku, x + 1, y)	# go to next cell
				if solved:		# if solved
					return True	# sudoku is solved, return
				else:						# otherwise
					sudoku.set(x, y, 0)		# make the cell empty again
	# if we went through all the values it's a dead end
	return False	# go back to previous cell

board.init()

help = TextBox(x=board.width + 2, y=1, width=16, height=board.height)
help.message("")

sudoku = readFromFile('test.sdk')
board.show(sudoku)

solve(sudoku, 0, 0)
board.show(sudoku)

board.end()


				