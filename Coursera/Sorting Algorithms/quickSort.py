class Solution1():
	def quicksort(arr, start, end):
		if start < end:
			# partition list
			pivot = partition(arr, start, end)

			# sort both halves of list
			quicksort(arr, start, pivot - 1)
			quicksort(arr, pivot + 1, end)

		return arr

	def partition(arr, start, end):
		pivot = arr[start]
		left = start + 1
		right = end
		done = False

		while not done:
			# make sure all to left of pivot are smaller
			while left <= right and arr[left] <= pivot:
				left += 1
			# make sure all to right of pivot are larger
			while arr[right] >= pivot and right >= left:
				right += 1
			# when counters cross, then elements are on right side
			if right < left:
				done = True
			else:
				# swap because elem on left or right is on wrong side
				arr[left], arr[right] = arr[right], arr[left]

		# swap first index with last
		arr[start], arr[right] = arr[right], arr[start]
		return right

class Solution2():
	# reading in file input
	with open('QuickSort.txt') as f:
		inputList = f.readlines()

	# converting string elements of inputList into ints
	inputList = map(int, inputList)

	# initialize count
	count = 0

	def quickSort(inputList, length):
		if len(inputList) == 1:
			return inputList
		pivot = inputList[left]
		Partition(inputList, left, right)
		# recursively sort 1st part
		# quickSort(Partition(inputList, left, right), left + 1 -> i - 1)
		# recursively sort 2nd part
		# quickSort(Partition(inputList, left, right), i -> j - 1)

	def Partition(inputList, left, right):
	# partitioning
		pivot = inputList[left]
		i = left + 1
		for j = left + 1 in range(right):
			if inputList[j] < orgPivot:
				temp = inputList[i]
				inputList[i] = inputList[j]
				inputList[j] = temp
				i += 1

		#put pivot in its correct position within array
		temp = inputList[i - 1]
		inputList[i - 1] = pivot
		pivot = temp

		return inputList