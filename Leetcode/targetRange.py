class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(n):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= n:
                    high = mid
                else:
                    low = mid + 1
            return low
        low = search(target)
        return [low, search(target+1)-1] if target in nums[low:low+1] else [-1, -1]