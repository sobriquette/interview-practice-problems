###
# Boundary Cases:
# Max time to sort if elements are in reverse order
# Min time to sort O(n) if elements are already sorted
###
# Uses:
# When number of elements is small, or when input array is almost sorted
###

def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped

def insertion_sort_iterative(arr):
	"""
		Iterative implementation of insertion sort
		type: list
		rtype: list

		runtime: O(n^2)
		space: O(1)
	"""
	for i in range(1, len(arr)):
		curr = arr[i]
		pos = i

		while pos > 0 and arr[pos - 1] > curr:
			arr[pos] = arr[pos - 1]
			pos -= 1

		arr[pos] = curr

	return arr

def insertion_sort_recursive(arr, n):
	"""
		Recursive implementation of insertion sort
		type: list
		rtype: list

		runtime: O(n^2)
		space: O(1)
	"""
	if n <= 1:
		return

	insertion_sort_recursive(arr, n - 1)

	last = arr[n - 1]
	j = n - 2

	while j >= 0 and arr[j] > last:
		arr[j + 1] = arr[j]
		j -= 1

	arr[j + 1] = last

	return arr

def binary_insertion_sort(arr, n):
	def binary_search(val, low, high):
		if high <= low:
			if val > arr[low]:
				return low + 1
			else:
				return low

		mid = (low + high) // 2

		if val == arr[mid]:
			return mid + 1

		if val > arr[mid]:
			return binary_search(val, mid + 1, high)
		else:
			return binary_search(val, low, mid - 1)
	
	for i in range(1, n):
		j = i - 1
		curr = arr[i]

		# find index for insertion of curr
		insert_idx = binary_search(curr, 0, j)

		# move all elements over for insertion
		while j >= insert_idx:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = curr

	return arr


if __name__=="__main__":
	from timeit import Timer
	import numpy.random as nprnd

	# while True:
	# 	response = input("enter an array of integers to sort: ")
	# 	if response == "q":
	# 		break

	# 	arr = list(map(int, response.split()))
	# 	print(insertion_sort_recursive(arr, len(arr)) == insertion_sort_iterative(arr))
	# 	print(binary_insertion_sort(arr, len(arr)))

	arr = nprnd.randint(1000, size=100000)

	wrap_iter = wrapper(insertion_sort_iterative, arr)
	wrap_recur = wrapper(insertion_sort_recursive, arr, len(arr))
	wrap_bin_s = wrapper(binary_insertion_sort, arr, len(arr))

	t1 = Timer("insertion_sort_iterative", "from __main__ import insertion_sort_iterative")
	t2 = Timer("insertion_sort_recursive", "from __main__ import insertion_sort_recursive")
	t3 = Timer("binary_insertion_sort", "from __main__ import binary_insertion_sort")

	print(t1.timeit())
	print(t2.timeit())
	print(t3.timeit())

