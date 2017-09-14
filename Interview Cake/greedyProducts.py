def greedyProducts(arr):
	# check edge cases
	if len(arr) < 2:
		return False

	# create results list
	result = [1 for _ in range(len(arr))]
	
	# cache previous products calculated
	forward = backward = 1
	
	# create products going forward
	# skipping the first in results
	for i in range(1, len(arr)):
		result[i] = forward * arr[i - 1]
		forward = result[i]

	# go backwards and use already calculated products
	# skipping the last in results
	for j in range(len(arr) - 1, 0, -1):
		result[j - 1] = result[j - 1] * backward * arr[j]
		backward *= arr[j]

	return result

def greedyProductsSolution(arr):
	if len(arr) < 2:
		return False

	# create results list
	results = [None] * len(arr)

	# for each integer, find product of all integers before it
	# store total product so far each time
	forward = 1
	i = 0
	while i < len(arr):
		results[i] = forward
		forward *= arr[i]
		i += 1

	# for each integer, find product of all integers after it
	# each index in results already has product of all integers before it
	# now we store total product of all other integers
	backward = 1
	i = len(arr) - 1
	while i >= 0:
		results[i] *= backward
		backward *= arr[i]
		i -= 1

	return results

if __name__=="__main__":
	nums = [[1, 7, 3, 4], [1, 2, 6, 5, 9], [0, 0, 0], [], [14]]
	for i in range(len(nums)):
		print(greedyProducts(nums[i]))
		print(greedyProductsSolution(nums[i]))

# Runtime: O(2n)
# Space: O(n)