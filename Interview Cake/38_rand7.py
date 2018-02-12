def rand7():
	while True:
		n1 = rand5()
		n2 = rand5()

		outcome = (n1 - 1) * 5 + (n2 - 1) + 1

		if outcome > 21:
			continue
			
		return outcome % 7 + 1