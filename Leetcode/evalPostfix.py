def evalRPN(tokens):
	ops = '/*+-'
	opstack = []

	for token in tokens:
		if token not in ops:
			opstack.append(int(token))
		else:
			if len(opstack) >= 2:
				n1 = opstack.pop()
				n2 = opstack.pop()

				opstack.append(compute(token, n1, n2))

	return opstack.pop()


def compute(token, n1, n2):
	if token == '/':
		if (n2 > 0 and n1 > 0) or (n2 < 0 and n1 < 0):
			return n2 // n1
		else:
			return int(n2 / n1)
	elif token == '*':
		return n2 * n1
	elif token == '+':
		return n2 + n1
	elif token == '-':
		return n2 - n1

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))