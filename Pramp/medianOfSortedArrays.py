import math

class Solution(object):
    def isOdd(self, arr):
        return len(arr) & 1

    def calculateMedian(self, arr):
        mid = int((len(arr) - 1) / 2)
        
        if self.isOdd(arr):
            med = arr[mid]
        else:
            med = (arr[mid] + arr[mid + 1]) / float(2)
        return med

    def findMedianSortedArrays(self, nums1, nums2):
        if nums1 == [] and nums2 == []:
            return 0
        elif nums1 == []:
            return self.calculateMedian(nums2)
        elif nums2 == []:
            return self.calculateMedian(nums1)
        else:
            med1 = self.calculateMedian(nums1)
            med2 = self.calculateMedian(nums2)
            total = med1 + med2
            remainder = total % 2

            if remainder < 1:
                return int(total / 2)
            elif remainder == 1:
                return total / float(2)
            elif total % 2 > 1:
                return int(math.ceil(total / 2))
        