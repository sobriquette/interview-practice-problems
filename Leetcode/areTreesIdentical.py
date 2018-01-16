def is_same_tree_rec(t1, t2):
	if not t1 and not t2:
		return True
	elif t1 and t2:
		if t1.data != t2.data:
			return False
		is_same_tree_rec(t1.left, t2.left)
		is_same_tree_rec(t1.right, t2.right)
	else:
		return False

def is_same_tree_it(t1, t2):
	nodes = [(t1, t2)]

	while nodes:
		t1, t2 = nodes.pop()
		if not t1 or not t2 or (t1.data != t2.data):
			return False
		nodes.append((t1.left, t2.left), (t1.right, t2.right))

	return True