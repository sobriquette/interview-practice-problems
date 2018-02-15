class Solution:
	def binary_search(self, arr, target):
		start = 0
		end = len(arr) - 1
		
		while start <= end:
			mid = start + ((end - start) // 2)
			print("arr[mid]: ", arr[mid])
			if target == arr[mid]:
				return True
			elif target < arr[mid]:
				end = mid - 1
			else:
				start = mid + 1
			print("start: {}, end: {}".format(start, end))
		
		return False
		
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix or not matrix[0] or target is None:
			return False
		
		len_m = len(matrix)
		for r in matrix:
			if target == r[-1]:
				return True
			elif target < r[-1]:
				print("here: ", r)
				return self.binary_search(r, target)
		return False


if __name__=="__main__":
	arr = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
	target = -5
	print(Solution().searchMatrix(arr, target))