# cursor implementation for unix systems

import sys

x = 0
y = 0

def reset():
	global x
	global y
	x = 0
	y = 0

def move_up(count=1):
	global y
	y-=count
	sys.stdout.write("\u001b[{0}A".format(str(count)))
	sys.stdout.flush()

def move_down(count=1):
	global y
	y+=count
	sys.stdout.write("\u001b[{0}B".format(str(count)))
	sys.stdout.flush()

def move_right(count=1):
	global x
	x+=count
	sys.stdout.write("\u001b[{0}C".format(str(count)))
	sys.stdout.flush()

def move_left(count=1):
	global x
	x-=count
	sys.stdout.write("\u001b[{0}D".format(str(count)))
	sys.stdout.flush()

def writeToCursorPos(value):
	sys.stdout.write(str(value))
	sys.stdout.write("\u001b[1D")
	sys.stdout.flush()

def writeStringToCursorPos(string):
	sys.stdout.write(string)
	sys.stdout.write("\u001b[{0}D".format(len(string)))
	sys.stdout.flush()

def goto(xPos, yPos):
	xMove = xPos - x
	yMove = yPos - y
	if yMove < 0:
		move_up(-yMove)
	elif yMove > 0:
		move_down(yMove)
	if xMove < 0:
		move_left(-xMove)
	elif xMove > 0:
		move_right(xMove)