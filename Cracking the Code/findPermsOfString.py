class SolutionCTCI:
	def find_perms(string):
		if string.strip() == '':
			return None

		perms = []

		if len(string) == 0:
			perms.append('')

		curr_char = string[0]
		rest = string[1:]

		for w in find_perms(rest):
			for i in range(len(w) + 1):
				s = insert_char(w, curr_char, i)
				perms.append(s)

		return perms

	def insert_char(word, char, idx):
		return word[:idx] + char + word[idx:]

class MySolution:
	def find_perms(s):
		if s.strip() == '':
			return None

		return find_perms_util(s, len(s) - 1, all_perms, uniq_perms)

	def find_perms_util(s, idx, all_perms):
		all_perms = []
		
		if idx == 0:
			all_perms.append('')

		curr_char = s[idx]

		for word in find_perms_util(s, idx - 1, all_perms):
			for i in range(len(word) + 1):
				all_perms.append(word[:i] + curr_char + word[i:])

		return all_perms