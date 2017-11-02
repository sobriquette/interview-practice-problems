def mult_util(n1, n2):
	if n2 == 0:
		return 0
	elif n2 == 1:
		return n1
	else:
		s = n2 >> 1
		half = mult_util(n1, s)
		print("s={}, half = {}".format(s, half))
		if n2 % 2 == 0:
			return half + half
		else:
			return half + half + n1

def recursive_multiply(n1, n2):
	if n2 > n1:
		return recursive_multiply(n2, n1)

	return mult_util(n1, n2)

print(recursive_multiply(35, 31))