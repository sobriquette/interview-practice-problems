def add_strings_as_ints(s1, s2):
	if not s1:
		return s2
	if not s2:
		return s2
	if not s2 and not s1:
		return 0

	s1 = s1.replace(',', '')
	s2 = s2.replace(',', '')
	
	res = ''
	carry = 0
	s1_idx, s2_idx = len(s1) - 1, len(s2) - 1

	while s1_idx >= 0 or s2_idx >= 0 or carry:
		if s1_idx >= 0:
			carry += int(s1[s1_idx])
			s1_idx -= 1
		if s2_idx >= 0:
			carry += int(s2[s2_idx])
			s2_idx -= 1
		
		res = str(carry % 10) + res
		carry //= 10

	return res

s1 = '121'
s2 = '289'
print(add_strings_as_ints(s1, s2))