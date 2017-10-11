def merge(arr, low, mid, high):
	"""
		Implementation of merge function within mergesort
	"""

	n1 = mid - low + 1
	n2 = high - mid

	left = [None] * n1
	right = [None] * n2

	for i in range(n1):
		left[i] = arr[low + i]

	for j in range(n2):
		right[j] = arr[mid + low + j]

	i, j, k = 0, 0, low

	while i < n1 and j < n2:
		if left[i] <= right[j]
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1

		k += 1

	while i < n1:
		arr[k] = left[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = right[j]
		j += 1
		k += 1

def merge_sort_recursive(arr, low, high):
	"""
		Recursive implementation of mergesort
		type: list
		rtype: list

		runtime: O(nlogn)
		space: O(n) for temp arrays in merge()
	"""
	if low < high:
		mid = (low + high) // 2
		merge_sort(arr, low, mid)
		merge_sort(arr, mid + 1, high)
		merge(arr, low, mid, high)

def merge_sort_iterative(arr, n):
	"""
		Iterative implementation of mergesort
		type: list
		rtype: list

		runtime: O(nlogn)
		space: O(n) for temp arrays in merge()
	"""

	# Merges subarrays in bottom up manner
	# First merge subarrays of size 1 to create sorted subarrays of size 2,
	# then merge subarrays of size 2 to subarrays of size 4...etc.
	for size in range(1, n-1, size * 2):
		# Pick starting point of different subarrays of current size
		for left in range(0, n-1, left + (size * 2)):
			# Find ending point of left subarray
			# mid + 1 is starting point of right
			mid = left + size - 1
			right = min((left + 2*size - 1), n-1)
			# merge subarrays
			merge(arr, left, mid, right)
