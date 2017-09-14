def highest_product_of_three(nums):
	if len(nums) < 3:
		raise Exception('can\'t have less than 3 items')

	low = min(nums[0], nums[1])
	high = max(nums[0], nums[1])
	lowest_two = low * high
	highest_two = low * high
	highest_three = highest_two * nums[2]

	for i, n in enumerate(nums):
		if i < 2:
			continue
		highest_three = max(highest_three, n * highest_two, n * lowest_two)
		highest_two = max(highest_two, high * n, low * n)
		lowest_two = min(lowest_two, low * n, high * n)
		high = max(high, n)
		low = min(low, n)

	return highest_three
