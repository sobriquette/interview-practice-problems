def mark_cavities(arr):
	num_rows = len(arr)
	num_cols = len(arr[0])
	for i in range(1, num_rows - 1):
		tmp = ''
		for j in range(1, num_cols - 1):
			if is_cavity(arr, i, j):
				tmp += 'X'
			else:
				tmp += arr[i][j]

		arr[i] = arr[i][0] + tmp + arr[i][num_cols - 1]

	return arr

def is_cavity(arr, i, j):
	potential_cavity = arr[i][j]
	top = arr[i - 1][j]
	left = arr[i][j + 1]
	bottom = arr[i + 1][j]
	right = arr[i][j - 1]

	if already_marked(top) or already_marked(left) or \
		already_marked(bottom) or already_marked(right):
		return False
	else:
		return potential_cavity > top and potential_cavity > left and \
				potential_cavity > bottom and potential_cavity > right

def already_marked(val):
	return val == 'X'

print(mark_cavities(['9999', '1912', '9999', '1234']))