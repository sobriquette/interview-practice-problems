
if __name__=="__main__":
	T = int(input())

	for i in range(1, T + 1):
		inputs = input().split(" ")
		
		pancakes, k = inputs[0], int(inputs[1])
		print("Case #{}: {}".format(i, flipPancakes(pancakes, k)))