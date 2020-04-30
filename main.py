from sudoku import Sudoku, readFromFile, copy, save
from textbox import TextBox
from random import randint
import sys
import board
import time
import platform
if platform.system() == "Windows":
	import cursor_windows as cursor
else:
	import cursor


help_message = "Commands:\n\
 \n\
help\n\
load <filename>\n\
gen\n\
solve\n\
save <filename>\n\
interval <value>\n\
clear\n\
exit\n\
"

# variable which will loop around when it reaches it's max value
class LoopVariable:
	def __init__(self, start, end, i=1):
		self.start = start
		self.end = end
		self.i = i
		self.current = start
	
	def increment(self):
		self.current += self.i
		self.current = (self.current - self.start) % (self.end - self.start) + self.start

	def get(self):
		return self.current

	def set(self, value):
		self.current = value


class SudokuLoopVar(LoopVariable):
	def __init__(self, current, increment):
		LoopVariable.__init__(self, 1, 10, increment)
		LoopVariable.set(self, current)


def solve(sudoku, x, y, display=True, getStart=lambda: 1):
	time.sleep(interval)			# interval between function calls for better visualisation
	if x > 8:						
		x = 0						# simulating for loop in recursive funtion
		y += 1
	if y > 8:
		return True					# end condition
	if sudoku.get(x, y) == 0:	# if cell is empty
		nr = getStart()
		i = SudokuLoopVar(nr, randint(1, 2)) # loop through all the values
		while 1:
			if sudoku.canPut(x, y, i.get()):	# if value can be put
				sudoku.set(x, y, i.get())		
				if display:
					board.setValue(x, y, i.get())
				if solve(sudoku, x + 1, y, display, getStart):	# go to next cell
					return True
				else:
					sudoku.set(x, y, 0)
					if display:
						board.setValue(x, y, 0)
			i.increment()			# next value
			if i.get() == nr:
				break
	elif solve(sudoku, x + 1, y, display, getStart):	#if cell is not empty, go to next cell
		return True
	return False

interval = .01
board.init()

prompt = TextBox(x=0, y=board.height + 1, width=board.width)
prompt.message("Enter Command:")

help = TextBox(x=board.width + 2, y=1, width=16, height=board.height)
help.message(help_message)

info = TextBox(x=board.width + 2, y=help.y + help.height, width=help.width, height=3)

sudoku = Sudoku()
board.show(sudoku)

while 1:
	cursor.goto(prompt.x, prompt.y + 1)
	cursor.writeStringToCursorPos(" " * 20)
	command = input(">>> ")

	cursor.move_up()
	cursor.y += 1

	args = command.split(" ")
	if args[0] == "help":
		if args[1] == "":
			help.message(help_message)
		elif args[1] == "load":
			help.message(
				"Loads a .sdk\n\
file into\n\
the board\n\
 \n\
usage:\n\
load <filename>"
			)
		elif args[1] == "gen":
			help.message(
				"Generates a\n\
random solved\n\
sudoku\n\
 \n\
usage:\n\
gen"
			)
		elif args[1] == "solve":
			help.message(
				"Solves the\n\
current sudoku\n\
 \n\
usage:\n\
solve"
			)
		elif args[1] == "save":
			help.message(
				"Saves the\n\
current sudoku\n\
in a .sdk file\n\
 \n\
usage:\n\
save <filename>"
			)
		elif args[1] == "interval":
			help.message(
				"Sets the interval\n\
between each solve\n\
tick\n\
I used to slow down\n\
the algorithm for\n\
better visualisation\n\
usage:\n\
interval <value>\n\
interval 0\n\
for max speed"
			)
		elif args[1] == "clear":
			help.message(
				"Clears the\n\
board\n\
usage:\n\
clear"
			)
		elif args[1] == "exit":
			help.message(
				"exits the prompt"
			)
	elif args[0] == "load":
		sudoku = readFromFile(args[1] if args[1].endswith(".sdk") else args[1] + ".sdk")
		board.show(sudoku)
		info.message("Loaded sudoku\n{}".format(args[1]))
	elif args[0] == "gen":
		sudoku = Sudoku()
		board.show(sudoku)
		info.message("Generating...")
		solve(sudoku, 0, 0, display=True, getStart=lambda: randint(1, 9))
		#last_removed = [0, 0, 0]
		#while solve(copy(sudoku), 0, 0, display=True):
		#	board.show(sudoku)
		#	last_removed[0] = randint(0, 8)
		#	last_removed[1] = randint(0, 8)
		#	last_removed[2] = sudoku.get(last_removed[0], last_removed[1])
		#	sudoku.set(last_removed[0], last_removed[1], 0)
		#sudoku.set(last_removed[0], last_removed[1], last_removed[2])
		info.message("Done")
		board.show(sudoku)
	elif args[0] == "solve":
		info.message("Solving...")
		solve(sudoku, 0, 0, display=True)
		info.message("Done")
	elif args[0] == "save":
		save(sudoku, args[1])
	elif args[0] == "interval":
		interval = float(args[1])
		info.message("Interval: {0}".format(interval))
	elif args[0] == "clear":
		sudoku = Sudoku()
		board.show(sudoku)
	elif args[0] == "exit":
		break
	else:
		info.message("Not a command\nType help to\nshow them")

	

board.end()
