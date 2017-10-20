# [1] Given an array of integers, determine whether or not there exist two elements in the array (at different positions) whose sum is equal to some target value. 
# Examples: [5, 4, 2, 4], 8 --> true 
# 			[5, 1, 2, 4], 8 --> false
#
# Constraints:
# - negative #s?
# - empty arr?
# - includes #s greater than target?
#
# BF - O(n^2), go through each pair
# Sort - O(nlogn), sort array, have a start & end pointer
# 		while start < end:
# 			if start + end == target: return true
# 			elif start + end < target: start += 1
# 			else: end -= 1
# 		return false
#
# Dict - O(n), use dictionary to track pairs, where key => (target - n) and value => n

class Solution:
	def has_pair(self, target, arr):
		"""
			Uses dictionary to store complementary integers,
			where the key is the "missing" integer needed to reach target.
			
			If the current n is already in the dictionary, that means
			we have found the "missing" integer for a previous n.

			Runtime: O(n), where n is size of input array
			Auxiliary Space: O(n), where n is size of input array

			itype: list
			rtype: bool
		"""
		pairs = {}
		for n in arr:
			if n in pairs:
				return True
			else:
				pairs[target - n] = n

		return False


# [2] Implement a set-like data structure that supports Insert, Remove, and GetRandomElement efficiently. 
# Example: If you insert the elements 1, 3, 6, 8 and remove 6, the structure should contain [1, 3, 8]. 
# Now, GetRandom should return one of 1, 3 or 8 with equal probability.  
#
# Constraints:
# - "efficiently" == O(1)? O(n)?
# - "equal probability" == Return element if it has not already been seen before?
# 						   Or for each call to GetRandom, each number has same P of returning?
# - will there be repeating numbers?

import random
class Solution:
	class ArrayDict:
		def __init__(self):
			self.my_dict = {} # will handle repeating numbers
			self.my_list = []

		def insert(self, n):
			self.my_list.append(n)
			last_idx = len(self.my_list) - 1

			# Tracks indices of number n, if it repeats
			# E.g. [1, 1, 3, 6, 8, 6] --> '6': [3, 5]
			if n in self.my_dict:
				my_dict[n].append(last_idx)
			else:
				my_dict[n] = [last_idx]

		def remove(self, n):
			if n not in self.my_dict:
				raise KeyError("This element does not exist")

			indices = self.my_dict[n]

			# go backwards to maintain O(1) pop()
			for idx in reversed(indices):
				last_idx = len(self.my_list) - 1
				last_n = self.my_list[last_idx]
				# swap the number to be removed
				# with the last element of the list
				self.my_list[last_idx], self.my_list[idx] = \
				self.my_list[idx], self.my_list[last_idx]

				self.my_list.pop() # remove from list
				self.my_list[last_n] = idx # update index for n that was swapped
				self.my_dict[n].pop() # remove from dict

			# when all instances of number are removed from list
			# remove from dictionary as well
			self.my_dict.pop('n')

		def get_random(self):
			# assumes "equal probability" means that
			# for each call to get_random(), 
			# each number has equal P of being returned
			return random.choice(self.my_list)












