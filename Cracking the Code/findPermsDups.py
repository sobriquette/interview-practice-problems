from collections import Counter
def print_perms(string):
	result = []
	char_map = Counter(string)
	print_perms_util(char_map, '', len(string), result)

def print_perms_util(char_map, prefix, remaining, result):
	if remaining == 0:
		result.append(prefix)
		return result

	for char in char_map.keys():
		count = char_map[char]
		if count > 0:
			char_map[char] = count - 1
			print_perms_util(char_map, prefix + char, remaining - 1, result)
			char_map[char] = count

print(print_perms('aabb'))