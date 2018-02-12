def is_riffle(shuffled_deck, half1, half2):
	idx1, idx2 = 0, 0
	max_half1, max_half2 = len(half1) - 1, len(half2) -1

	for card in shuffled_deck:
		if idx1 <= max_half1 and card == half1[idx1]:
			idx1 += 1
		elif idx2 <= max_half2 and card == half2[idx2]:
			idx2 += 1
		else:
			return False

	return True