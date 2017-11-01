def count_ways_util(n, m):
	if n <= 1:
		return n
	res = 0
	i = 1
	while i <= m and i <= n:
		print("res: {} | i: {} | m: {} | n: {}".format(res, i , m, n))
		res = res + count_ways_util(n - i, m)
		i += 1

	return res

def count_ways(n, m):
	return count_ways_util(n + 1, m)

def count_ways_memoized(n, m):
	res = [0 for _ in range(n)]
	res[0], res[1] = 1, 1

	for i in range(2, n):
		j = 1
		while j <= m and j <= n:
			res[i] = res[i] + res[i - j]
			j += 1
			print("res: {}, j: {}, i: {}".format(res, j, i))

	return res[n - 1]


print(count_ways_memoized(5, 4))