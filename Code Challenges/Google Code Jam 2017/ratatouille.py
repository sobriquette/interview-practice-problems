def isValidKit(num_packages, required, ingredients):
	for i in range(num_packages):
		if required[i] < ingredients[i]:
			return False
		else:	
			pass



if __name__=="__main__":
	T = int(input())

	for i in range(1, T + 1):
		num_ingredients, num_packages = input().split()
		required = dict(map(int,))
		ingredients = []
		for j in range(int(num_ingredients)):
			ingredients.append(list(map(int, input().split())))
		#print("Case #{}: {}".format(i, isValidKit(num_packages, required, ingredients)))