def find_duplicate_spaceEd2(arr):
	n = len(arr) - 1
	position_in_cycle = n + 1

	for i in range(n):
		position_in_cycle = arr[position_in_cycle - 1]

	saved_position = position_in_cycle
	curr_position = arr[position_in_cycle - 1]
	cycle_length = 1

	while curr_position != saved_position:
		curr_position = arr[curr_position - 1]
		cycle_length += 1


	curr = n + 1
	nxt = n + 1

	for i in range(cycle_length):
		nxt = arr[nxt - 1]

	while nxt != curr:
		curr = arr[curr - 1]
		nxt = arr[nxt - 1]

	return curr