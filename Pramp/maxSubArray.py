def maxSubArray(nums):
    curr_max = nums[0]
    curr_sum = 0
    for index, n in enumerate(nums):
        curr_sum += n
        
        if curr_sum > curr_max:
            curr_max = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    
    return curr_max

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])