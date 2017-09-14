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

####		http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/ 	####
#### 		To calculate size of bit array, m 							   		####
#### 		m = ( n * ln(p) // (ln(2))^2 )										####
#### 		To calculate the number of hashes to use, k 					  	####
####		k = - ( (m / n) * ln(2) )											####
