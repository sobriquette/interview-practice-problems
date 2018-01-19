"""
Implementation on attempt #3: 08/09/2017
"""
def merge_ranges(meeting_times):
	sorted_meeting_times = sorted(meeting_times)
	merged = []
	start = sorted_meeting_times[0][0]
	end = sorted_meeting_times[0][1]

	for i in range(1, len(sorted_meeting_times)):
		if end >= sorted_meeting_times[i][0] or end > sorted_meeting_times[i][1]:
			start = min(sorted_meeting_times[i][0], start)
			end = max(sorted_meeting_times[i][1], end)
		else:
			merged.append((start, end))
			start = sorted_meeting_times[i][0]
			end = sorted_meeting_times[i][1]

	merged.append((start, end))
	return merged

def merge_ranges_solution(meetings):
	sorted_meetings = sorted(meetings)
	merged_meetings = [sorted_meetings[0]]

	for curr_start, curr_end in sorted_meetings[1:]:
		last_merged_start, last_merged_end = merged_meetings[-1]

		if curr_start <= last_merged_end:
			merged_meetings[-1] = (last_merged_start, max(last_merged_end, curr_end))
		else:
			merged_meetings.append(curr_start, curr_end)

	return merged_meetings

"""
Implementation on attempt #2: 04/15/2017
"""
def merge_ranges(input_range_list):
    s_ranges = sorted(input_range_list)
    merged = []
    prev_start, prev_end = s_ranges[0][0], s_ranges[0][1]

    for r in range(len(s_ranges) - 1):
        curr_start, curr_end = s_ranges[r + 1][0], s_ranges[r + 1][1]

        if prev_end >= curr_start:
            if curr_end < prev_end:
                prev_end = curr_end
        else:
            merged.append([prev_start, prev_end])
            prev_start, prev_end = curr_start, curr_end
    
    merged.append([prev_start, prev_end])

    return merged

print(merge_ranges([[1, 10], [5, 8], [8, 15]]))
#merge_ranges([[1, 10], [5, 8], [8,15]])

def merged_ranges(times):
    s_times = sorted(times)
    options = []
    first_s, first_e = s_times[0][0], s_times[0][1]
    for t in range(len(s_times) - 1):
        sec_s, sec_e = s_times[t + 1][0], s_times[t + 1][1]
        if first_e >= sec_s:
            if first_e < sec_e:
                first_e = sec_e
        else:
            options.append((first_s, first_e))
            first_s, first_e = sec_s, sec_e

    options.append((first_s, first_e))

    return options


"""
Implementation on attempt #1: 03/28/2017
"""

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