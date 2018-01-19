# Assumes the array is rotated

def findRotationPoint(words):
	left = 0
	right = len(left) - 1
	mid = (left + right) // 2

	while left < right:
		if words[mid] >= words[right]:
			left = mid
		else:
			right = mid
		mid = (left + right) // 2

	return mid

def findRotationPointSolution(words):
	first_word = words[0]
	floor_index = 0
	ceiling_index = len(words) - 1

	while floor_index < ceiling_index:
		guess = floor_index + (ceiling_index - floor_index) // 2

		# if guess comes after first word or is first word
		if word[guess] >= first_word:
			# go right
			floor_index = guess
		else:
			# go left
			ceiling_index = guess

		# if floor meets ceiling
		if floor_index + 1 == ceiling_index:
			# that means we are at the beginning of the list
			# and ceiling is the first word
			return ceiling_index