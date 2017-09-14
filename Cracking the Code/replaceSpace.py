string = input("enter a string: ")

def replaceSpacesEasy(string):
	print(string.replace(' ', '%20'))

def replaceSpacesLong(string):
	newString = []
	replacement = '%20'

	for i in string:
		if i == ' ':
			newString.append(replacement)
		else:
			newString.append(i)

	print("".join(newString))

replaceSpacesEasy(string)
# Runtime: O(n)
# Space: O(n)
replaceSpacesLong(string)
# Runtime: O(2n)
# Space: O(n)
