def quicksort(arr, low, high):
	"""
		Recursive implementation of quicksort
		type: list
		rtype: list

		runtime: O(n^2) worst case b/c always picking last element
		space: O(1)
	"""

	def partition():
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

	while low < high:
		pi = partition()

		if (pi - low) < (high - pi):
			quicksort(arr, low, (pi - 1))
			low = pi + 1
		else:
			quicksort(arr, (pi + 1), high)
			high = pi - 1

	return arr

if __name__=="__main__":
	while True:
		response = input("enter a list of integers: ")

		if response == 'q':
			break

		arr = list(map(int, response.split()))
		print(quicksort(arr, 0, len(arr) - 1))