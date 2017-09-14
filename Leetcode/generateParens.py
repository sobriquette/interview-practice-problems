class Solution:
	def generateParens(self, n):
		results = []
		self.generateParensHelper(results, "", n, n)
		return results

	def generateParensHelper(self, results, seq, left_count, right_count):
		if left_count < 0 or right_count < left_count:
			print("returning")
			return	# this is an invalid sequence
		if left_count == 0 and right_count == 0:
			print("done: ", seq)
			results.append(seq)
		if left_count > 0:
			print("left: %s || right: %s || seq: %s" % (left_count, right_count, seq))
			self.generateParensHelper(results, seq + "(", left_count - 1, right_count)
		if right_count > left_count:
			print("right: %s || left: %s || seq: %s" % (right_count, left_count, seq))
			self.generateParensHelper(results, seq + ")", left_count, right_count - 1)


print(Solution().generateParens(3))