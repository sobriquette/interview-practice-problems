# * ^ *		=>		* * *
# * | *		=>		- - >
# * | *		=>		* * *

# Given NxN matrix, rotate image 90 degrees IN PLACE.

image = [['*', '^', '*'], 
		 ['*', '|', '*'], 
		 ['*', '|', '*']]

image2 = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P']]

# First attempt (not in-place):
def rotateWithDS(image):
	if image == [] or len(image) != len(image[0]):
		return image

	row = len(image) - 1
	rotated = [[] for i in range(len(image))]

	while row >= 0:
		for i in range(len(image)):
			rotated[i].append(image[row][i])
		row -= 1

	print(rotated)

# Runtime: O(n^2)
# Space: O(n^2)

# Second attempt (in-place):
def rotateInPlace(image):
	if image == [] or len(image) != len(image[0]):
		return image

	size = len(image)
	half = size // 2

	for i in range(half):
		for j in range(i, size - 1 - i):
			tl = image[i][j] # get top left corner
			
			# left to top
			image[i][j] = image[size - 1 - j][i]
			# bottom to left
			image[size - 1 - j][i] = image[size - 1 - i][size - 1 - j]
			# right to bottom
			image[size - 1 - i][size - 1 - j] = image[j][size - 1 - i]
			# top to right
			image[j][size - 1 - i] = tl

	print(image)

# Runtime: O(n^2)
# Space: O(n)

if __name__ == "__main__":
	rotateWithDS(image2)
	rotateInPlace(image2)