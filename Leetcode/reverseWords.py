class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		word_start = None
		words = []
		
		for i, c in enumerate(s):
			if c == ' ':
				if word_start is not None:
					words.append(s[word_start:i])
					word_start = None
			elif i == len(s) - 1:
				if c != ' ' and word_start is None:
					words.append(s[i:i+1])
				elif word_start is not None:
					words.append(s[word_start:i + 1])
			else:
				if word_start is None:
					word_start = i
		
		new_string = ''

		while words:
			new_string += words.pop()
			if len(words) > 0:
				new_string += ' '

		return new_string

	def reverseWords_easy(self, s):
		return ' '.join(s.split()[::-1])

sol = Solution()
print("|{}|".format(sol.reverseWords('    ab')))