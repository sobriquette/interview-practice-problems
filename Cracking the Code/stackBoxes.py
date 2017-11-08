class SolutionR:
	def stack_boxes(self, boxes):
		if not boxes:
			return 0
		if len(boxes) == 1:
			return boxes[0][0]
		
		max_ht = float('-inf')
		boxes_sorted = reversed(sorted(boxes, key=lambda x: x[0]))

		for i in range(len(boxes_sorted)):
			curr_ht = build_stack(boxes_sorted, i)
			max_ht = max(max_ht, curr_ht)

		return max_ht

	def build_stack(self, boxes, idx):
		bot_box = boxes[idx]
		max_ht = 0

		for j in range(idx + 1, len(boxes)):
			if can_stack(boxes[j], bot_box):
				height = build_stack(boxes, j)
				max_ht = max(max_ht, curr_ht)
		
		return max_ht + bot_box[0]

	def can_stack(self, top_box, bot_box):
		if bot_box[0] <= top_box[0]:
			return False
		if (bot_box[1] * top_box[2]) <= (top_box[1] * top_box[2]):
			return False

		return True

class SolutionDP:
	def stack_boxes(self, boxes):
		if not boxes:
			return 0
		if len(boxes) == 1:
			return boxes[0][0]

		max_ht = float('-inf')
		boxes_sorted = reversed(sorted(boxes, key=lambdax: x[0]))
		stacks = [0 for _ in range(len(boxes))]

		for i in range(len(boxes_sorted)):
			curr_ht = build_stack(boxes_sorted, i, stacks)
			max_ht = max(max_ht, curr_ht)

		return max_ht

	def build_stack(self, boxes, idx, stacks):
		if idx >= len(boxes):
			return 0
		if idx < len(boxes) and stack[bot_box] > 0:
			return stacks[idx]

		bot_box = boxes[idx]
		max_ht = 0
		for j in range(idx + 1, len(boxes)):
			if can_stack(boxes[j], bot_box):
				curr_ht = build_stack(boxes, j, stacks)
				max_ht = max(max_ht, curr_ht)

		max_ht += bot_box[0]
		stacks[idx] = max_ht
		return max_ht

class Solution2:
	def stack_boxes(self, boxes):
		boxes_sorted = reversed(sorted(boxes, key=lambda x: x[0]))
		stack = [0 for _ in range(len(boxes))]
		return build_stack(boxes_sorted, None, 0, stack)

	def build_stack(boxes, bottom_box, offset, stack):
		if offset >= len(boxes):
			return 0

		new_bottom_box = boxes[offset]
		ht_with_bottom = 0

		if bottom_box == None or can_stack(new_bottom_box, bottom_box):
			if stack[offset] == 0:
				stack[offset] = build_stack(boxes, new_bottom_box, offset + 1, stack)
				stack[offset] += new_bottom_box[0]

			ht_with_bottom = stack[offset]

		ht_wo_bottom = build_stack(boxes, bottom_box, offset + 1, stack)

		return max(ht_with_bottom, ht_wo_bottom)

