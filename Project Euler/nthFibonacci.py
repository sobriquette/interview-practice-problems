# Print the nth number in the Fibonacci Sequence

# Approach 1: iterative, space optimized
def fibIterative(n):
	n1, n2 = 0, 1

	if n < 0:
		return "Input is incorrect"
	elif n == 1:
		return n1
	elif n == 2:
		return n2
	else:
		for i in range(2,n):
			n1, n2 = n2, n1 + n2

	return n2

# Runtime: O(n)
# Space: O(1)

# Approach 2: recursion
def fibRecursive(n):
	if n < 0:
		return "Input is incorrect"
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibRecursive(n - 2) + fibRecursive(n - 1)

# Runtime: O(2^n)
# Space: O(1) -- if considering call stack size, O(n)

# Approach 3: recursion w/ dynamic programming
def fibDynamic(n):
	fibs = [0, 1]
	if n < 0:
		return "Input is incorrect"
	elif n <= len(fibs):
		return fibs[n - 1]
	else:
		fib = fibDynamic(n - 1) + fibDynamic(n - 2)
		fibs.append(fib)
		return fib

# Runtime: O(n)
# Space: O(n) for storing calculated fibonacci numbers

if __name__=="__main__":
	n = 9
	print(fibIterative(n))
	print(fibRecursive(n))
	print(fibDynamic(n))