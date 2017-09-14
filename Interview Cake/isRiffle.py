def isRiffle_iterative(shuffled_deck, half1, half2):
	if len(shuffled_deck) == 0:
		return True

	half1_index = 0
	half2_index = 0
	half1_end = len(half1) - 1
	half2_end = len(hafl2) - 1

	for card in shuffled_deck:
		if half1_index <= half1_end and half1[half1_index] == card:
			half1_index += 1
		elif half2_index <= half2_end and half2[half2_index] == card:
			half2_index += 1
		else:
			return False
 
	return True

def isRiffle_recursive(shuffled_deck, top_card, half1, half1_index, half2_index, half2):
	if top_card == len(shuffled_deck):
		return True

	if half1_index < len(half1) and half1[half1_index] == shuffled_deck[top_card]:
		half1_index += 1
	elif half2_index < len(half2) and half2[half2_index] == shuffled_deck[top_card]:
		half2_index += 1
	else:
		return False

	top_card += 1
	return isRiffle_recursive(shuffled_deck, top_card, half1, half1_index, half2_index, half2)