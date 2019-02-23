import datetime

class Rental:
	def __init__(self, rentalId, movie, client, rentedDate, dueDate, returnedDate = datetime.date(1, 1, 1)):
		self._rentalId = rentalId
		self._movie = movie
		self._client = client
		self._rentedDate = rentedDate
		self._dueDate = dueDate
		self._returnedDate = returnedDate

	def __eq__(self, other):
		return self._rentalId == other._rentalId and self._movie == other._movie and self._client == other._client \
				and self._rentedDate == other._rentedDate and self._dueDate == other._dueDate \
				and self._returnedDate == other._returnedDate

	def __str__(self):
		if self._returnedDate == datetime.date(1, 1, 1):
			returnValue = "It was not returned"
		else:
			returnValue = str(self._returnedDate)
		return "ID: " + str(self._rentalId) + ", Movie: " + str(self._movie._id) + ", Client: " +\
			str(self._client.id) + ", Rented date: "+ str(self._rentedDate) + ", Due date: " + str(self._dueDate) + ", ReturnedDate: " + returnValue

	@property
	def movie(self):
		return self._movie

	@property
	def rental_id(self):
		return self._rentalId

	@property
	def client(self):
		return self._client

	@property
	def rentedDate(self):
		return self._rentedDate

	@property
	def returnedDate(self):
		return self._returnedDate

	@returnedDate.setter
	def returnedDate(self, returnedDate):
		self._returnedDate = returnedDate

	@property
	def dueDate(self):
		return self._dueDate

