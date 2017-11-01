def prefix_to_postfix(expression):
	ops = '/*+-'
	opstack = []
	output = ''

	for token in reversed(expression):
		if token not in ops:
			opstack.append(token)
		else:
			tmp = ''
			cnt = 0
			while opstack and cnt < 2:
				tmp += opstack.pop()
				cnt += 1

			tmp += token
			opstack.append(tmp)

	while opstack:
		output += opstack.pop()

	return output

print(prefix_to_postfix('+-435'))