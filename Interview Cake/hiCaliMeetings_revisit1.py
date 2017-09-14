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