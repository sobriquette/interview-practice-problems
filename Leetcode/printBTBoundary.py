def print_right_boundary(root, should_print):
	if not root:
		return

	print_right_boundary(root.left, (should_print and not root.right))
	print_right_boundary(root.right, should_print)

	if should_print or (not root.left and not root.right):
		print(root.data)

def print_left_boundary(root, should_print):
	if not root:
		return
	
	if should_print or (not root.left and not root.right):
		print(root.data)
	
	print_left_boundary(root.left, should_print)
	print_right_boundary(root.right, (should_print and not root.left))

def print_binary_tree_boundary(root):
	if not root: 
		return None

	print(root.data)
	print_left_boundary(root.left, True)
	print_right_boundary(root.right, True)