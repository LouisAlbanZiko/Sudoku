
class Matrix:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = [[0 for i in range(width)] for c in range(height)]

	def set(self, x, y, value):
		self.data[y][x] = value

	def get(self, x, y):
		return self.data[y][x]

	def toString(self):
		l = []
		for array in self.data:
			l.append("".join(str(element) for element in array))
		return "\n".join(l)