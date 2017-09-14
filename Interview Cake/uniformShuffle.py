import random

def get_random(floor, ceiling):
	return random.randrange(floor, ceiling + 1)

def uniformShuffle(items):
	if len(items) <= 1:
		return items

	last_index = len(items) - 1

	for index_we_are_choosing in range(len(items) - 1):
		# choose a random not-yet-placed item to place there
		# (could also be item already in the spot)
		# must be an item AFTER the current item
		# because stuff before is already placed
		random_index = get_random(index_we_are_choosing_for, last_index)

		if random_index != index_we_are_choosing_for:
			items[index_we_are_choosing_for], items[random_index] = items[random_index], items[index_we_are_choosing_for]

	return items
