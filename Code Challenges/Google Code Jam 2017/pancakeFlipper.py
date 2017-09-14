def convertToInts(string):
	ints = []
	for c in string:
		if c == '-':
			ints.append(0)
		if c == '+':
			ints.append(1)

	return ints

def flipPancakes(string, k):
	pancakeBits = convertToInts(string)
	front = 0
	back = len(pancakeBits) - 1
	happy = 1
	flips = 0

	while front < back:
		# flipping from front of line
		# flip k pancakes if curr one is 0
		if pancakeBits[front] is not happy:
			flips += 1
			# make sure does not go out of bounds
			if front + k <= len(pancakeBits):
				for i in range(front, front + k):
					pancakeBits[i] ^= 1
		
		# check if all are flipped already
		if sum(pancakeBits) == len(pancakeBits):
			return flips

		# flipping from back of line
		# flip k pancakes if curr one is 0
		if pancakeBits[back] is not happy:
			flips += 1
			# make sure does not go out of bounds
			if back - k >= 0:
				for i in range(back, back - k, -1):
					pancakeBits[i] ^= 1

		# check again if all are flipped already
		if sum(pancakeBits) == len(pancakeBits):
			return flips

		front += 1
		back -= 1

	return "IMPOSSIBLE"


if __name__=="__main__":
	T = int(input())

	for i in range(1, T + 1):
		inputs = input().split(" ")
		pancakes, k = inputs[0], int(inputs[1])
		print("Case #{}: {}".format(i, flipPancakes(pancakes, k)))