def buildWordCloud_with_two_DS(data):
	words = data.split(" ")
	word_cloud = {}

	for w in words:
		# remove extraneous punctuation
		# if at end or beginning of word
		if w[len(w)] in '.,:;)]}!?':
			curr = w[:len(w) - 1]
		if w[0] in '({[':
			curr = w[1:]

		# add word to cloud
		if curr.lower() not in word_cloud:
			word_cloud[curr.lower()] = 1
		else:
			word_cloud[curr.lower()] += 1

	return word_cloud

def buildWordCloud(data):
	punctuation = '.,:;)]}!?'
	word_cloud = {}

	l = 0
	while l < len(data):
		# skip to next character if there is punctuation in front of letter
		if data[l] in '({[':
			l += 1

		# find end of word
		end = l
		while not data[end] == ' ':
			end += 1

		# don't include punctuation at end of word
		if data[end] in punctuation:
			word = data[l:end - 1].lower()
		else:
			word = data[l:end].lower()

		# add it to the word cloud
		if word not in word_cloud:
			word_cloud[word] = 1
		else:
			word_cloud[word] += 1
		l += 1

	return word_cloud

# Solution
class WordCloudData:
	def __init__(self, input_string):
		self.word_counts = {}
		self.populate_word_counts(input_string)

	def populate_word_counts(input_string):
		word_start = 0
		word_length = 0

		for i, char in enumerate(input_string):
			# if we are at the end of the input string,
			# check if last char is a letter and add to dict
			if i == len(input_string):
				if char.isalpha():
					word_length += 1
				if word_length > 0:
					curr_word = input_string[word_start : word_start + word_length]
					self.add_word_to_dict(curr_word)
			# if char is a space or emdash, we are at the end of the word
			elif char == ' ' or char == u'\u2014':
				if word_length > 0:
					curr_word = input_string[word_start : word_start + word_length]
					self.add_word_to_dict(curr_word)
					word_length = 0
			# if we reach a . we want to make sure we split ellipses
			# and add the word to the dict
			elif char == '.':
				if i < len(input_string) - 1 and input_string[i + 1] == '.':
					if word_length > 0:
						curr_word = input_string[word_start : word_start + word_length]
						self.add_word_to_dict(curr_word)
						word_length = 0
			# if char is letter or apostrophe, add to our word
			elif char.isalpha() or char == '\'':
				if word_length == 0:
					word_start = i
				word_length += 1
			# if char is a hyphen, check if it surrounded by letters
			# if it is, add as a word
			elif char == '-':
				if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
					if word_length == 0:
						word_start = i

					word_length += 1
				else:
					if word_length > 0:
						curr_word = input_string[word_start : word_start + word_length]
						self.add_word_to_dict(curr_word)
						word_length = 0

	def add_word_to_dict(word):
		if word in self.word_counts:
			self.word_counts += 1
		# if a lowercase word is in the dictionary, our input word is uppercase
		# since we only keep uppercase words if they are always uppercase, we increment lowercase
		elif word.lower() in self.word_counts:
			self.word_counts[word.lower()] += 1
		# if an uppercase word is in the dictionary, our input word is lowercase
		# since we only keep uppercase words if they are always uppercase, we add the lowercase version
		# and add the uppercase version's count to it
		elif word.capitalize() in self.word_counts:
			self.word_counts[word] = 1
			self.word_counts[word] += self.word_counts[word.capitalize()]
			del self.word_counts[word.capitalize()]
		# this word is not in the dictionary yet
		else:
			self.word_counts[word] = 1


