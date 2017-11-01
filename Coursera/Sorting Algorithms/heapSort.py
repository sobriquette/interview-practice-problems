# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify_max(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap
		# Heapify the root.
		heapify_max(arr, n, largest)

def heapify_min(arr, n, i):
	smallest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[l] < arr[i]:
		smallest = l
	if r < n and arr[r] < arr[smallest]:
		smallest = r

	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		heapify_min(arr, n, smallest)

# The main function to sort an array of given size
def heapSort_max(arr, n):
	# Build a maxheap.
	for i in range(n - 1, -1, -1):
		heapify_max(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify_max(arr, i, 0)

def heapSort_min(arr, n):
	for i in range(n):
		heapify_min(arr, n, i)

	for i in range(n):
		arr[i], arr[0] = arr[0], arr[i]
		heapify_min(arr, i, 0)

# Driver code to test above
arr = [5, 3, 8, 10, 12, 2, 1, 11, 13]
n = len(arr)
heapSort_min(arr, n)
print ("Sorted array is")
print(arr)
# This code is contributed by Mohit Kumra
