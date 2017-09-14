# ({[]})()
def validateStringParens(s):
	opens = '({['
	closes = ')}]'
	matches = []

	for c in string:
		if c in opens:
			matches.append(c)
		elif c in closes:
			if not matches:
				return False
			else:
				v = matches.pop()
				if closes.index(c) != opens.index(v):
					return False

	return len(matches) == 0

# runtime: O(n)
# space: O(n)

# OR can use dictionary to represent
def validateStringParens_Solution(s):
	openers_to_closers = {
		'(' : ')',
		'{' : '}',
		'[' : ']'
	}

	openers = frozenset(openers_to_closers.keys())
	closers = frozenset(openers_to_closers.values())

	openers_stack = []

	for char in s:
		if char in openers:
			openers_stack.append(char)
		elif char in closers:
			if not openers_stack:
				return False
			else:
				last_unclosed_opener = openers_stack.pop()
				if not openers_to_closers[last_unclosed_opener] == char:
					return False

	return openers_stack == []