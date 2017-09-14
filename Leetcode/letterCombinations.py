# Time: O(n * 4^n)
# Space: O(4^n) where n is the number of digits

# An iterative solution
class Solution:
	def letterCombinations(self, digits):
		if not digits:
			return []

		keypad = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		results = [""]

		for digit in digits:
			# grab the choices of letters we have
			letters = keypad[int(digit)]
			num_letters, num_results = len(letters), len(results)

			# add placeholders based on the previous set of choices
			# that will be added onto with our current set of letters
			results += [results[i % num_results] for i in range(num_results, (num_letters * num_results))]

			for i in range(num_letters * num_results):
				results[i] =  results[i] + letters[i // num_results]

		return results

# A recursive solution
class Solution2:
	def letterCombinations(self, digits):
		if not digits:
			return []

		keypad = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		results = []

		self.letterCombinationsHelper(results, digits, keypad, "", 0)
		return results

	def letterCombinationsHelper(self, results, digits, keypad, curr, n):
		if n == len(digits):
			results.append(curr)
		else:
			for letter in keypad[int(digits[n])]:
				self.letterCombinationsHelper(results, digits, keypad, curr + letter, n + 1)

print(sorted(Solution2().letterCombinations("234")) == sorted(Solution().letterCombinations("234")))