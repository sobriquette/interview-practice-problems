class Solution:
	def levelOrder(self, root):
		if not root:
			return []

		node = root
		queue, result = [node], []

		while queue:
			nodes_at_level = []
			level_width = len(queue)
			while len(nodes_at_level) < level_width:
				node = queue.pop(0)
				nodes_at_level.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			result.append(nodes_at_level)

		return result