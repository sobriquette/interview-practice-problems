import math

n = int(input("Enter number you want to find largest prime for: "))

def findLargestPrime(n):
	# eliminate all even number factors
	while (n % 2 == 0):
		n = n // 2

	# eliminate all odd number factors
	for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
		while (n % i == 0 and n // i > 1):
			n = n // i
			
	# remaining n must be prime but need to check if not 1 or 2
	if (n > 2):
		return n

print(findLargestPrime(n))