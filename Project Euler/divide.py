class Solution:
	def divide(self, dividend, divisor):
		if divisor == 0:
			return None
		
		abs_dividend = abs(dividend)
		abs_divisor	= abs(divisor)

		quotient = 0
		while abs_dividend >= abs_divisor:
			abs_dividend -= abs_divisor
			quotient += 1

		if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
			return quotient
		else:
			return self.negate(quotient)


	def negate(self, n):
		sign = -1 if n > 0 else 1
		neg = 0

		while n != 0:
			neg += sign
			n += sign

		return neg

	def subtract(self, a, b):
		return a + neg(b)

	def multiply(self, a, b):
		if (a < b):
			return self.multiply(b, a)

		s = 0
		for i in range(abs(b), 0, -1):
			sum += a

		if b < 0:
			sum = negate(sum)

		return sum
