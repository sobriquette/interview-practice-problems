def infix_to_postfix(expression):
	prec = { '/': 3, '*': 3, '+': 2, '-': 2, '(': 1 }
	opstack = []
	output = ''

	for char in expression:
		if char == ' ':
			continue
		elif char == '(':
			opstack.append(char)
		elif char == ')':
			top = opstack.pop()
			while opstack and top != '(':
				output += top
				top = opstack.pop()
		elif char in '/*+-':
			top_idx = len(opstack) - 1
			while opstack and prec[opstack[top_idx]] >= prec[char]:
				output += opstack.pop()
			opstack.append(char)
		else:
			output += char

	if opstack:
		while opstack:
			output += opstack.pop()

	return output

print(infix_to_postfix('(A + B) * C - (D - E) * (F + G)'))
