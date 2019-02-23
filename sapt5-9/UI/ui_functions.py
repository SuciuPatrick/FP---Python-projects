class UI:
	def __init__(self, service):
		self._service = service

	@property
	def service(self):
		return self._service


	def printClientList(self):
		for client in self._service.clientRepo.getList():
			print(str(client))


	def printMovieList(self):
		for movie in self._service.movieRepo.getList():
			print(str(movie))


	def printRentalList(self):
		for rental in self._service.rentalRepo.getList():
			print(str(rental))


	def showMenu(self):
		print("-" * 17 + "Clients operations" + "-" * 17)
		print("    1. Show the list of clients")
		print("    2. Add a client")
		print("    3. Remove a client")
		print("    4. Update a client's name")
		print("-" * 17 + "Movies operations" + "-" * 17)
		print("    5. Show the list of movies")
		print("    6. Add a movie")
		print("    7. Remove a movie")
		print("    8. Update a movie's info")
		print("-" * 17 + "Rentals operations" + "-" * 17)
		print("    9. Show the rental list")
		print("    10. Rent a movie")
		print("    11. Return a movie")
		print("-" * 17 + "Search operation" + "-" * 17)
		print("    12. Search a client")
		print("    13. Search a movie")
		print("-" * 17 + "Statistics operation" + "-" * 17)
		print("    14. Most rented movies")
		print("    15. Most active clients")
		print("    16. Currently rented movies")
		print("-" * 17 + "Undo/Redo" + "-" * 17)
		print("    17. Undo")
		print("    18. Redo")
		print("0. Exit")

	def showSearchClientMenu(self):
		print("1. ID")
		print("2. Name")

	def showUpdateMovieMenu(self):
		print("1. Title")
		print("2. Description")
		print("3. Genre")

	def showSearchMovieMenu(self):
		print("1. ID")
		print("2. Title")
		print("3. Description")
		print("4. Genre")

	def readOption(self):
		return int(input("Choose one from the options above: "))

	def invalidOption(self):
		print("Something has to go there")


	def addClientUI(self):
		try:
			an_id = int(input("ID: "))
		except ValueError:
			print("ID must be a number")
			raise ValueError("")
		name = input("Name: ")
		try:
			self._service.addClient(an_id, name)
		except ValueError as ve:
			print(ve)
			raise ValueError("")


	def addMovieUI(self):
		an_id = int(input("ID: "))
		title = input("Title: ")
		desc = input("Description: ")
		gen = input("Genre: ")
		try:
			self._service.addMovie(an_id, title, desc, gen)

		except ValueError as ve:
			print(ve)
			raise ValueError("")

	def removeClientUI(self):
		try:
			an_id = int(input("Which ID to remove: "))
			self._service.removeClient(an_id)
		except ValueError:
			print("ID must be a number")
			raise ValueError("")


	def removeMovieUI(self):
		try:
			an_id = int(input("Which ID to remove: "))
		except ValueError:
			print("ID must be a number")
			raise ValueError("")
		try:
			self._service.removeMovie(an_id)
		except SyntaxError as se:
			raise SyntaxError(se)


	def updateClientUI(self):
		try:
			indx = int(input("Which client do you want to modify? "))
		except ValueError:
			print("ID must be a number")
			raise ValueError("")
		name = input("Name: ")
		try:
			self._service.updateClient(name, indx)
		except SyntaxError as se:
			print(se)
			raise SyntaxError("")


	def updateMovieUI(self):
		try:
			indx = int(input("Which movie do you want to modify? "))
		except ValueError:
			print("ID must be a number")
			raise ValueError("")
		print("What do you want to update?")
		self.showUpdateMovieMenu()
		op = self.readOption()
		try:
			if op == 1:
				title = input("Title: ")
				self._service.updateMovie(indx, title, op)
			elif op == 2:
				desc = input("Description: ")
				self._service.updateMovie(indx, desc, op)
			elif op == 3:
				genre = input("Genre: ")
				self._service.updateMovie(indx, genre, op)
			else:
				raise ValueError("Can you read?")
		except SyntaxError as se:
			print(se)
			raise SyntaxError("")


	def rentMovieUI(self):
		try:
			rID = int(input("Rental ID: "))
			mID = int(input("Movie ID: "))
			cID = int(input("Client ID: "))
		except ValueError:
			print("Learn how to write")
			raise ValueError("")
		if type(self._service.movieRepo.findObj(mID)) is None:
			print("ID not found")
		if type(self._service.clientRepo.findObj(cID)) is None:
			print("ID not found")
		rentDate_raw = input("Rented Date (yyyy/mm/dd): ")
		dueDate_raw = input("Due date (yyyy/mm/dd): ")
		try:
			self._service.rentMovie(rentDate_raw, dueDate_raw, rID, mID, cID)
		except ValueError as ve:
			print(ve)
			raise ValueError('')
		except SyntaxError as se:
			print(se)
			raise SyntaxError('')
		except TypeError as te:
			print(te)
			raise TypeError("")


	def returnMovieUI(self):
		try:
			mID = int(input("Choose a rental ID: "))
		except ValueError:
			print("Learn how to write.")
			raise ValueError("")
		if self._service.rentalRepo.findByID == False:
			print("ID not found")
		returnDate_raw = input("Returned date (yyyy/mm/dd OR today): ")
		try:
			self._service.returnMovie(returnDate_raw, mID)
		except SyntaxError as se:
			print(se)
			raise SyntaxError()
		except ValueError as ve:
			print(ve)
			raise ValueError("")

	def searchClientsUI(self):
		self.showSearchClientMenu()
		op = input("Choose one of the above: ")
		if op != '1' and op != '2':
			print("Try again")
			raise ValueError("")
		o = int(op)
		filterr = input("Filter: ")
		result = self._service.searchClientsBy(filterr, o)
		self.printResult(result)

	def searchMoviesUI(self):
		self.showSearchMovieMenu()
		op = input("Choose one of the above: ")
		if op != '1' and op != '2' and op != '3' and op != '4':
			print("Try again")
			raise ValueError("")
		o = int(op)
		filterr = input("Filter: ")
		result = self._service.searchMoviesBy(filterr, o)
		self.printResult(result)

	def mostRentedUI(self):
		print("1. By number of rentals")
		print("2. By number of days rented")
		op = input("Choose one of the above: ")
		if op != '1' and op != '2':
			print("Try again")
			raise ValueError("")
		o = int(op)
		if o == 1:
			self.mostRentedMoviesByNumberUI()
		if o == 2:
			self.mostRentedMoviesByDaysUI()

	def mostRentedMoviesByDaysUI(self):
		res = self._service.mostRentedMoviesByDays()
		print("Number of days" + " " * 14 + "Movie")
		for item in res:
			print(str(item))

	def mostRentedMoviesByNumberUI(self):
		res = self._service.mostRentedMoviesByNumber()
		print("Number of rentals" + " " * 35 + "Movie")
		for item in res:
			print(str(item))

	def clientsWithMostRentedDaysUI(self):
		res = self._service.clientsWithMostRentedDays()
		print("Number of days" + " " * 35 + "Client")
		for item in res:
			print(str(item))

	def rentedMoviesUI(self):
		res = self._service.rentedMovies()
		print("The following movies are rented: ")
		for movie in res:
			print(str(movie))

	def printResult(self, result):
		for obj in result:
			print(str(obj))

	def undo(self):
		try:
			self._service.undo()
		except ValueError as ve:
			print(ve)

	def redo(self):
		try:
			self._service.redo()
		except ValueError as ve:
			print(ve)