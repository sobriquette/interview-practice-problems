def max_duffel_bag_value(cakes, capacity):
	max_value_per_capacity = [0] * (capacity + 1)

	max_value_per_capacity[0] = 0
	max_value_per_capacity[1] = 1

	for c in range(capacity + 1):
		curr_max_value = 0

		# if cake weighs 0 but has a positive value,
		# we can fit infinite number of cakes
		for cake_weight, cake_value in cakes:
			if cake_weight == 0 and cake_weight != 0:
				return float('inf')

			# check if we should use the cake
			# if we do use it, we take the current cake value and...
			# add that to the max value obtained from the weight leftover
			if cake_weight <= capacity:
				max_value_using_this_cake = cake_value + max_value_per_capacity[capacity - cake_weight]
				curr_max_value = max(max_value_using_this_cake, curr_max_value)

		# then get the max value for this capacity and add it to our list
		max_value_per_capacity[c] = curr_max_value

	return max_value_per_capacity[capacity]
