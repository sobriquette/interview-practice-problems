class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class Line:
	def __init__(self, p1, p2):
		self.start = p1
		self.end = p2
		self.slope = (p2.y - p1.y) / (p2.x - p1.x)
		self.y_intercept = (p2.y - (self.slope * p2.x))

def swap(p1, p2):
	p1.x, p2.x = p2.x, p1.x
	p1.y, p2.y = p2.y, p1.y

def is_coord_between(start, middle, end):
	if start > end:
		return end <= middle <= start
	else:
		return start <= middle <= end

def is_between(start, middle, end):
	return is_coord_between(start.x, middle.x, end.x) and \
			is_coord_between(start.y, middle.y, end.y)

def compute_intersection(start1, end1, start2, end2):
	if start1.x > end1.x:
		swap(start1, end1)
	if start2.x > end2.x:
		swap(start2, end2)
	if start1.x > start2.x:
		swap(start1, start2)
		swap(end1, end2)

	line1 = Line(start1, end1)
	line2 = Line(start2, end2)

	if line1.slope == line2.slope:
		if line1.y_intercept == line2.y_intercept and \
			is_between(start1, start2, end1)
			return start2
		return None

	x = (line2.y_intercept - line1.y_intercept) / \
		(line1.slope - line2.slope)
	y = x * line1.slope + line1.y_intercept

	intersection = Point(x, y)

	if is_between(start1, intersection, end1) and \
		is_between(start2, intersection, end2):
		return intersection

	return None

