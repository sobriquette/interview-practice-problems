def swap1(a, b):
	b = b/a
	a = a * b
	b = a * 1/b

def swap2(a, b):
	if a < b:
		return swap2(b, a)
	a = a - b
	b = a + b
	a = b - a

def swap3(a, b):
	a = a ^ b
	b = a ^ b
	a = a ^ b
	
