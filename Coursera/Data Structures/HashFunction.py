"""
Implementations of simple hashing algorithms.

The one-at-a-time hash reaches avalanche quickly,
(i.e. changing a single bit produces a wildly different hash).
"""
def fnv_hash(key, key_len, fnv_offset_basis, fnv_prime):
	h = fnv_offset_basis
	for i in range(key_len):
		h = (h * fnv_prime) ^ key[i]

	return h

def oat_hash(key, key_len):
	h = 0

	for i in range(key_len):
		h += key[i]
		h += h << 10
		h ^= h >> 6

	h += h << 3
	h ^= h >> 11
	h += h << 5

	return h
