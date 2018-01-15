def recursive_levenshtein(s, t):
	if s == t:
		return 0

	return lev_util(s, t, len(s), len(t))

def lev_util(s, t, len_s, len_t):
	if len_s == 0:
		return len_t

	if len_t == 0:
		return len_s

	if s[len_s - 1] == t[len_t - 1]:
		return lev_util(s, t, len_s - 1, len_t - 1)

	return 1 + min( lev_util(s, t, len_s, len_t - 1), \
					lev_util(s, t, len_s - 1, len_t), \
					lev_util(s, t, len_s - 1, len_t - 1) )

def iterative_levenshtein(s, t):
	"""
	type: str str
	rtype: int

	For all i and j, dist[i, j] will hold the Levenshtein
	distance between the first i charactesr of s and 
	the first j characters of t.
	"""
	if len(s) < len(t):
		return iterative_levenshtein(t, s)

	if s == t:
		return 0
	elif len(t) == 0:
		return len(s)
	else:
		rows = len(s) + 1
		cols = len(t) + 1
		dist = [[0 for _ in range(cols)] for _ in range(rows)]

		for i in range(cols):
			dist[0][i] = i

		for i in range(1, rows):
			dist[i][0] = i

		for col in range(1, cols):
			for row in range(1, rows):
				if s[row - 1] == t[col - 1]:
					cost = 0
				else:
					cost = 1

				# deletion, insertion, substition
				dist[row][col] = min(dist[row -1][col] + 1, \
									 dist[row][col - 1] + 1, \
									 dist[row - 1][col - 1] + cost)

				if row > 0 and col > 0 and \
					s[row + 1] == t[col] and s[row] == t[col + 1]:
					d[row][col] = min(d[row][col], d[row - 1][col - 1] + cost)

		return dist[row][col]
