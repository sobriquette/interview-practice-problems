def get_products_of_all_ints_except_at_index(nums):
	length = len(nums)

	if length < 2:
		raise IndexError('need at least 2 numbers to make a product')

	prods = [1] * length
	p_forward, p_backward = 1, 1

	# calculate products going forward
	for i in range(1, length):
		p_forward *= nums[i - 1]
		prods[i] = p_forward

	# calculate products going backward
	for i in range(length - 1, -1, -1):
		p_backward *= nums[i]
		prods[i - 1] *= p_backward

	return prods

def get_products_of_all_ints_solution(nums):
	if len(nums) < 2:
		raise IndexError('need at least 2 numbers to make a product')

	products = [None] * len(nums)
	
	# go forward
	product_so_far = 1
	i = 0
	while i < len(nums):
		products[i] = product_so_far
		product_so_far *= nums[i]
		i += 1

	# go backward
	product_so_far = 1
	i = len(nums)
	while i >= 0:
		products[i] *= product_so_far
		product_so_far *= nums[i]
		i -= 1

	return products