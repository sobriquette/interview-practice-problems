def saddlepoints(m):
	if m == [] or len(m) <= 0:
		return "No saddle point"

	saddlepoints = []

	for i in range(len(m)):
		row_min = m[i][0]
		col_ind = 0

		# get current minimum of ith row
		# get column index of current min
		for j, num in enumerate(m[i]):
			if row_min > num:
				row_min = num
				col_ind = j

		# check if current min of ith row
		# is also max element of column
		colMax = -float('inf')
		for k, num in enumerate(m):
			if m[k][col_ind] > colMax:
				colMax = m[k][col_ind]
		
		if colMax == row_min:
			saddlepoints.append(row_min)

	return saddlepoints

if __name__=="__main__":
	m = [[1, 2, 3, -1],
		 [4, 5, 6, -10],
		 [7, 8, 9, -5]]

	print(saddlepoints(m))

