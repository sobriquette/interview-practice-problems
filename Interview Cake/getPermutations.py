def get_permuations(string):
	if len(string) <= 1:
		return set([string])

	all_chars_except_last = string[::-1]
	last_char = string[-1]

	permuations_all_except_last = get_permutations(all_chars_except_last)

	permutations = set()
	for p in permutations_all_except_last:
		for i in range(len(all_chars_except_last) + 1):
			permutation = p[:i] + last_char + p[i:]
			permutations.add(permutation)

	return permutations