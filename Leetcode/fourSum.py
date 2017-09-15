class Solution:
	def four_sum(self, nums, target):
		results = []
		self.solve_n_sum(sorted(nums), target, 4, [], results)
		return results
	
	def solve_n_sum(self, nums, target, N, result, results):
		# early termination
		if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
			return
		if N == 2:
			left, right = 0, len(nums) - 1

			while left < right:
				total = nums[left] + nums[right]
				if total == target:
					results.append(result + [nums[left], nums[right]])
					left += 1

					# avoid duplicates
					while left < right and nums[left] == nums[left - 1]:
						left += 1

				elif total < target:
					left += 1
				else:
					right -= 1
		# reduce N until we reach the 2-sum problem
		else:
			for i in range(len(nums) - N + 1):
				if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
					self.solve_n_sum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)


print(Solution().four_sum([1, 0, -1, 0, -2, 2], 0))

