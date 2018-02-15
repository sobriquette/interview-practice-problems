# prev attempt
def findDuplicateNumber(nums):
	n = max(nums)
	s_max = sum(n)
	s_nums = sum(nums)

	return s_nums - s_max