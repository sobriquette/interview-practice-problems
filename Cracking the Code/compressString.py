# 01/05/2018
def compress_string(s):
	char_count = 1
	curr_char = s[0]
	res = []

	for idx, char in enumerate(s):
		if idx == 0:
			continue
		if char == curr_char:
			char_count += 1
		else:
			res.append(curr_char, char_count)
			curr_char = char
			char_count = 1

	res.append(curr_char, char_count)
	final_string = ''.join(res)

	if len(final_string) >= len(s):
		return s
	else:
		return final_string

# 2017
def compressString1(string):
	length = len(string)
	curr = 0
	chars = []
	charCounts = []
	charIndex = 0

	if length == 0:
		return string

	while curr < length:
		chars.append(string[curr])
		charCounts.append(1)

		for i in range(curr, length - 1):
			if chars[charIndex] == string[i + 1]:
				charCounts[charIndex] += 1
			else:
				break

		curr = sum(charCounts)
		charIndex += 1

	compressed = ''.join('{}{}'.format(*c) for c in zip(chars, charCounts))
	
	if len(compressed) < length:
		print(compressed)
	else:
		print(string)

def compressString2(string):
	compressed = ""
	length = len(string)

	if length == 0:
		return ""
	elif length == 1:
		return string + "1"
	else:
		count = 1
		i = 0
		
		while i < length - 1:
			if string[i] == string[i + 1]:
				count += 1
			else:
				compressed = compressed + string[i] + str(count)
				count = 1

			i += 1

		compressed = compressed + string[i] + str(count)

		if len(compressed) < length:
			print(compressed)
		else:
			print(string)

if __name__ == "__main__":
	s = input("Enter a string: ")
	while (s != 'q'):
		#compressString1(s)
		compressString2(s)
		s = input("Enter a string: ")

