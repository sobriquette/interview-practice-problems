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