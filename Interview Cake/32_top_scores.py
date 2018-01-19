"""
Implementation on attempt #2: 01/18/2018
"""
def top_scores(unsorted_scores, highest_possible_score):
	scores_by_count = [0 for _ in range(highest_possible_score + 1)]

	# populate scores with unsorted_scores
	for score in unsorted_scores:
		scores_by_count[score] += 1
	
	final_scores = []
	for score in range(len(scores_by_count) - 1, -1, -1):
		count = scores_by_count[score]

		for i in range(count + 1):
			final_scores.append(score)

	return final_scores

"""
Implementation on attempt #1: 08/07/2017
"""
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