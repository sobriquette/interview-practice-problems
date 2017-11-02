def find_magic_util_distinct(arr, lo, hi):
	if hi < lo:
		return -1

	mid = (lo + hi) // 2

	if mid == arr[mid]:
		return mid
	elif arr[mid] > mid:
		return find_magic_util(arr, lo, mid - 1)
	else:
		return find_magic_util(arr, mid + 1, hi)

def find_magic_util(arr, lo, hi):
	if hi < lo:
		return -1

	mid_idx = (lo + hi) // 2
	mid_val = arr[mid_idx]

	if mid_val == mid_idx:
		return mid_idx

	left_idx = min(mid_idx - 1, mid_val)
	left = find_magic_util(arr, lo, left_idx)
	if left >= 0:
		return left

	right_idx = max(mid_idx + 1, mid_val)
	right = find_magic_util(arr, right_idx, hi)
	return right

def find_magic(arr):
	return find_magic_util_distinct(arr, 0, len(arr))

