s1 = 'a1t'
s2 = '1atq'

# create a dictionary of characters in string
def buildCharDict(string):
	cDict = {}

	for i in string:
		if i in cDict:
			cDict[i] += 1
		else:
			cDict[i] = 1

	return cDict

# if all characters in second string are in dict
# then they are 1:1 match, which means they are permutations
def isPermutation(cDict, string):
	for i in string:
		if i in cDict:
			cDict[i] -= 1
	
	# calculate absolute of values in dict
	# to account for possibility of negative values
	return sum(abs(c) for c in cDict.values() if c > 0) == 0

if __name__ == "__main__":
	# return false immediately if strings are different lengths
	# or if either string is empty
	if len(s1) != len(s2) or s1 is None or s2 is None:
		print(False)
	else:
		print(isPermutation(buildCharDict(s1), s2))

# Runtime complexity: O(3n)
# 3 for loops, none nested

# Space complexity: O(n)
# dictionary to hold keys and values