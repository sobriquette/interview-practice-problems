# fibonacci recursively
def fibRecursive(n):
	if n == 0:
		return 0
	elif 0 < n <= 2:
		return 1
	else:
		return fibRecursive(n - 2) + fibRecursive(n - 1)

# fibonacci recursively with memoization
def fibRecursiveMemo(memo, n):
	memo = {}

	if n == 0:
		return 0
	elif 0 < n <= 2:
		return 1
	elif n in memo:
		return n
	else:
		memo[n] = fibRecursiveMemo(memo, n - 2) + fibRecursiveMemo(memo, n - 1)
	
	return memo[n]

# fibonacci iteratively
def fibIterative(n):
	if n == 0:
		return 0
	elif n in [0, 1]:
		return n
	else:
		prev, next = 0, 1

		for i in range(n - 1):
			prev, next = next, prev + next

		return next