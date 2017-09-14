"""
CODING CHALLENGE:
Write a function that, when given a string as input, can output the indices of the farthest apart matching characters. Here are some example scenarios.

Input: 'yabcdey'

Output: [0, 6]

Explanation: Since the only matching characters are 'y', and 'y', we return the two places where 'y' appears in the string: at index 0 and index 6.

Input: 'yabcyzdefgz'

Output: [5, 10]

Explanation: There are 2 possible matching characters here-- 'y' and 'z'. The distance between the matching 'y' characters is 3. 
The distance between the matching 'z' characters is 4. So, 'z' wins! We output 5 (the index of the first 'z') and 10 (the index of the second 'z').

Input: 'abc'

Output: [None, None]

Explanation: There are no matching characters here. So, a sane output would be [None, None].

NOT SURE WHERE TO START? 

Start by writing a function that, when given a string as input, can return True or False depending on whether there are two matching characters in the string.

Then, tackle the aspect of getting the indices of those two matching characters.

Lastly, finish off by keeping track of the maximum distance between two matching characters.
"""

class Solution1():
	def find_furthest_matching_characters(self, string):
		# Exit early if we don't have a string to work with
		if not string:
			return [None, None]

		# Exit early if we do not have any matching characters
		characters_with_matches = self.get_matching_characters(string)
		if sum(characters_with_matches.values()) < 1:
			return [None, None]

		# Use the given string and dictionary of matching characters
		# and return the indices of the furthest matching characters
		return self.get_distances_of_matching_characters(string, characters_with_matches)

	def get_matching_characters(self, string):
		# There is a match if the count is greater than 0
		matches_dict = {}
		for char in string:
			if char in matches_dict:
				matches_dict[char] += 1
			else:
				matches_dict[char] = 0

		return matches_dict

	def get_distances_of_matching_characters(self, string, characters_with_matches):
		max_distance_indices = [-1, -1]
		distances_dict = {}
		for index, char in enumerate(string):
			# Look at character only if it has a match
			if characters_with_matches[char] > 0:
				# Update the dictionary with the index of the 2nd matching character
				if char in distances_dict:
					distances_dict[char][1] = index
					# Update max_distance_indices if the distance b/n the current set of indices
					# is greater than what we found in max_distance_indices
					char_dist = distances_dict[char][1] - distances_dict[char][0]
					curr_max_dist = max_distance_indices[1] - max_distance_indices[0]
					if char_dist > curr_max_dist:
						max_distance_indices = [distances_dict[char][0], distances_dict[char][1]]
				# Otherwise, we update distances_dict with
				# the index of the first matching character
				else:
					distances_dict[char] = [index, None]

		return max_distance_indices

class Solution2():
	def find_furthest_matching_characters(self, string):
		# Exit early if we don't have a string to work with
		if not string:
			return [None, None]

		indices_of_char_appearances = self.get_indices_for_char_appearances(string)

		max_distance_indices = [-1, -1]
		for k, v in indices_of_char_appearances.items():
			# Ignore items that do not have at least 2 indices
			if len(v) < 2:
				continue
			else:
				# Take the last index because this represents
				# the furthest matching character.
				# e.g. 'abexcdxex' --> 'x' : [3, 6, 8]
				# v[len(v)] - v[0] = 8 - 0
				char_dist = v[len(v) - 1] - v[0]
				curr_max_dist = max_distance_indices[1] - max_distance_indices[0]
				# Update max with the furthest two indices
				if char_dist > curr_max_dist:
					max_distance_indices = [v[0], v[len(v) - 1]]

		# If max_distance_indices has not changed,
		# there are no matching characters
		if sum(max_distance_indices) > 0:
			return max_distance_indices
		else:
			return [None, None]

	def get_indices_for_char_appearances(self, string):
		# Add index to dict every time the character appears
		indices_of_char_appearances = defaultdict(list)
		for index, char in enumerate(string):
			indices_of_char_appearances[char].append(index)

		return indices_of_char_appearances

from collections import defaultdict
if __name__ == "__main__":
	while True:
		string = input("Enter a string: ")
		if string == "q":
			break
		print(Solution1().find_furthest_matching_characters(string))
		print(Solution2().find_furthest_matching_characters(string))
