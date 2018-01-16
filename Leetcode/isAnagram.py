from Collections import Counter
def is_anagram_w_dict(w1, w2):
	"""
	Store counts of letters in dictionaries for word1 and word2.
	If all counts of letters match, the words are anagrams.

	type: str, str
	rtype: bool

	runtime: O(a + b)
	space: O(a + b)
	"""
	if not w1 or not w2 or (not w1 and not w2):
		return False

	len_w1, len_w2 = len(w1), len(w2)
	if len_w1 != len_w2:
		return False

	counts_a = Counter(w1)
	counts_b = Counter(w2)

	for letter in w1:
		if counts_a[letter] != counts_b[letter]:
			return False

	return True

def is_anagram_by_sorting(w1, w2):
	"""
	Sort the two words and see if they match

	type: str, str
	rtype: bool

	runtime: O(aloga + blogb)
	space: O(a + b)
	"""
	if not w1 or not w2 or (not w1 and not w2):
		return False

	len_w1, len_w2 = len(w1), len(w2)
	if len_w1 != len_w2:
		return False

	s_w1, s_w2 = sorted(w1), sorted_w2
	return s_w1 == s_w2