class Movie:
	def __init__(self, movieId,  title, description, genre):
		self._id = movieId
		self._title = title
		self._description = description
		self._genre = genre

	@property
	def id(self):
		return self._id

	@property
	def title(self):
		return self._title

	@property
	def description(self):
		return self._description

	@property
	def genre(self):
		return self._genre

	@id.setter
	def id(self, movieId):
		self._id = movieId

	@title.setter
	def title(self, title):
		self._title = title

	@description.setter
	def description(self, description):
		self._description = description

	@genre.setter
	def genre(self, genre):
		self._genre = genre

	def __eq__(self, other):
		return self._id == other._id and self._title == other._title and self._description == other._description and self._genre == other._genre

	def __str__(self):
		return "ID: " + str(self._id) + "    Title: " + self._title + "     Description: " + self._description + "     Genre: " + self._genre
