list1, list2 = input("enter values in first array: ").split(), input("enter values in second array: ").split()

print (" ".join([str(i) for i in list1 if i in list2]))