def build_new_string(s, l):
	res = ''
	for c in s:
		if c == ' ':
			res += '%20'
		else:
			res += c

	return res

def update_existing_string(s, l):
	num_spaces = 0

	for idx, c in s:
		if c == ' ':
			num_spaces += 1

	idx = l + num_spaces * 3
	for i in range(l - 1, -1 -1):
		if s[i] == ' ':
			s[idx - 1] = '0'
			s[idx - 2] = '2'
			s[idx - 3] = '%'
			idx -= 3
		else:
			s[idx - 1] = s[i]
			idx -= 1

	return s