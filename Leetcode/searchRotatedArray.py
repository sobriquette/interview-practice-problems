# Implement a modified binary search
# to maintain O(logn) time complexity
def search(nums, target):
    start, end = 0, len(nums) - 1
    mid = len(nums) // 2
    
    while start <= end:
        if target == nums[mid]:
            return mid
        elif nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
                
        mid = (start + end) // 2
    
    return -1

if __name__=="__main__":
    nums = [7,9,10,0,1,2,5]

    while True:
        target = input("enter a number to search for: ")
        
        if target == "q" or target == "quit":
            break
        
        print(search(nums, int(target)))
