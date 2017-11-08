def change_top_down(amount_left, denominations, current_index=0):
	if amount_left == 0:
		return 1
	if amount_left < 0:
		return 0
	if current_index == len(denominations):
		return 0

	current_coin = denominations[current_index]
	ways = 0
	while amount_left >= 0:
		ways += change_top_down(amount_left, denominations, current_index + 1)
		amount_left -= current_coin

	return ways

def change_top_down_memoized(amount_left, denominations, current_index=0, memo={}):
	memo_key = str((amount_left, current_index))

	if memo_key in memo:
		return memo[memo_key]

	if amount_left == 0:
		return 1
	if amount_left < 0:
		return 0
	if current_index == len(denominations):
		return 0

	current_coin = denominations[current_index]
	ways = 0
	while amount_left >= 0:
		ways += change_top_down_memoized(amount_left, denominations, current_index + 1, memo)
		amount_left -= current_coin

	memo[memo_key] = ways
	return ways

def change_bottom_up(amount, denominations):
	ways = [0] * (amount + 1)
	ways[0] = 1

	for coin in denominations:
		for amount_left in range(coin, amount + 1):
			ways[amount_left] += ways[amount_left - coin]

	return ways[amount]

print(change_top_down(4, [1,2,3,4], 0))