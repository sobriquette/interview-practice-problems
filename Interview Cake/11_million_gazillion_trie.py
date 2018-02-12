# If there is a web crawler that manages a set of visited URLs,
# and the set has grown too large and our machine is running out of memory,
# how can we reduce the amount of space taken by the visited() set?
#
# Analysis:
# In a flat dictionary approach, where all URLs are n length or less,
# our space complexity is O(n * 26^(n))
# where:
# 	n: the number of possible URLs
# 	26^n: 26 possible characters (a-z) that can be used per char
#
# In a trie, each layer has 26 nodes, and each node has 26 children nodes.
# For all URLs of n length or less, our space complexity is reduced to:
# O(26^n) -- a reduction by factor of n from the flat dictionary appraoch.
#
# N.B. most web browsers do not support URLs longer than 2,000 chars in length

# Solution: use a trie
class Trie:
	def __init__(self):
		self.root = {}

	def check_present_and_add(self, word):
		curr_node = self.root
		is_new_word = False

		# Traverse downwards through trie,
		# adding nodes as needed,
		# and tracking where we add new nodes.
		for char in word:
			if char not in curr_node:
				is_new_word = True
				curr_node[char] = {}
			curr_node = curr_node[char]

		# Explicitly mark the end of the word,
		# else we might say a word is present if
		# it is a prefix of a different, longer word
		# that was added earlier.

		# Opt 1: use a message, eg. "End of Word"
		if "End of Word" not in current_node:
			is_new_word = True
			current_node["End of Word"] = {}

		# Opt 2: add the entire word as end node
		#		 --> no need to reconstruct in search
		if word not in current_node:
			is_new_word = True
			current_node[word] = {}

		return is_new_word