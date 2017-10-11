# Runtime: O(nlogn + (n * k))
# Space: O(n)

def max_duffel_bag_cake_choices(cake_tuples, capacity):
	"""
		Return the maximum monetary value the duffel bag can hold
		type: list of tuples
		rtype: list of tuples
	"""
	# sort the cakes in descending order by highest value
	cakes_sorted = sorted(cake_tuples, key=lambda cake: cake[1], reverse=True)
	max_cake_choices = None

	max_duffel_value = 0

	for i in range(len(cakes_sorted)):
		rem_capacity = capacity
		curr_duffel_value = 0
		curr_cake_choices = []
		j = i

		if cakes_sorted[i][0] > capacity or \
			cakes_sorted[i][0] == 0 and cakes_sorted[i][1] == 0:
				continue

		while rem_capacity > 0 and j < len(cakes_sorted):
			if cakes_sorted[j][0] == 0:
				return (cakes_sorted[j], float('inf'))
			num_of_curr_cakes = rem_capacity // cakes_sorted[j][0]
			curr_duffel_value += num_of_curr_cakes * cakes_sorted[j][1]
			curr_cake_choices.append((cakes_sorted[j], num_of_curr_cakes))
			rem_capacity %= cakes_sorted[j][0]
			j += 1

		if curr_duffel_value > max_duffel_value:
			max_duffel_value = curr_duffel_value
			max_cake_choices = curr_cake_choices

	return max_cake_choices

def max_duffel_bag_value(cake_tuples, capacity):
	"""
		Return the maximum monetary value the duffel bag can hold
		type: list of tuples
		rtype: integer
	"""
	# sort the cakes in descending order by highest value
	cakes_sorted = sorted(cake_tuples, key=lambda cake: cake[1], reverse=True)

	max_duffel_value = 0

	for i in range(len(cakes_sorted)):
		rem_capacity = capacity
		curr_duffel_value = 0
		j = i

		if cakes_sorted[i][0] > capacity or \
			cakes_sorted[i][0] == 0 and cakes_sorted[i][1] == 0:
				continue

		while rem_capacity > 0 and j < len(cakes_sorted):
			if cakes_sorted[j][0] == 0:
				return float('inf')
			num_of_curr_cakes = rem_capacity // cakes_sorted[j][0]
			curr_duffel_value += num_of_curr_cakes * cakes_sorted[j][1]
			rem_capacity %= cakes_sorted[j][0]
			j += 1

		max_duffel_value = max(max_duffel_value, curr_duffel_value)

	return max_cake_choices

if __name__=="__main__":
	cake_tuples = [(7, 160), (3, 90), (2, 15)]
	capacity = 20
	print(max_duffel_bag_value(cake_tuples, capacity))
	print(max_duffel_bag_cake_choices(cake_tuples, capacity))