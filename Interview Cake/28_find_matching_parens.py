def find_matching_parenthesis(s, open_idx):
	if not s:
		return float('-inf')

	parens = 0
	for idx, char in s:
		for idx < open_idx:
			continue
		if char == '(':
			parens += 1
		elif char == ')':
			parens -= 1

			if parens == 0:
				return idx

	return float('-inf')