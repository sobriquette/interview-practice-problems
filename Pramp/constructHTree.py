class Point:
	def __init__(self):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def update(self, new_x, new_y):
		self.x = new_x
		self.y = new_y


def drawHTree(x, y, starting_length, depth):
	# base case
	if depth == 0:
		return

	# create points of H-tree
	top_left = Point()
	bot_left = Point()
	top_right = Point()
	bot_right = Point()

	# update points of H-tree
	top_left.update(x - starting_length // 2 , y + starting_length // 2)
	bot_left.update(x - starting_length // 2 , y - starting_length // 2)
	top_right.update(x + starting_length // 2 , y + starting_length // 2)
	bot_right.update(x + starting_length // 2 , y - starting_length // 2)

	# x coordinates
	#l_x = x - starting_length // 2
	#r_x = x + starting_length // 2

	# y coordinates
	#t_y = y + starting_length // 2
	#b_y = y - starting_length // 2

	# draw 3 line segments of H-tree
	drawLine(l_x, b_y, l_x, t_y) 	# left side
	drawLine(l_x, y, r_x, y) 		# middle
	drawLine(r_x, b_y, r_x, t_y) 	# right side

	drawHTree(l_x, t_y, ( starting_length // (2**0.5) ), depth - 1) # top left H-tree
	drawHTree(l_x, b_y, ( starting_length // (2**0.5) ), depth - 1) # bottom left H-tree
	drawHTree(r_x, t_y, ( starting_length // (2**0.5) ), depth - 1) # top right H-tree
	drawHTree(r_x, b_y, ( starting_length // (2**0.5) ), depth - 1) # bottom right H-tree