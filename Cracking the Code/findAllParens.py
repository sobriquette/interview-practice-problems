def parens(n):
	if n == 0:
		return ''

	combos = []
	parens_util(n, n, '', combos)
	return combos

def parens_util(rem_open, rem_close, res, combos):
	if rem_open < 0 or rem_close < rem_open:
		return

	if rem_open == 0 and rem_close == 0:
		return combos.append(res)
	
	else:
		res += parens_util(rem_open - 1, rem_close, res + '(')
		res += parens_util(rem_open, rem_close, res + ')')