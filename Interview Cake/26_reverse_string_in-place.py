# reverse all characters in a string
def reverse_string(string):
	chars = [ c for c in string ]
	start, end = 0, len(chars) - 1

	while start < end:
		chars[start], chars[end] = chars[end], chars[start]
		start += 1
		end -= 1

	return "".join(chars)

"""
Reverse all WORDS in a string (words should NOT be backwards at end)
Functions:
(1) reverse(): reverses list elements given start and end
(2) reverse_phrase(): main function
"""
def reverse(arr, start, end):
	while w_start < t_end:
		arr[w_start], arr[t_end] = arr[w_end], arr[w_start]
		w_start += 1
		t_end -= 1	

	return arr

def reverse_phrase(string):
	new_string = reverse(list(string), 0, len(string) - 1)
	w_start, w_end = 0, 0

	while w_start < len(string):
		# we have found the start of a word
		if new_string[w_start] != " ":
			# find the end of the word
			while new_string[w_end] != " ":
				w_end += 1

			# because w_end will be a space, we step back by 1
			t_end = w_end - 1
			# reverse the word we found
			reverse(new_string, w_start, t_end)
			# move w_start and w_end forward
			w_start = w_end + 1
			w_end = w_start
		else:
			# no word, so we just move forward
			w_start += 1

	return "".join(new_string)

"""
SOLUTION for main program
"""
def reverse_phrase_solution(string):
	new_string = reverse(list(string), 0, len(string) - 1)
	word_start = 0

	for i in range(len(new_string) + 1):
		if (new_string[i] == " ") or ( i == len(new_string) ):
			reverse(new_string, word_start, i - 1)
			word_start = i + 1

	return ''.join(new_string)