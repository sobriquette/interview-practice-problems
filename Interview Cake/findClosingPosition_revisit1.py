def findClosingParens(open_index, string):
	if string[open_index] == '(':
		count = 1
	else:
		return "invalid character, expected '('"

	for i in range(open_index + 1, len(string)):
		if string[i] == '(':
			count += 1
		elif string[i] == ')':
			count -= 1

		if count == 0:
			return i

	if count > 0:
		return "string is unbalanced"

# runtime: O(n)
# space: O(1)