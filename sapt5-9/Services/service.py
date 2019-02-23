from Domain.Client import Client
from Domain.Movie import Movie
from Domain.Rental import Rental
import datetime, re, operator
from Services.transferClient import *
from Services.transferMovie import *
from Domain.validatorMovie import ValidatorMovie
from Services.undoRedo import *

class Services():
	def __init__(self, clientRepo, movieRepo, rentalRepo):
		self._clientRepo = clientRepo
		self._movieRepo = movieRepo
		self._rentalRepo = rentalRepo
		self._UndoService = UndoService()

	@property
	def clientRepo(self):
		return self._clientRepo

	@property
	def movieRepo(self):
		return self._movieRepo

	@property
	def rentalRepo(self):
		return self._rentalRepo

	def addClient(self, an_id, name):
		'''
		Adds a client to the list of clients
		Input: an_id - int
			   name - string
		Output: Adds a client to the client list
		'''
		undo = FunctionCall(self.removeClient, an_id)
		redo = FunctionCall(self.addClient, an_id, name)
		op = Operation(undo, redo)
		self._UndoService.addOperation(op)
		self._clientRepo.add(Client(an_id, name))

	def addMovie(self, an_id, title, desc, gen):
		'''
		Adds a movie to the list of movies
		Input: an_id - int
			   title, desc, gen - string
		Output: Adds a movie to the movie list
		'''
		ValidatorMovie.validator(Movie(an_id, title, desc, gen))
		undo = FunctionCall(self.removeMovie, an_id)
		redo = FunctionCall(self.addMovie, an_id, title, desc, gen)

		op = Operation(undo, redo)
		self._UndoService.addOperation(op)
		self._movieRepo.add(Movie(an_id, title, desc, gen))

	def removeClient(self, an_id):
		'''
		Removes a client from the client list
		Input: an_id - int
		Output: Removes a client from the client list
		'''

		self._clientRepo.remove(an_id)
		self._rentalRepo.removeRentalWithClientID(an_id)

	def removeMovie(self, an_id):
		'''
		Removes a movie from the movie list
		Input: an_id - int
		Output: Removes a movie from the movie list
		'''

		self._movieRepo.remove(an_id)
		self._rentalRepo.removeRentalWithMovieID(an_id)

	def updateClient(self, name, indx):
		'''
		Replaces the name of a client with a new one
		Input: name - string
			   indx - int
		Output: Replaces the name of the client with the ID <indx> with <name> or raises an error
		'''
		pos = self._clientRepo.findPosByID(indx)
		if pos == -1:
			print("ID not found")
		if name == '':
			print("Name not in the corect format")
		self._clientRepo.getList()[pos].name = name

	def updateMovie(self, indx, inputt, op):
		'''
		Updates a movie's details
		Input: indx - int
			inputt - string (represents the title, desc or genre)
			op - int (1 for title, 2 for desc, 3 for genre)
		Output: Updates a movie's details or raises an error
		'''
		pos = self._movieRepo.findPosByID(indx)
		if pos == -1:
			print("ID not found")
		if inputt == '':
			print("Name not in the corect format")
		if op == 1:
			self._movieRepo.getList()[pos].title = inputt
		elif op == 2:
			self._movieRepo.getList()[pos].desc = inputt
		elif op == 3:
			self._movieRepo.getList()[pos].genre = inputt

	def rentMovie(self, rentDate_raw, dueDate_raw, rID, mID, cID):
		'''
		Rents a movie (add a rental to the rental list)
		Input: rentDate_raw - string
			   dueDate_raw - string
			   rID, mID, cID - int
		Output: adds a rental to the rental list or returns an error
		'''
		rentDate = rentDate_raw.split('/')[:]
		dueDate = dueDate_raw.split('/')[:]
		if len(rentDate) != 3 or len(dueDate) != 3:
			raise SyntaxError("Invalid date")
		client = self._clientRepo.findObj(cID)
		movie = self._movieRepo.findObj(mID)
		try:
			rent1 = int(rentDate[0])
			rent2 = int(rentDate[1])
			rent3 = int(rentDate[2])
			due1 = int(dueDate[0])
			due2 = int(dueDate[1])
			due3 = int(dueDate[2])
		except ValueError:
			raise ValueError("Invalid date")
		r = Rental(rID, movie, client, datetime.date(rent1, rent2, rent3), datetime.date(due1, due2, due3))
		self._rentalRepo.add(r)

	def returnMovie(self, returnDate_raw, mID):
			'''
			Returns a movie (sets the return date of a rental)
			Input: returnDate_raw - string
				   rID - int
			Output: sets the return date of a movie in the rental list (the rental has the ID <rID>) or raises an error
			'''
			if returnDate_raw == 'today':
				returnDate = [datetime.date.today().year, datetime.date.today().month, datetime.date.today().day]
			else:
				returnDate = returnDate_raw.split('/')[:]
			if len(returnDate) != 3:
				raise SyntaxError("Invalid date")
			#retDate = datetime.date(int(returnDate[0]), int(returnDate[1]), int(returnDate[2]))
			for rental in self._rentalRepo.getList():
				if rental._rentalId == mID:
					date = datetime.date(int(returnDate[0]), int(returnDate[1]), int(returnDate[2]))
					self._rentalRepo.returnMovie(mID, date)

	@staticmethod
	def checkExistingID(repo, an_id):
		'''
		Checks if an object is already in a repository (client or movie)
		Input: repo - Repository
			   an_id - int
		Output: True if that ID is already the ID of an object in repo
		'''
		for obj in repo.getList():
			if obj.id == an_id:
				return True
		return False

	def searchClientsBy(self, inputt, op):
		'''
		Searches clients by ID or name (partial string matching and case insensitive)
		Input: inputt - string
			   op - int (1 for ID, 2 for name)
		Output: res - list of Client objects
		'''
		res = []
		for client in self._clientRepo.getList():
			if op == 1:
				if re.search(inputt.lower(), str(client.id)) != None:
					res.append(client)
			if op == 2:
				if re.search(inputt.lower(), client.name.lower()):
					res.append(client)
		return res

	def searchMoviesBy(self, inputt, op):
		'''
		Searches movies by ID, title, description or genre (partial string matching and case insensitive)
		Input: inputt - string
			   op - int (1 for ID, 2 for title, 3 for description, 4 for genre)
		Output: res - list of Movie objects
		'''
		res = []
		for movie in self._movieRepo.getList():
			if op == 1:
				if re.search(inputt.lower(), str(movie.id)) != None:
					res.append(movie)
			if op == 2:
				if re.search(inputt.lower(), movie.title.lower()):
					res.append(movie)
			if op == 3:
				if re.search(inputt.lower(), movie.desc.lower()):
					res.append(movie)
			if op == 4:
				if re.search(inputt.lower(), movie.genre.lower()):
					res.append(movie)
		return res

	def mostRentedMoviesByNumber(self):
		'''
		Generates the list of most rented movies by the number of rentals
		Input: -
		Output: result - list of Movie objects
		'''
		statistic = {}
		for rental in self._rentalRepo.getList():
			if rental.movie.id not in statistic.keys():
				statistic[rental.movie.id] = 1
			else:
				statistic[rental.movie.id] += 1
		for movie in self._movieRepo.getList():
			if movie.id not in statistic.keys():
				statistic[movie.id] = 0
		result = sorted(statistic.items(), key=operator.itemgetter(1))
		result.reverse()
		result1 = []
		for item in result:
			result1.append(TransferMovieDays(self.movieRepo.findObj(item[0]), item[1]))
		return result1

	def mostRentedMoviesByDays(self):
		'''
		Generates the list of most rented movies by the number of days they were rented
		Input: -
		Output: result - list of Movie objects
		'''
		today = datetime.date.today()
		statistic = {}
		for rental in self._rentalRepo.getList():
			if rental.movie.id not in statistic.keys():
				if rental.returnedDate == datetime.date(1, 1, 1):
					statistic[rental.movie.id] = (
								datetime.date(today.year, today.month, today.day) - rental.rentedDate).days
				else:
					statistic[rental.movie.id] = (rental.returnedDate - rental.rentedDate).days
			else:
				if rental.returnedDate == datetime.date(1, 1, 1):
					statistic[rental.movie.id] += (
								datetime.date(today.year, today.month, today.day) - rental.rentedDate).days
				else:
					statistic[rental.movie.id] += (rental.returnedDate - rental.rentedDate).days
		for movie in self._movieRepo.getList():
			if movie.id not in statistic.keys():
				statistic[movie.id] = 0
		result = sorted(statistic.items(), key=operator.itemgetter(1))
		result.reverse()
		result1 = []
		for item in result:
			result1.append(TransferMovieDays(self.movieRepo.findObj(item[0]), item[1]))
		return result1

	def clientsWithMostRentedDays(self):
		'''
		Generates the list of most active clients (ordered by the number of days of their rentals)
		Input: -
		Output: result - list of Client objects
		'''
		today = datetime.date.today()
		statistic = {}
		for rental in self._rentalRepo.getList():
			if rental.client.id not in statistic.keys():
				if rental.returnedDate == datetime.date(1, 1, 1):
					statistic[rental.client.id] = (
								datetime.date(today.year, today.month, today.day) - rental.rentedDate).days
				else:
					statistic[rental.client.id] = (rental.returnedDate - rental.rentedDate).days
			else:
				if rental.returnedDate == datetime.date(1, 1, 1):
					statistic[rental.client.id] += (
								datetime.date(today.year, today.month, today.day) - rental.rentedDate).days
				else:
					statistic[rental.client.id] += (rental.returnedDate - rental.rentedDate).days
		for client in self._clientRepo.getList():
			if client.id not in statistic.keys():
				statistic[client.id] = 0
		result = sorted(statistic.items(), key=operator.itemgetter(1))
		result.reverse()
		result1 = []
		for item in result:
			result1.append(TransferClient(self.clientRepo.findObj(item[0]), item[1]))
		return result1

	def rentedMovies(self):
		'''
		Generates the list of currently rented movies
		Input: -
		Output: statistic - list of Movie objects
		'''
		statistic = []
		for rental in self._rentalRepo.getList():
			if rental.returnedDate == datetime.date(1, 1, 1):
				statistic.append(rental.movie)
		return statistic

	def undo(self):
		if self._UndoService.undo() == False:
			raise ValueError("No more undos")

	def redo(self):
		if self._UndoService.redo() == False:
			raise ValueError("No more redos")