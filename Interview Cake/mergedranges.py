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
