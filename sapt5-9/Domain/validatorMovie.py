from Domain.Movie import Movie

class ValidatorMovie:
	"""
	Valides if a movie has all fields corectly added.
	"""
	@staticmethod
	def validator(movie):
		if isinstance(movie, Movie) is False:
			raise TypeError("It is not a movie!")

		_errors = []
		if type(movie.id) != int:
			_errors.append("Not an integer.")

		if movie.title == '':
			_errors.append("Title is missing.")

		if movie.genre == '':
			_errors.append("Genre is missing.")

		if movie.description == '':
			_errors.append("Description error.")

		if len(_errors) > 0:
			index = 0
			while index < len(_errors):
				print(_errors[index])
				index += 1
