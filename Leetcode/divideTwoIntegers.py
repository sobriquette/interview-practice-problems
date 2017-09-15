class Solution():
	def divide(self, dividend, divisor):
		if divisor == 0:
			return -1
		
		positive = (dividend < 0) is (divisor < 0)
		dividend, divisor = abs(dividend), abs(divisor)
		result = 0
		
		while dividend >= divisor:
			tmp, count = divisor, 1

			while dividend >= tmp:
				dividend -= tmp
				result += count
				count <<= 1
				tmp <<= 1

		if not positive:
			result = -result

		return min(max(-2147483648, result), 2147483647)

if __name__=="__main__":
	while True:
		dividend, divisor = map(int, input("Enter two numbers to divide with: ").split())
		print(Solution().divide(dividend, divisor))