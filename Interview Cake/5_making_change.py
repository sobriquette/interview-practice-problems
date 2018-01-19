"""
Implementation on attempt #3: 11/06/2017
"""
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


"""
Implementation on attempt #2: 07/24/2017
"""
class Change():
	def __init__(self, n):
		self.coins = [1,2,3]
		self.ways = [0] * (n + 1)
		self.amount = n	

	def countWaysDP(self):
		if self.amount < 0:
			return 0
		elif self.amount == 0:
			return 1
		else:
			self.ways[0] = 1

			for c in self.coins:
				for curr_amount in range(c, self.amount + 1):
					leftover = curr_amount - c
					self.ways[curr_amount] += self.ways[leftover]

			return self.ways[self.amount]

if __name__ == "__main__":
	n = int(input("enter the number: "))

	print(Change(n).countWaysDP())


"""
Implementation on attempt #1: 03/30/2017
"""

# For a certain amount (in cents), and given a list of coin denominations (cents),
# output the number of ways to make the amount with those denominations

class Change:
	def __init__(self):
		self.combos = {}

	def number_of_ways(self, remaining, denominations, i=0):
		# check if we've seen this combination before
		combo_key = str((remaining, i))
		
		if combo_key in self.combos:
			return self.combos[combo_key]

		# this combination gives us the amount
		if remaining == 0: return 1
		# this exceeds the amount we need
		if remaining < 0: return 0
		# out of coins to use
		if i == len(denominations): return 0
		# current coin
		curr_d = denominations[i]

		ways = 0
		while remaining >= 0:
			ways += self.number_of_ways(remaining, denominations, i + 1)
			remaining -= curr_d

		# save to our combos dict for memoization
		self.combos[combo_key] = ways

		return ways

	def ways_bottom_up(self, amount, denominations):
		ways_of_doing_n_cents = [0] * (amount + 1)
		ways_of_doing_n_cents[0] = 1

		for coin in denominations:
			for higher_amount in range(coin, amount + 1):
				remainder = higher_amount - coin
				ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[remainder]

		print(ways_of_doing_n_cents[amount])
		return ways_of_doing_n_cents[amount]


# Change().number_of_ways(4, [1, 2, 3])
Change().ways_bottom_up(4, [1, 2, 3])