def prefix_to_postfix(exp):
	operators = '*/+-'
	operands = []

	for char in reversed(exp):
		if char in operators:
			curr_exp = ''
			ops_count = 0
			while operands and ops_count < 2:
				curr_exp += operands.pop()
				ops_count += 1
			operands.append(curr_exp + char)
		else:
			operands.append(char)

	res = ''
	while operands:
		res += operands.pop()

	return res

print(prefix_to_postfix('+-435'))