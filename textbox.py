import platform
if platform.system() == "Windows":
	import cursor_windows as cursor
else:
	import cursor
import board

# Simple textbox for showing messages to the user
class TextBox:
	def __init__(self, x, y, width = 10, height = 1):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		a = [[" " for i in range(self.width)] for i in range(self.height)]
		l = []
		for s in a:
			l.append("".join(s))
		self.clearString = "\n".join(l)

	def message(self, string):
		self.show(self.clearString)
		self.show(string)

	def show(self, string):
		x = cursor.x
		y = cursor.y
		strings = string.split("\n")
		cursor.goto(self.x, self.y)
		for s in strings:
			if len(s) > self.width:
				s = s[0:self.width - 1]
			cursor.writeStringToCursorPos(s)
			cursor.move_down()
		cursor.goto(x, y)