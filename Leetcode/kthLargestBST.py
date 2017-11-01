def kth_largest_helper(node, k, count):
	if not node or count >= k:
		return

	# go as far right as possible
	kth_largest_helper(node.right, k, count)
	# add visited right node to count
	count += 1

	# if c == k then we have found our node
	if count == k:
		return node.data

	# check left subtree to find kth largest
	kth_largest_helper(node.left, k, count)

def kth_largest_bst(root, k):
	count = 0
	return kth_largest_helper(root, k, count)
