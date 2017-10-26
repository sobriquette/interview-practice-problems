def edit_distance_dp(str1, str2, m, n):
	"""
		Compute minimum edit distance b/n two strings
		Operations are insert, remove, replace

		Runtime: O(n * m)
		Space: O(n * m)
	"""
	# m rows for each char in str1
	# n columns for each char in str2
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

	for i in range(m + 1):
		for j in range(n + 1):
			# if len(str1) is 0, min distance is len(str2)
			if i == 0:
				dp[i][j] = j
			# if len(str2) is 0, min distance is len(str1)
			elif j == 0:
				dp[i][j] = i
			# if last chars of str1 and str2 are the same,
			# we can ignore it and recur on str1 and str2
			elif str1[i - 1] == str2[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
			# if last chars of str1 and str2 are diff,
			# take min of all possibilities
			# (insert, remove, replace)
				dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

	return dp[m][n]

def edit_distance_dp_2(str1, str2):
	"""
		Improve auxiliary space usage from edit_distance_dp function

		Runtime: O(m * n)
		Space: O(min(m, n))
	"""

	# swap strings so str1 is the longer one
	m, n = len(str1), len(str2)
	if m < n:
		str1, str2 = str2, str1
		m, n = n, m

	prev_distances = [0 for _ in range(n + 1)]
	curr_distances = [0 for _ in range(n + 1)]

	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0:
				curr_distances[j] = j
			elif j == 0:
				curr_distances[j] = i
			elif str1[i - 1] == str2[j - 1]:
				curr_distances[j] = prev_distances[j - 1]
			else:
				curr_distances[j] = 1 + min(curr_distances[j - 1], prev_distances[j], prev_distances[j - 1])

		prev_distances = curr_distances
		curr_distances = [0 for _ in range(n + 1)]

	return prev_distances[n]

if __name__=="__main__":
	str1 = input("string #1: ")
	str2 = input("string #2: ")

	print(edit_distance_dp(str1, str2, len(str1), len(str2)) == edit_distance_dp_2(str1, str2))
	print(edit_distance_dp_2(str1, str2))