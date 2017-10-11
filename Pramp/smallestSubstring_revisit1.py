def get_shortest_unique_substring(arr, string):
	seen = {c: 0 for c in arr}
	start = 0
	num_unique_chars = 0
	result = ""

	for idx, c in enumerate(string):
		# we don't need this character
		if c not in seen:
			continue

		c_count = seen[c]
		if c_count == 0:
			num_unique_chars += 1

		seen[c] += 1

		while num_unique_chars == len(arr):
			curr_len = idx - start + 1
			if curr_len == len(arr):
				return string[start : idx + 1]

			if result == "" or curr_len < len(result):
				result = string[start : idx + 1]

			curr_front = string[start]

			if curr_front in seen:
				front_count = seen[curr_front] - 1

				if front_count == 0:
					num_unique_chars -= 1

				seen[curr_front] = front_count

			start += 1
	
	return result

if __name__=="__main__":
	arr1 = ['x', 'y', 'z']
	string1 = 'xyyzyzyx'

	print(get_shortest_unique_substring(arr1, string1) == 'zyx')

	arr2 = ['a']
	string2 = 'a'
	print(get_shortest_unique_substring(arr2, string2) == 'a')