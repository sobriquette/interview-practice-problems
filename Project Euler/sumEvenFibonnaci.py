maxNum = int(input("Enter ceiling for sum: "))

# From StackOverflow, using generators
# Calculates fibonacci sequence
def fib(maxNum):
	a, b = 0, 1
	while b <= maxNum:
		yield a
		a, b = b, a + b

def getEvenFibSum(maxNum):
	evenSum = 2
	prev = 2
	curr = 3

	if maxNum <= 1:
		return 0
	elif maxNum == 2:
		return 2
	else:
		while (curr < maxNum):
			if curr % 2 == 0:
				evenSum += curr
			prev, curr = curr, prev + curr
		return evenSum


if __name__=="__main__":
	# for i in evenFib(maxNum):
	# 	print(i)
	print(getEvenFibSum(maxNum))


