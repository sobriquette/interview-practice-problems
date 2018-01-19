"""
Implementation on attempt #2: 01/18/2018
"""

def reverse(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

def reverse_words(s):
	chars = list(s)
	chars_len = len(chars)
	
	# reverse all chars in string
	reverse(chars, 0, chars_len)

	# reverse words within chars array
	word_start = None
	for idx, char in enumerate(chars):
		if char == ' ':
			if word_start is not None:
				reverse(chars, word_start, idx - 1)
				word_start = None
		elif idx == chars_len - 1:
			if word_start is not None:
				reverse(chars, word_start, idx)
		else:
			if word_start is None:
				word_start = idx