import functools

maxNum = int(input("Enter the number up to which you want to find the sum: "))
last = maxNum + 1

def squareNums(maxNum):
	return map(lambda x: x**2, range(1, last))

def reduceNumsToSum(nums):
	return functools.reduce(lambda x, y: x + y, nums) 

if __name__ == "__main__":
	sumOfSq = reduceNumsToSum(squareNums(maxNum))
	sqOfSum = reduceNumsToSum(range(1, last))**2
	print(sqOfSum - sumOfSq)