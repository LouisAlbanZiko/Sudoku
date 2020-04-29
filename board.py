from matrix import Matrix
import sys
import platform
if platform.system() == "Windows":
	import cursor_windows as cursor
else:
	import cursor
import sudoku

vertical = "\u2551"
verticalThin = "\u2502"
horizontal = "\u2550"
horizontalThin = "\u2500"
intersection = "\u256C"
intersectionThin = "\u253C"
intersectionVerticalThin = "\u256A"
intersectionHorizontalThin = "\u256B"
trisectionV = ["\u2563", "\u2560"]
trisectionVThin = ["\u2562", "\u255F"]
trisectionH = ["\u2569", "\u2566"]
trisectionHThin = ["\u2567", "\u2564"]
cornerTopLeft = "\u2554"
cornerTopRight = "\u2557"
cornerBotLeft = "\u255A"
cornerBotRight = "\u255D"

width = 4 * 9 + 1
height = 2 * 9 + 1

def init():
	array = Matrix(width, height)
	for x in range(4):
		for y in range(9):
			array.set(x * 4 * 3, y * 2 + 1, vertical)
			for i in range(3):
				array.set(y * 4 + 1 + i, x * 2 * 3, horizontal)
	for x in range(0, 3):
		for y in range(0, 9):
			for i in range(1, 3):
				array.set(x * 4 * 3 + i * 4, y * 2 + 1, verticalThin)
				for b in range(0, 3):
					array.set(y * 4 + 1 + b, x * 2 * 3 + i * 2, horizontalThin)
	for y in range(1, 3):
		for x in range(1, 3):
			array.set(x * 4 * 3, y * 2 * 3, intersection)
	for y in range(3):
		for x in range(3):
			for i in range(1, 3):
				for j in range(1, 3):
					array.set(x * 4 * 3 + i * 4, y * 2 * 3 + j * 2, intersectionThin)
	for y in range(1, 3):
		for x in range(0, 3):
			for i in range(1, 3):
				array.set(x * 4 * 3 + i * 4, y * 2 * 3, intersectionVerticalThin)
				array.set(y * 4 * 3, x * 2 * 3 + i * 2, intersectionHorizontalThin)
	for y in range(1, 3):
		array.set(4 * 9,      y * 2 * 3, trisectionV[0])
		array.set(0,          y * 2 * 3, trisectionV[1])
		array.set(y * 4 * 3,  2 * 9,     trisectionH[0])
		array.set(y * 4 * 3,  0,         trisectionH[1])

	for y in range(0, 3):
		for x in range(1, 3):
			array.set(4 * 9,      			y * 2 * 3 + x * 2, 	trisectionVThin[0])
			array.set(0,          			y * 2 * 3 + x * 2, 	trisectionVThin[1])
			array.set(y * 4 * 3 + x * 4,  	2 * 9,     			trisectionHThin[0])
			array.set(y * 4 * 3 + x * 4,  	0,         			trisectionHThin[1])

	for y in range(9):
		for x in range(9 * 2):
			array.set(x * 2 + 1, y * 2 + 1, ' ')


	array.set(0, 0, cornerTopLeft)
	array.set(0, 2 * 9, cornerBotLeft)
	array.set(4 * 9, 0, cornerTopRight)
	array.set(4 * 9, 2 * 9, cornerBotRight)

	sys.stdout.write(array.toString())
	#strings = array.toString().split('\n')
	#for s in strings:
	#	cursor.writeStringToCursorPos(s)
	#	cursor.move_down()
	
	cursor.move_up(height - 1)
	cursor.move_left(width - 1)
	cursor.reset()

def show(sudoku):
	goto(0, 0)
	for y in range(9):
		for x in range(9):
			setValue(x, y, sudoku.get(x, y))
	goto(0, 0)
	
def setValue(x, y, value):
	goto(x, y)
	cursor.writeToCursorPos(value if value != 0 else ' ')

def goto(x, y):
	cursor.goto(x * 4 + 2, y * 2 + 1)

def end():
	cursor.goto(0, height + 3)
