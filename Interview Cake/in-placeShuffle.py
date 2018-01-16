import random as r
def shuffle_deck(cards):
	deck_size = 52
	for i in range(deck_size):
		swap_idx = r.randint(i, deck_size - 1)
		if swap_idx != i:
			cards[i], cards[swap_idx] = cards[swap_idx], cards[i]