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