# Add a feature to a calendar tool to see times in a day when everyone is available
# Return a list of tuples that merges given time ranges together
# availabilities = [(1,3), (2,4)]
# options = [(1, 4)]

def merged_ranges(times):
	# Sort first so we don't have to worry 
	# about a meeting at n - k that breaks our constraint
	s_times = sorted(times)
	# The availabilities based on meeting times
	options = []
	# Start at the first meeting time
	first_s, first_e = s_times[0][0], s_times[0][1]
	for t in range(len(s_times) - 1):
		# Use next meeting time
		sec_s, sec_e = s_times[t + 1][0], s_times[t + 1][1]
		# We can merge if the end time of the first meeting
		# is greater than the start time of the second meeting
		if first_e >= sec_s:
			if first_e < sec_e:
				first_e = sec_e
		else:
			# We will run through all meetings until they no longer
			# satisfy the if condition above.
			# Then we add it as an option
			options.append((first_s, first_e))
			# Update after we have finished merging
			first_s, first_e = sec_s, sec_e

	# Append the very last set
	options.append((first_s, first_e))

	return options

# Runtime: O(nlogn + n)
# Space: O(4n)

if __name__=="__main__":
	# times = [(0,1), (3,5), (4,8), (10, 12), (9,10), (2, 4), (11, 12)]
	#times = [(1,10), (2,6), (3,5), (7,9)]
	times = [[1, 10], [5, 8], [8, 15]]
	print(merged_ranges(times))