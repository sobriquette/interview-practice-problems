class SolutionGenerator:
	def powerset(self, seq):
		if len(seq) == 0:
			yield []
		elif len(seq) == 1:
			yield seq
			yield []
		else:
			for item in self.powerset(seq[1:]):
				yield [seq[0]] + item
				yield item

class SolutionRecursive:
	def powerset(self, seq):
		if not seq:
			return [set()]
		r = []
		for e in seq:
			set_e = {e}
			for el in self.powerset(seq - set_e):
				if el not in r:
					r.extend([el, el | set_e])
		return r

class SolutionBits:
	def powerset(self, seq):
		all_subsets = []
		max_size = 1 << len(seq) # power of 2
		
		for b in range(max_size):
			# b is the length of the binary string
			subset = self.convertBToSet(b, seq)
			all_subsets.append(subset)

		return all_subsets

	def convertBToSet(self, b, seq):
		subset = []
		set_idx = 0

		while b > 0:
			# the kth set bit tells us if the num
			# at seq[set_idx] should go in the subset
			if (b & 1) == 1:
				subset.append(seq[set_idx])
			set_idx += 1
			b >>= 1

		return subset



if __name__=="__main__":
	s1 = SolutionGenerator()
	seq = [1, 2, 3, 4]
	r = [x for x in s1.powerset(seq)]
	print(r)

	s2 = SolutionRecursive()
	print(s2.powerset({1, 2, 3}))

	s3 = SolutionBits()
	s3_sol = s3.powerset([1, 2, 3, 4])
	print(s3_sol)