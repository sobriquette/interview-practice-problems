# Solution
class Solution:
	class DocPair:
		def __init__(self, doc1, doc2):
			self.doc1 = d1
			self.doc2 = d2

	def group_words(self, documents):
		words_to_docs = {}

		for doc_id, words in documents:
			for word in words:
				if word in words_to_docs:
					words_to_docs[word].append(doc_id)
				else:
					words_to_docs[word] = [doc_id]

	def increment(self, similarities, doc1, doc2):
		doc_pair = self.DocPair(doc1, doc2)
		if doc_pair not in similarities:
			similarities[doc_pair] = 1.0
		else:
			similarities[doc_pair] += 1

	def compute_intersections(self, words_to_docs):
		words = words_to_docs.keys()
		similarities = {}

		for word in words:
			docs = words_to_docs[word]

			for i in range(len(docs)):
				for j in range(i, len(docs)):
					self.increment(similarities, docs[i], docs[j])

		return similarities

	def update_to_similarity_value(self, documents, similarities):
		for pair, intersection in documents:
			doc1, d1_len = pair.doc1, len(documents[pair.doc1])
			doc2, d2_len = pair.doc2, len(documents[pair.doc2])
			union = intersection / (d1_len + d2_len - intersection)
			similarities[pair] = union

	def compute_similarities(self, documents):
		words_to_docs = self.group_words(documents)
		similarities = self.compute_intersections(words_to_docs)
		self.update_to_similarity_value(documents, similarities)

		return similarities

# Attempt - 30 min
def print_doc_similarity(documents):
	"""
	input: dict{id: set{words}
	output: none
	"""	
	similarity_dict = {}

	ids = dict.keys()
	for id1 in range(len(ids)):
		for id2 in range(id1, len(ids)):
			if (id1, id2) not in similarity_dict:
				doc1_len = len(documents[id1])
				doc2_len = len(documents[id2])
				similarity_dict[(id1, id2)] = [(doc1_len + doc2_len), 0]

	for pair, stats in similarity_dict:
		doc1 = pair[0]
		doc2 = pair[1]

		for word in doc1:
			if word in doc2:
				similarity_dict[pair][1] += 1.0

		intersection = similarity_dict[pair][1]
		total_elems = similarity_dict[pair][0]
		union = total_elems - intersection

		similarity_dict[pair][0] = union
		
		similarity = intersection / union
		if similarity == 0:
			del similarity_dict[pair]
		else:
			similarity_dict[pair] = similarity

	for pair, stats in similarity_dict:
		print("{}, {} : {}".format(pair[0], pair[1], stats))
