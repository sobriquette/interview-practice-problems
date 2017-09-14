def merge(left, right):
	full = []
	while left and right:
		if left[0] < right[0]:
			full.append(left[0])
			left.remove(left[0])
		else:
			full.append(right[0])
			right.remove(right[0])

	if len(left) == 0:
		full += right
	else:
		full += left

	return full

def mergeSort(arr):
	if len(arr) <= 1:
		return arr
	else:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]

		return merge(left, right)

def sortArray(arr):
	sortedArray = mergeSort(arr)
	# check if all are unique
	for i in range(len(sortedArray) - 1):
		if arr[i] == arr[i + 1]:
			return False