def has_palidnrome_permuation(s):
	unpaired_chars = set()

	for c in s:
		if c in unpaired_chars:
			unpaired_chars.remove(c)
		else:
			unpaired_chars.add(c)

	return len(unpaired_chars) <= 1