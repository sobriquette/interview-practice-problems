def parse_number(idx, eqn, eqn_len):
	num = ''
	while idx < eqn_len and eqn[idx].isdigit():
		num += eqn[idx]
		idx += 1
	return num

def calculate_num(first, op, second):
	if op == '+':
		return first + second
	elif op == '-':
		return first - second
	elif op == '*':
		return first * second
	elif op == '/':
		return first / second
	else:
		return second

def collapse_top(op, operands, operators, op_priority):
	while len(operators) >= 1 and len(operands) >= 2:
		if op_priority[op] <= op_priority[operators[-1]]:
			second = operands.pop()
			first = operands.pop()
			curr_top_op = operators.pop()

			collapsed_num = calculate_num(first, curr_top_op, second)
			operands.append(collapsed_num)
		else:
			break

def calculate(eqn):
	operands = []
	operators = []
	op_priority = {
		'*': 2,
		'/': 2,
		'+': 1,
		'-': 1,
		'None': 0
	}

	idx = 0
	eqn_len = len(eqn)
	while idx < eqn_len:
		try:
			value = parse_number(idx, eqn, eqn_len)
			operands.append(int(value))

			idx += len(value)
			if idx >= eqn_len:
				break

			if eqn[idx] in op_priority:
				op = eqn[idx]
			else:
				op = 'None'
			collapse_top(op, operands, operators, op_priority)
			operators.append(op)
			idx += 1
		except ValueError:
			return float('-inf')

	collapse_top('None', operands, operators, op_priority)
	
	if operands and not operators:
		return operands.pop()
	
	return 0

print(calculate('2*3+5/6*3+15'))