def count_ways_util(n, m):
	if n <= 1:
		return n
	res = 0
	step = 1
	while step <= m and step <= n:
		res += count_ways_util(n - step, m)
		step += 1

	return res

def count_ways(n, m):
	return count_ways_util(n + 1, m)

def count_ways_memoized(n, m):
	res = [0 for _ in range(n)]
	res[0], res[1] = 1, 1

	for n_i in range(2, n):
		step = 1
		while step <= m and step <= n:
			res[n_i] += res[n_i - step]
			step += 1
			
	return res[n - 1]


print(count_ways_memoized(5, 4))