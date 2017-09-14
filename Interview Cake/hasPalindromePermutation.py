import collections
def hasPalindromePermutation(s):
	letters = collections.Counter(s)
	if len(s) % 2 == 0:
		return sum(map(lambda c: abs(c), letters.values())) == 0
	else:
		return sum(map(lambda c: abs(c), letters.values())) == 1

def has_palidnrome_permuation(s):
	unpaired_chars = set()

	for c in s:
		if c in unpaired_chars:
			unpaired_chars.remove(c)
		else:
			unpaired_chars.add(c)

	return len(unpaired_chars) <= 1