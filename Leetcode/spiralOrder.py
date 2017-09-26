def spiral_order(matrix):
	"""
		type: matrix: List[[int]]
		rtype: List[int]
	"""

	if not matrix:
		return matrix

	top, left = 0, 0
	bottom, right = len(matrix), len(matrix[0])
	result = []

	while top < bottom and left < right:
		# get all values in top row
		for t_num in range(left, right):
			result.append(matrix[top][t_num])
		top += 1

		# get all values in rightmost column
		for r_row in range(top, bottom):
			result.append(matrix[r_row][right - 1])
		right -= 1

		if (top < bottom):
			# get all values in bottom row
			for b_num in range(right - 1, left - 1, -1):
				result.append(matrix[bottom - 1][b_num])
			bottom -= 1

		if (left < right):
			# get all values in leftmost column
			for l_row in range(bottom - 1, top - 1, -1):
				result.append(matrix[l_row][left])
			left += 1

	return result