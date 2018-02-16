class WordDict:
	def __init__(self):
		self.word_dict = {}

	def process_text(self, text):
		for word in text:
			if word.lower() in self.word_dict:
				self.word_dict[word.lower()] += 1
			else:
				self.word_dict[word.lower()] = 1

	def get_word_count(self, word):
		if word.lower() in self.word_dict:
			return self.word_dict[word.lower()]
		else:
			return 0
