def build_word_cloud(sentence):
	word_dict = {}
	punctuation = (',', '.', ':', ';', '(', ')', '?', '!', '"')
	word_start = 0

	for idx, char in enumerate(sentence):
		if char == ' ' or char in punctuation:
			if word_start is not None:
				word = sentence[word_start:idx]
				
				if 	word.lower() not in word_dict and \
					word.title() not in word_dict:
					word_dict[word] = 1
				elif word.lower() in word_dict:
					word_dict[word.lower()] += 1
				elif word.title() in word_dict:
					word_dict[word.title()] += 1
				
				word_start = None
		elif char.isalnum():
			if word_start is None:
				word_start = idx

	return word_dict

sentence = 'We came, we saw, we conquered...then we ate Bill\'s (Mille-Feuille) cake.'
print(build_word_cloud(sentence))

