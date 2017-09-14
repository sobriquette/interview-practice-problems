maxNum = input("Please enter the number up to which you want to find the sum: ")

def sumMultiples(maxNum):
	sum = 0
	for i in range(maxNum):
		if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
			sum += i

	return sum

print(sumMultiples(maxNum))