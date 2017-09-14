def rankPlayers(unsorted_scores, highest_possible_score):
	sorted_scores = []
	rankings = [0] * highest_possible_score

	# update rankings array
	for s in unsorted_scores:
		rankings[s] += 1

	# return valid rankings in sorted order
	for i in range(len(rankings) - 1, -1, -1):
		# i reflects the players' scores
		# if multiple players share the same score,
		# we add them n times
		for n in range(rankings[i]):
			sorted_scores.append(i)

	return sorted_scores

# runtime: O(2n)
# space: O(n)