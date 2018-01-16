def convert_to_postfix(exp):
	ops = { '(': 0, ')': 0, '*': 1, '/': 1, '+': 2, '-': 2 }

	ops, res = [], ''
	num_ops = 0

	for char in exp:
		if char == '(':
			ops.append(char)
			num_ops += 1
		elif char == ')':
			while ops and ops[num_ops] != ')':
				res += ops.pop()
		elif char in ops:
			while ops and ops[num_ops] >= ops[char]:
				res += ops.pop()
				num_ops -= 1
			ops.append(char)
		else:
			res += char

	while ops:
		res += ops.pop()

	return res
	