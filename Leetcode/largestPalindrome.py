import math

digits = int(input("n of n-digits to multiply: "))

def findLargestPalindrome(digits):
	upperLimit = 1 * pow(10, digits)
	lowerLimit = 1 * pow(10, digits - 1)
	largestPal = 0

	for i in range(upperLimit, lowerLimit, -1):
		for j in range(upperLimit, lowerLimit, -1):
			product = i * j
			if str(product) == str(product)[::-1]:
				if product > largestPal:
					largestPal = product

	return largestPal
	
print(findLargestPalindrome(digits))