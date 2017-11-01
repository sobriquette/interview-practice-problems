def sum_subarrays_v1(arr):
	sums = [arr[0]]

	for i, n in enumerate(arr):
		if i == 0:
			continue
		sums.append(sums[i - 1] + (n * (i + 1)))

	return sum(sums)

def sum_subarrays_v2(arr):
	total = 0
	length = len(arr)

	for i, n in enumerate(arr):
		total += n * (i + 1) * (length - i)

	return total

if __name__=="__main__":
	while True:
		input_ = input("Enter a list of numbers: ")

		if input_ == 'q':
			break
		else:
			arr = list(map(int, input_.split()))

			print(sum_subarrays_v1(arr) == sum_subarrays_v2(arr))