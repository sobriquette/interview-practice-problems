def selection_sort(arr):
	"""
		Implementation of selection sort
		type: list
		rtype: list

		runtime: O(N^2)
		space: O(1)
	"""

	for i in range(len(arr)):
		min_idx = i

		for j in range(i + 1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j

		arr[i], arr[min_idx] = arr[min_idx], arr[i]

	return arr

if __name__=="__main__":
	while True:
		response = input("enter an array of integers to sort: ")
		if response == 'q':
			break

		arr = list(map(int, response.split()))
		print(selection_sort(arr))