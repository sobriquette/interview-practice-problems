"""
Implementation for attempt #1: 01/18/2018
"""
def get_perms_util(s, idx):
	if idx == 0:
		return {s[idx]}

	perms = set()

	for p in get_perms_util(s, idx - 1):
		for i in range(len(p) + 1):
			perms.add(p[:i] + s[idx] + p[i:])

	return perms

def get_all_permutations(s):
	return get_perms_util(s, len(s) - 1)


print(get_all_permutations('abc'))

"""
Implementation for attempt #1: 08/07/2017
"""
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