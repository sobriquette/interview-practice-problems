# Sieve of Eratosthenes
# Find primes less than n first
def SieveOfEratosthenes(upperLimit):
	last = upperLimit + 1
	multiples = set()
	
	for i in range(2, last):
		# Get a set of composite numbers in range n
		# Can stop loop if i**2 is greater than last
		if i not in multiples and i * i < last:
			# If i is not in multiples
			# Then update multiples list with multiples of i
			multiples.update(range(i * i, last, i))

	# Return only differences between full range and multiples
	# Result will contain only primes
	return set(range(2, last)).difference(multiples)

# Then perform prime factorization
def FasterFindLCM(upperLimit):
	primes = SieveOfEratosthenes(upperLimit)
	LCM = 1
	
	for p in primes:
		i = 1
		while p * i < upperLimit:
			i *= p

		LCM *= i

	return LCM


# BRUTE FORCE
def FindLCM(upperLimit):
	upperLimitPadded = upperLimit + 1
	LCM = upperLimit
	isLCMForRange = []
	isLCM = False

	if upperLimit == 1:
		return upperLimit
	else:
		while (not isLCM):
			for i in range(1, upperLimitPadded):
				isLCMForRange.append(LCM % i == 0)
			if sum(isLCMForRange) == upperLimit:
				isLCM = True
				return LCM
			else:
				del isLCMForRange[:]
				LCM += upperLimit

# Call brute force solution

if __name__ == "__main__":
	upperLimit = int(input("Enter the highest number in the range: "))
	#print(FindLCM(upperLimit))
	print(FasterFindLCM(upperLimit))