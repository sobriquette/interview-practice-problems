def findOutOfOrderIndex(arr):
	index = 0
	for i in range(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			index = i + 1
			break

	return index

def reduceNum(index, arr):
	# replace all digits in lower places
	# than out of order digit with 9
	for i in range(index + 1, len(arr)):
		arr[i] = 9

	return arr

def tidyRestOfNum(index, arr):
	# backtrack through digits and reduce
	# until number is tidy
	isTidy = False
	while not isTidy and index > 0:
		if arr[index - 1] > arr[index]:
			arr[index - 1] -= 1
			arr[index] = 9
			index -= 1
		else:
			isTidy = True

	if arr[0] == 0:
		arr.pop(0)

	return arr

def tidyNumber(n):
	# immediate checks we can do
	if n < 10:
		return n

	# else we will tidy up number
	digits = list(map(int, str(n)))
	
	# find place of first digit out of order
	outOfOrderIndex = findOutOfOrderIndex(digits)

	# if outOfOrderIndex is still -1
	# n is tidy
	if outOfOrderIndex < 1:
		return n

	if outOfOrderIndex + 1 < len(digits):
		digits = reduceNum(outOfOrderIndex, digits)

	digits = tidyRestOfNum(outOfOrderIndex, digits)

	return "".join(map(str, digits))

if __name__=="__main__":
	T = int(input())

	for i in range(1 , T + 1):
		n = int(input())
		print("Case #{}: {}".format(i, tidyNumber(n)))

