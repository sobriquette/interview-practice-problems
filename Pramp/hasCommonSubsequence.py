def has_subsequence(a, b):
	chars_a = set(a)

	for c in b:
		if c in chars_a:
			return 1

	return 0


if __name__ == "__main__":
	num_tests = int(input())

	for i in range(num_tests):
		a, b = input().split()
		print(has_subsequence(a, b))