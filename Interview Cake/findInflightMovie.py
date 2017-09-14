# Using a dictionary
def findInflightMovieDict(flight_length, movie_lengths):
	pairs = {}

	for m in movie_lengths:
		if m in pairs and pairs[m] != m:
			return True
		else:
			pairs[flight_length - m] = m

	return False

# Using a set
def findInflightMovieSet(flight_length, movie_lengths):
	movies = set()

	for m in movie_lengths:
		second = flight_length - m
		if second in movies:
			return True
		else:
			movies.add(m)

	return False

# If total time within X min of flight_length
## NOT SURE IF CORRECT ##
def findInflightMovieAnyLessThan(flight_length, movie_lengths, window):
	movies = set()
	window_low = flight_length - window
	window_high = flight_length + window

	for m in movie_lengths:
		if window_low <= m <= window_high:
			second = flight_length - m
			if second in movies:
				return True
			else:
				movies.add()
		else:
			continue

	return False

# If we wanted any number of movies
def findInflightMovieAnyNumMovies(flight_length, movie_lengths):
	movies = set()
	total_time = 0

	for m in movie_lengths:
		pass