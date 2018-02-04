class SolutionDP:
	def num_paths_to_sq(self, i, j, memo):
		if i < 0 or j < 0:
			return 0
		elif i < j:
			return 0
		elif i == 0 and j == 0:
			return 1
		elif memo[i][j] != -1:
			return memo[i][j]
		else:
			memo[i][j] = self.num_paths_to_sq(i, j - 1, memo) + self.num_paths_to_sq(i - 1, j, memo)

		print("i: {}, j: {}, val: {}".format(i, j, memo[i][j]))
		return memo[i][j]

	def num_of_paths_to_dest(self, n):
		memo = [[-1 for _ in range(n)] for _ in range(n)]
		
		return self.num_paths_to_sq(n - 1, n - 1, memo)

class SolutionIter:
	def num_of_paths_to_dest(self, n):
		if n == 1:
			return 1

		last_row = [1 for _ in range(n)]

		curr_row = [0 for _ in range(n)]
		
		for j in range(1, n):
			for i in range(1, n):
				if i == j:
					curr_row[i] = last_row[i]
				else:
					curr_row[i] = curr_row[i - 1] + last_row[i]
				print("cr: {} | i: {} | j: {}".format(curr_row, i, j))
			last_row = curr_row
			print("lr: ", last_row)

		return curr_row[n - 1]

s = SolutionIter()
s.num_of_paths_to_dest(5)