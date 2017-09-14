def computeC(n):
    c, c0, c1 = n, 0, 0
    print("c: {} and c0: {} and c1: {}".format(bin(c), bin(c0), bin(c1)))
    while c&1 == 0 and c != 0:
            c0 += 1
            print("c0: {}".format(bin(c0)))
            c >>= 1
            print("c: {}".format(bin(c)))
            print("c&1: {}".format(bin(c&1)))
    while c&1 == 1:
            c1 += 1
            print("c1: {}".format(bin(c1)))
            c >>= 1
            print("c: {}".format(bin(c)))
    return [c, c0, c1]


if __name__ == "__main__":
	n = int(input("enter the number to compute trailing 0 and 1: "))
	print(computeC(n))