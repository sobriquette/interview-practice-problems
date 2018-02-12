def count(pattern, char):
	cnt = 0
	for c in pattern:
		if c == char:
			cnt += 1

	return cnt

def matches(pattern, value, main_size, alt_size, alt_idx):
	str_idx = main_size

	for i in range(1, len(pattern)):
		if pattern[i] == pattern[0]:
			size = main_size
			offset = 0
		else:
			size = alt_size
			offset = alt_idx

		if not is_equal(value, offset, str_idx, size):
			return False
		str_idx += size
	return True

def is_equal(s1, offset1, s2, offset2):
	for i in range(size):
		if s1[offset1 + i] != s1[offset2 + i]:
			return False

	return True

def is_match(pattern, value):
	if not pattern:
		return len(value) == 0

	pat_main = pattern[0]
	pat_alt = 'b' if pat_main == 'a' else 'a'
	size = len(value)

	pat_main_cnt = count(pattern, pat_main)
	pat_alt_cnt = len(pattern) - pat_main_cnt
	pat_alt_idx = pattern.index(pat_alt)
	max_main_size = size // pat_main_cnt

	for main_size in range(max_main_size):
		rem_size = size - main_size * pat_main_cnt
		if pat_alt_cnt == 0 or rem_size % pat_alt_cnt == 0:
			alt_idx = pat_alt_idx * main_size

			alt_size = 0
			if pat_alt_cnt > 0:
				alt_size = rem_size // pat_alt_cnt

			if matches(pattern, value, main_size, alt_size, alt_idx):
				return True

	return False