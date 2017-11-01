def bubble_sort_iterative(arr):
	"""
		Iterative implementation of bubble sort
		type: list
		rtype: list

		runtime: O(N^2)
		space: O(1)
	"""
	swaps = 0

	for i in range(len(arr) - 1):
		print("arr {} at i = {}".format(arr, i))
		for j in range(i, len(arr)):
			if arr[j] < arr[i]:
				arr[i], arr[j] = arr[j], arr[i]
				swaps += 1
			print("arr {} at i = {} and j = {}".format(arr, i, j))

		# if there are no swaps for a whole pass
		# we can return early since it is already sorted
		if swaps > 0:
			swaps = 0 
		else:
			return arr

	return arr

def bubble_sort_recursive(arr, n):
	"""
		Recursive implementation of bubble sort
		type: list
		rtype: list

		runtime: O(N^2)
		space: O(1)
	"""
	if n == 1:
		return

	for i in range(n - 1):
		if arr[i] > arr[i + 1]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]

	bubble_sort_recursive(arr, n - 1)

	return arr


if __name__=="__main__":
	while True:
		response = input("enter an array of integers to sort: ")
		if response == "q":
			break

		arr = list(map(int, response.split()))
		print(bubble_sort_iterative(arr))
		# print(bubble_sort_recursive(arr, len(arr)) == bubble_sort_iterative(arr))

