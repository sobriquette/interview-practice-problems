def partition(arr, low, high):
	"""
		Partitioning using last element
	"""
	pivot = arr[high]
	# index of smaller element
	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = pivot, arr[i + 1] 

	return (i + 1)

def quicksort_recursive(arr, low, high):
	"""
		Recursive implementation of quicksort
		type: list
		rtype: list

		runtime: O(n^2) worst case b/c always picking last element
		space: O(n)
	"""

	while low < high:
		pi = partition(arr, low, high)

		if (pi - low) < (high - pi):
			quicksort_recursive(arr, low, (pi - 1))
			low = pi + 1
		else:
			quicksort_recursive(arr, (pi + 1), high)
			high = pi - 1

	return arr

def quicksort_iterative(arr, low, high):
	"""
		Iterative implementation of quicksort
		type: list
		rtype: list

		runtime: O(n^2)
		space: O(n)
	"""

	stack = [0] * (high - low + 1)
	stack.append(low)
	stack.append(high)

	while len(stack) >= 2:
		high = stack.pop()
		low = stack.pop()

		pi = partition(arr, low, high)

		# push left side onto stack if there are elements
		# on left side of pivot
		if pi - 1 > low:
			stack.append(low)
			stack.append(pi - 1)

		# push right side onto stack if there are elements
		# on right side of pivot
		if pi + 1 < high:
			stack.append(pi + 1)
			stack.append(high)

	return arr

if __name__=="__main__":
	while True:
		response = input("enter a list of integers: ")

		if response == 'q':
			break

		arr = list(map(int, response.split()))
		print(quicksort_recursive(arr, 0, len(arr) - 1) == \
			  quicksort_iterative(arr, 0, len(arr) - 1))

