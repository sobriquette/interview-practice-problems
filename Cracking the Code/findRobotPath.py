class Point:
	def __init__(self, row, col):
		self.row = row
		self.col = col

def get_path(grid):
	if not grid:
		return None

	path = []
	off_limits = set()

	if is_path(grid, len(grid) - 1, len(grid[0] - 1, path, off_limits)):
		return path

	return None

def is_path(grid, row, col, path, off_limits):
	if row < 0 or col < 0 or not grid[row][col]:
		return False

	new_point = Point(row, col)
	
	if new_point in off_limits:
		return False	

	is_at_origin = (row == 0) and (col == 0)

	if is_at_origin or is_path(grid, row, col - 1, path, off_limits) or \
	   is_path(grid, row - 1, col, path, off_limits):
		path.append(new_point)
		return True

	off_limits.add(new_point)
	return False
