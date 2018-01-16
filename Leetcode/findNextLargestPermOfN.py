"""
Permute the digits of n to find the next largest permutation.
Assume n > 0.

type: list[int]
rtype: list[int]
"""
def reverse(lst, start, end):
	while start < end:
		lst[start], lst[end] = lst[end], lst[start]
		start += 1
		end -= 1

def find_next_permutation(n):
	if n <= 10:
		return n

	length = len(n)
	# find the pivot point
	pivot_idx = length - 1
	while pivot_idx > 1:
		if n[pivot_idx - 1] < n[pivot_idx]:
			pivot_idx -= 1
			break
		pivot_idx -= 1

	# find the next number larger than the pivot
	swap_idx = None
	for i in range(length - 1, pivot_idx, -1):
		if n[i] > n[pivot_idx]:
			swap_idx = i

	if swap_idx is not None:
		lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

	reverse(n, pivot_idx, length - 1)