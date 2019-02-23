class TransferMovieDays:
	def __init__(self, movie, days):
		self._movie = movie
		self._days = days

	@property
	def movie(self):
		return self._movie

	@property
	def days(self):
		return self._days

	def __str__(self):
		return str(self._days) + " " * (30 - len(str(self._days))) + str(self._movie)


class TransferMovieNumber:
	def __init__(self, movie, no):
		self._movie = movie
		self._no = no

	@property
	def movie(self):
		return self._movie

	@property
	def number(self):
		return self._no

	def __str__(self):
		return str(self._no) + " " * (30 - len(str(self._no))) + str(self._movie)

