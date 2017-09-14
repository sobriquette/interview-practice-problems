#Given an array with unique characters arr and a string str, find the smallest substring of str containing all characters of arr.
#
#Example:
#arr: [x,y,z], str: xyyzyzyx
#result: zyx
import collections

def smallestSubstring(arr, string):
	need = collections.Counter(arr)
	missing = len(arr)
	h = head = tail = 0

	for t, c in enumerate(string, 1):
		if c in arr:
			if need[c] > 0:
				missing -= 1
		need[c] -= 1
		if missing <= 0:
			while h < t and need[string[h]] < 0:
				need[string[h]] += 1
				h += 1
			if tail <= 0 or t - h <= tail - head:
				head, tail = h, t

	return string[head:tail]

def minWindow(s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
    	missing -= need[c] > 0
    	need[c] -= 1
    	if not missing:
    		while i < j and need[s[i]] < 0:
    			need[s[i]] += 1
    			i += 1
    		if not J or j - i <= J - I:
    			I, J = i, j
    return s[I:J]

if __name__=="__main__":
	string = "xyyzyxyz"
	arr = ['x', 'y', 'z']
	print(smallestSubstring(arr, string) == minWindow(string, arr))