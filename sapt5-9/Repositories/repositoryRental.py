from Domain import *
import datetime


class repositoryRental():
	def __init__(self, clientRepo, movieRepo):
		self._list = []
		self._clientRepo = clientRepo
		self._movieRepo = movieRepo

	def getList(self):
		return self._list

	def add(self, rental):
		ok = 0
		for i in range(0, len(self._list) - 1):
			if self._list[i].rental_id < rental.rental_id < self._list[i + 1].rental_id:
				self._list.insert(i + 1, rental)
				ok = 1
		if ok == 0:
			self._list.append(rental)

	def findByID(self, an_id):
		for rental in self._list:
			if an_id == rental.rental_id:
				return True
		return False

	def findByClientID(self, cID):
		for rental in self._list:
			if cID == rental.client.id:
				return True
		return False

	def getObjByID(self, an_id):
		for rental in self._list:
			if an_id == rental.rental_id:
				return rental
		return None

	def findByMovieID(self, an_id):
		for rental in self._list:
			if an_id == rental.movie.id:
				return True
		return False

	def isReturned(self, mID):
		for rental in self._list:
			if mID == rental.movie.id and rental.returnedDate == datetime.date(1, 1, 1):
				return False
		return True

	def removeRentalWithClientID(self, cID):
		i = 0
		for rental in self._list:
			if rental.client.id == cID:
				del self._list[i]
			i += 1

	def removeRentalWithMovieID(self, mID):
		i = 0
		for rental in self._list:
			if rental.movie.id == mID:
				del self._list[i]
			i += 1

	def deleteRental(self, rental):
		i = -1
		for r in self._list:
			i += 1
			if r == rental:
				del self._list[i]
				return

	def returnMovie(self, mID, returnedDate):
		for rental in self._list:
			if rental._rentalId == mID and rental.returnedDate == datetime.date(1, 1, 1):
				rental.returnedDate = returnedDate