"""
Implementation on attempt #3: 01/18/2018
"""
class TrieNode:
	def __init__(self, data):
		self.data = data
		self.children = {}

class Trie:
	def __init__(self):
		self.head = TrieNode('*')

	def insert(self, data):
		node = self.head

		for d in data:
			if d in node.children:
				node = node.children[d]
			else:
				node.children[d] = TrieNode(d)
				node = node.children[d]

		# add flag for end of data
		node.children['*'] = '*'

"""
Implementation on attempt #2: 07/27/2017
"""
from bitarray import bitarray
import mmh3

class BloomFilter:

	def __init__(self, size, hash_count):
		self.size = size
		self.hash_count = hash_count
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self, string):
		for seed in range(self.hash_count):
			result = mmh3.hash(string, seed) % self.size
			self.bit_array[result] = 1

	def lookup(self, string):
		for seed in range(self.hash_count):
			result = mmh3.hash(string, seed) % self.size
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"

"""
http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/
To calculate size of bit array, m 							   		
m = ( n * ln(p) // (ln(2))^2 )										
To calculate the number of hashes to use, k 					  	
k = - ( (m / n) * ln(2) )											
"""

"""
Implementation on attempt #1: 07/25/2017
"""
def reduceURLList(urls):
	triple_w = 'www.'
	url_dict = {}
	url_dict[triple_w] = {}

	for u in urls:
		if u[0:4] == triple_w:
			if u[4] in url_dict[triple_w]:
				url_dict[triple_w][u[4]].append(u[5:])
			else:
				url_dict[triple_w][u[4]] = u[5:]
		else:
			if u[0] in url_dict:
				url_dict[u[0]].append(u[1:])
			else:
				url_dict[u[0]] = u[1:]

	return url_dict