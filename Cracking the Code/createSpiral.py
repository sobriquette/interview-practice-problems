# [1    2   3   4   5]
# [6    7   8   9   10]
# [11   12  13  14  15]
# [16   17  18  19  20]
# [21   22  23  24  25]

arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

def printSpiral(arr):
   # return if array is empty
   if arr is None: return

   topRow = leftCol = 0
   botRow = len(arr)
   rightCol = len(arr[0])

   while (topRow < botRow and leftCol < rightCol):
      # top row
      for c in range(leftCol, rightCol):
         print(arr[topRow][c])
      topRow += 1

      # right col
      for r in range(topRow, botRow):
         print(arr[r][rightCol - 1])
      rightCol -= 1

      # bot row
      for c in range(rightCol - 1, leftCol - 1, -1):
         print(arr[botRow - 1][c])
      botRow -= 1

      # left col
      for r in range(botRow - 1, topRow - 1, -1):
         print(arr[r][leftCol])
      leftCol += 1      

printSpiral(arr)
