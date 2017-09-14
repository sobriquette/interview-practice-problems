# package: {limit: 4, arr: [3 7 1 9] --> [1 3 7 9]}
# find: two indices of two items exactly equal to limit
# output: (0, 2), or -1 if none found

###################################################
# Approach 1:
# Loop through each item in array
# and check all items after it to see if a pair
###################################################
# Runtime: O(n^2)
# Space: O(n)

def findWeights1(limit, arr):
   sorted_weights = sorted(arr)
   end = limit + 1
   for i in range(end):
      j = i + 1
      while sorted_weights[j] <= limit and j < end:
         curr_sum = sorted_weights[j] + sorted_weights[i]
         if curr_sum == limit:
            return [i, j]
         j += 1
   
   return -1

###################################################
# Approach 2:
# 1. Sort list and perform a binary search 
#    to determine which part of array to look in.
# 2. Then search up to 1/2 the remaining array
#    to find pairs.
###################################################
# Runtime: O(nlogn)

def binarySearch(limit, arr):
   start = 0
   end = len(arr) - 1

   while arr[end] > limit:
      mid = start + (end - start + 1) // 2
      if arr[mid] > limit:
         end = mid - 1
         mid = (start + end) // 2
      else:
         return arr[:mid + 1]

   return arr[:end + 1]

def findWeights2(limit, arr, original):
   # only need to search halfway
   end = len(arr)//2 + 1

   for i in arr[:end]:
      if (limit - i) in arr:
         return [original.index(i), original.index(limit - i)]

   return -1

###################################################
# Approach 3:
# 1. Use a dictionary, where the weight is the key
#    and the value is the index
# 2. Iterate through the list of weights
# 3. If a weight already exists in the dict,
#    return the index of that weight and the pair's
# 4. Else hash the complement of weight, using
#    the complement as key and index as value
###################################################
# Runtime: O(n)
# Space: O(m)

def findWeightsHash(limit, arr):
   pairs = {}

   for index, weight in enumerate(arr):
      if weight in pairs:
         return pairs[weight], index
      else:
         pairs[limit - weight] = index

   return -1


if __name__=="__main__":
   limit = 5
   weights = [3, 7, 1, 9, 2, 6, 4]
   # sorted_weights = sorted(weights)
   # relevant_weights = binarySearch(limit, sorted_weights)
   # print(findWeights(limit, relevant_weights, weights))
   print(findWeightsHash(limit, weights))