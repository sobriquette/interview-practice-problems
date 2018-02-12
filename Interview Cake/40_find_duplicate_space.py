# prev attempt
def findDuplicateNumber(nums):
	n = max(nums)
	s_max = sum(n)
	s_nums = sum(nums)

	return s_nums - s_max

# solution
def find_duplicate_spaceEd(arr):
	floor = 1
	ceiling = len(arr) - 1

	while floor < ceiling:
		mid = floor + (ceiling - floor) // 2
		l_floor, l_ceil = floor, mid
		h_floor, h_ceil = mid + 1, ceiling

		cnt_in_lower = 0
		for n in arr:
			if l_floor <= n <= l_ceil:
				cnt_in_lower += 1
		
		if cnt_in_lower > (l_ceil - l_floor) + 1:
			floor = l_floor
			ceiling = l_ceil
		else:
			floor = h_floor
			ceiling = h_ceil

		print("floor: {} | ceil: {}".format(floor, ceiling))

	return floor

print(find_duplicate_spaceEd([7, 3, 4, 1, 5, 8, 9, 2, 6, 10, 2]))