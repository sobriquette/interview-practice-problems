# Find max profit from buying and selling 1 purchase of stock
def negProfit(nums):
	best_profit = -float("inf")
	for i in range(len(nums) -1):
		curr = nums[i + 1] - nums[i]
		if curr > best_profit:
			best_profit = curr

	return best_profit

def maxProfit(nums):
	if len(nums) < 2:
		return "You need at least 2 prices"
	if nums[0] == min(nums):
		profit = max(nums) - min(nums)
		return profit if profit > 0 else 0
	if nums[0] == max(nums) and nums[len(nums) - 1] == min(nums):
		return negProfit(nums)

	# O(2n)
	a_min, a_max = min(nums), max(nums)
	# O(2n)
	a_min_i, a_max_i = nums.index(a_min), nums.index(a_max)
	# O(4n)
	l_min, l_max = min(nums[:a_max_i]), max(nums[a_min_i:])
	# total so far: O(8n)
	
	left = a_max - l_min
	right = l_max - a_min
	return left if left > right else right

def greedyProfit(nums):
	if len(nums) < 2:
		return "You need at least 2 prices"

	max_profit = nums[1] - nums[0]
	curr_min = nums[0]

	for i in range(len(nums) - 1):
		if nums[i] < curr_min:
			curr_min = nums[i]
		curr_profit = nums[i + 1] - curr_min
		if curr_profit > max_profit:
			max_profit = curr_profit

	return max_profit

	# Runtime: O(n)
	# Space: O(1)

def greedyProfitSolution(nums):
	if len(nums) < 2:
		return "You need at least 2 prices"

	# set the max profit to the first difference
	max_profit = nums[1] - nums[0]
	# set the min price to be the first number seen
	min_price = nums[0]

	for time, curr_price in enumerate(nums):
		# skip the first index because we already bought
		# and we can't subtract it from itself
		# because we would be buy/selling at the same time
		if time == 0:
			continue

		curr_profit = curr_price - min_price
		max_profit = max(max_profit, curr_profit)
		min_price = min(min_price, curr_price)

	return max_profit


if __name__=="__main__":
	nums = [[16, 7, 3, 20, 2, 10, 8], [10, 7, 5, 8, 11, 9], [1, 2 , 78, 2, 5], [1, 1, 1, 1], [], [15, 14, 12, 9, 5, 3, 1]]
	for i in nums:
		#print(maxProfit(i))
		print(greedyProfit(i) == greedyProfitSolution(i))