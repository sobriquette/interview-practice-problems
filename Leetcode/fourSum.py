class Solution:
	def four_sum(self, nums, target):
		if not nums or len(nums) < 4:
			return []

		nums_sort = sorted(nums)

		# we can exit early if these cases are true
		if nums_sort[0] > target or nums_sort[len(nums_sort) - 1] < target:
			return []

		results = []
		start = len(nums_sort) // 2
		inner_left, inner_right = start - 1, start

		while inner_left >= 1 and inner_right < len(nums_sort) - 1:
			outer_left = inner_left + 1
			outer_right = inner_right + 1

			while outer_left >= 0 and outer_right < len(nums_sort):
				s = nums_sort[inner_left] + nums_sort[inner_right] + \
					nums_sort[outer_left] + nums_sort[outer_right]

				if s < target:
					outer_right += 1
				elif s > target:
					outer_left -= 1
				else:
					results.append( \
						[nums_sort[inner_left], nums_sort[inner_right], \
						 nums_sort[outer_left], nums_sort[outer_right]])

					outer_right += 1
					outer_left -= 1
			
			inner_left -= 1
			inner_right += 1

		return results

print(Solution().four_sum([1, 0, -1, 0, -2, 2], 0))

