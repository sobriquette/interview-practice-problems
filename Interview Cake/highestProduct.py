# Given a list of integers, find the highest product you can get from 3 of the integers

def isValid(list_of_ints):
	if len(list_of_ints) < 3:
		raise IndexError("you need at least 3 ints!")
	elif len(list_of_ints) == 3:
		return list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
	else:
		return True

# Brute force
# Positive ints only
def highestProdBF(list_of_ints):
	low_to_high = sorted(map(abs, list_of_ints))
	end = len(list_of_ints)

	return low_to_high[end - 1] * low_to_high[end - 2] * low_to_high[end - 3]

# Runtime: O(nlogn) for sorting
# Space: O(n)

# Greedy approach #1
# Positive ints only
def highestProdGreedy1(list_of_ints):
	high_1 = list_of_ints[0]
	high_2 = list_of_ints[1]
	high_3 = list_of_ints[2]
	curr_min = min(high_1, high_2, high_3)
	max_prod = high_1 * high_2 * high_3

	for index, value in enumerate(list_of_ints):
		if index < 3:
			continue

		# need to be careful when multiple values are the same
		if value > curr_min:
			if curr_min == high_1:
				high_1 = value
			if curr_min == high_2:
				high_2 = value
			if curr_min == high_3:
				high_3 = value
			curr_min = min(high_1, high_2, high_3)

		curr_prod = high_1 * high_2 * high_3
		if curr_prod > max_prod:
			max_prod = curr_prod

	return max_prod

# Runtime: O(n)
# Space: O(1)

# Greedy approach # 2
# Positive and negative ints
def highestProdGreedy2(list_of_ints):
	high = max(list_of_ints[0], list_of_ints[1], list_of_ints[2])
	low = min(list_of_ints[0], list_of_ints[1], list_of_ints[2])
	high_prod_2 = max(list_of_ints[0] * list_of_ints[1], list_of_ints[1] * list_of_ints[2], list_of_ints[0], list_of_ints[2])
	low_prod_2 = min(list_of_ints[0] * list_of_ints[1], list_of_ints[1] * list_of_ints[2], list_of_ints[0], list_of_ints[2])
	max_prod = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

	for index, value in enumerate(list_of_ints):
		if index < 3:
			continue

		# need to be careful when multiple values are the same
		if value * high_prod_2 > max_prod:
			max_prod = value * high_prod_2
		elif value * low_prod_2 > max_prod:
			max_prod = value * low_prod_2

		if value * high > high_prod_2:
			high_prod_2 = value * high
		
		if value * low < low_prod_2:
			low_prod_2 = value * low

		high = max(high, value, low)
		low = min(high, value, low)

	return max_prod

# Runtime: O(n)
# Space: O(1)

if __name__=="__main__":
	list_of_ints = [[1, 10, -5, 1, -100], [-10, -10, 1, 2, 3], [10, 5, 4, 6, 8, 1], [3, 2, 7, 9, 5], [-5, 4, 6, 9]]
	for i in list_of_ints:
		if isValid(i):
			#print(highestProdBF(list_of_ints))
			#print(highestProdGreedy1(list_of_ints))
			print(highestProdGreedy2(i))
