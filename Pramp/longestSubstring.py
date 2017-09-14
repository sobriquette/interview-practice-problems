def lengthOfLongestSubstring(s):
    unique = {}
    end = maxLen = 0
    
    for index, c in enumerate(s):
        if c in unique and end <= unique[c]:
            end = unique[c] + 1
        else:
            unique[c] = index
            maxLen = max(maxLen, i - end + 1)

    return maxLen

print(lengthOfLongestSubstring("c"))