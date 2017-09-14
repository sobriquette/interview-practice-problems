def get_max_profit(stock_prices_yesterday):
	if len(stock_prices_yesterday) < 2:
		raise IndexError('need at least two stock prices to make a profit')

	lowest_price = stock_prices_yesterday[0]
	max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

	for time, current_price in enumerate(stock_prices_yesterday):
		# can't sell at the same time we buy (which is the initial lowest_price)
		if time == 0:
			continue

		potential_profit = current_price - lowest_price

		max_profit = max(max_profit, potential_profit)
		lowest_price = min(lowest_price, current_price)

	return max_profit
