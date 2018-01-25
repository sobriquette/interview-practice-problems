# get_min
# extract_min
# min_heapify
# decrease_key
# insert_key
# remove_key

class MinHeap:
	def __init__(self, capacity):
		self.size = 0
		self.capacity = capacity
		self.heap = [0] * capacity

	def parent(self, i):
		return (i - 1) // 2

	def left(self, i):
		return ((2 * i) + 1)

	def right(self, i):
		return ((2 * i) + 2)

	def swap(self, idx1, idx2):
		self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

	def get_min(self):
		if self.size == 0:
			return float('inf')

		return self.heap[0]

	# bubble up elements if they are smaller than parent
	def check_minheap_property(self, idx, parent_of_idx):
		while idx != 0 and self.heap[parent_of_idx] > self.heap[idx]:
			self.swap(idx, parent_of_idx)
			idx = parent(idx)
			parent_of_idx = parent(parent_of_idx)

	def insert_key(self, k):
		if self.size == self.capacity:
			return "Overflow: cannot insert key"

		self.size += 1
		idx = self.size - 1
		self.heap[idx] = k

		self.check_minheap_property(idx, parent(idx))

	def decrease_key(self, idx, new_val):
		self.heap[idx] = new_val
		self.check_minheap_property(idx, parent(idx))

	def delete_key(self, idx):
		self.decrease_key(idx, float('-inf'))
		self.extract_min()

	def extract_min(self):
		if self.size <= 0:
			return float('inf')
		if self.size == 1:
			self.size -= 1
			return self.heap[0]

		root = self.heap[0]
		self.heap[0] = self.heap[self.size - 1]
		self.size -= 1
		self.min_heapify(0)
		return root

	def min_heapify(self, idx):
		l = self.left(idx)
		r = self.right(idx)
		smallest = idx

		if l < self.size and self.heap[l] < self.heap[smallest]:
			smallest = l
		if r < self.size and self.heap[r] < self.heap[smallest]:
			smallest = r
		if smallest != idx:
			self.swap(idx, smallest)
			self.min_heapify(smallest)


