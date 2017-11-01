# Find all unique paths on a grid from (0,0) to bottom right

class SolutionComb:
	from math import factorial
	def combinatorial(self, r, c):
		return factorial(r + c) / (factorial(c) * factorial(r - c))

class SolutionBT:
	def backtracking(self, r, c, m, n):
		if r == m and c == n:
			return 1
		if r > m or c > n:
			return 0

		return self.backtracking(r + 1, c, m, n) + self.backtracking(r, c + 1, m, n)

class SolutionBTMemo:
	def bt_util(self, r, c, m, n, memo):
		if r == m and c == n:
			return 1
		if r > m or c > n:
			return 0

		if memo[r + 1][c] == -1:
			memo[r + 1][c] = self.bt_util(r + 1, c, m, n, memo)
		if memo[r][c + 1] == -1:
			memo[r][c + 1] = self.bt_util(r, c + 1, m, n, memo)

		return memo[r + 1][c] + memo[r][c + 1]


	def backtrack_memoized(self, m, n):
		memo = [[-1 for _ in range(n)] for _ in range(m)]

		self.bt_util(1, 1, m, n, memo)

class SolutionBottomUp:
	def bottom_up(self, m, n):
		mat = [[-1 for _ in range(n + 2)] for _ in range(m + 2)]
		mat[m][n + 1] = 1

		for r in range(m, 1, -1):
			for c in range(n, 1, -1):
				mat[r][c] = mat[r + 1][c] + mat[r][c + 1]

		return mat[1][1]