def spiral_copy(inputMatrix):
	output = []

	top = left = 0
	bottom = len(inputMatrix) - 1
	right = len(inputMatrix[0]) - 1

	while top <= bottom and left <= right:
		# get top row
		for i in range(left, right + 1):
			output.append(inputMatrix[top][i])
		top += 1

		# get right column
		for i in range(top, bottom + 1):
			output.append(inputMatrix[i][right])
		right -= 1


		if (top <= bottom):
			# get bottom row
			for i in range(right, left - 1, -1):
				output.append(inputMatrix[bottom][i])
			bottom -= 1


		if (left <= right):
			# get left column
			for i in range(bottom, top - 1, -1 ):
				output.append(inputMatrix[i][left])
			left += 1


	return output

inputMatrix = [[1,    2,   3,  4,    5],
				[6,    7,   8,  9,   10],
				[11,  12,  13,  14,  15],
				[16,  17,  18,  19,  20] ]
print(spiral_copy(inputMatrix))