def reverse_words(arr):
	# reverse the whole array first
	mirrorReverse(arr, 0, len(arr) - 1)
	# reverse individual words in array
	w_start = None
	for idx, c in enumerate(arr):
		if c == ' ':
			if w_start is not None:
				mirrorReverse(arr, w_start, idx - 1)
				w_start = None
		elif idx == len(arr) - 1:
			if w_start is not None:
				mirrorReverse(arr, w_start, idx)
		else:
			if w_start is None:
				w_start = idx
	
	return arr

def mirrorReverse(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

if __name__=="__main__":
	arr = ['a', ' ']
	print(reverse_words(arr))