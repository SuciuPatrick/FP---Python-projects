from Domain.Movie import *
from Domain.Client import Client
from Domain.Rental import Rental
from Repositories.repository import Repository
from Repositories.repositoryRental import repositoryRental
from UI.ui_functions import UI
from Services.service import Services
import random
import datetime
from test import *
from test.tests import *

class Main:
	def __init__(self):
		pass

	def clientsInitialize(self):
		clientRepo = Repository()
		firstName = ["Bogdan", "Andrei", "Cristi", "Patrick", "Gabriel", "Laura", "Alexandra", "Andreea", "Robert",
		             "Claudiu", "Mirel", "Carmen", "Darius", "Robert", "Macanache"]
		secondName = ["Suciu", "Petru", "Andras", "Pop", "Cosmulei", "Micu", "Crivei", "Bota", "Botis", "Stejerean",
		              "Vincze", "Somotecan", "Salvia"]

		i = 0
		while i <= 100:
			clientRepo.add(
				Client((i * 4 + i % 3 + 1) // 2 + 1, random.choice(firstName) + " " + random.choice(secondName)))
			i += 1

		i = 0
		while i < len(clientRepo._list):
			# print(clientRepo._list[i])
			i += 1

		return clientRepo

	def moviesInitialize(self):
		movieRepo = Repository()
		movieTitles = ["The Godfather", "The Shawshank Redemption", "Schindler's List", "Raging Bull", "Casablanca",
		               "Citizen Kane", "Gone with the Wind", "The Wizard of Oz ", "One Flew Over the Cuckoo's Nest"]
		descriptionList = ["Sure! Why not?", "Yea boi", "Best movie.", "Don't watch it with your mother", "18+", "1/10",
		                   "Do not recommend", "5/10", "Cry by yourself"]
		genreMovies = ["Drama", "Comedy", "Horror", "Action", "SF"]

		i = 0
		while i <= 100:
			movieRepo.add(
				Movie(((i * 5 + 1 + i % 2 + 3) // 2), random.choice(movieTitles), random.choice(descriptionList),
				      random.choice(genreMovies)))
			#print(movieRepo._list[i])
			i += 1

		return movieRepo

	#  de continuat cu repo-ul de rental + generari + mortii lor.
	def rentalInitialize(self, clientRepo, movieRepo):
		# global aid, movie, client, rentDate, dueDate, returnedDate
		rentalRepo = repositoryRental(clientRepo, movieRepo)
		for i in range(1, 100):
			aid = i
			movie = random.choice(movieRepo.getList())
			client = random.choice(clientRepo.getList())
			rentDate = datetime.date(random.randint(2014, 2018), random.randint(1, 12), random.randint(1, 28))
			dueDate = datetime.date(random.randint(2020, 2022), random.randint(1, 12), random.randint(1, 28))
			returnedDate = datetime.date(random.randint(2018, 2022), random.randint(1, 12), random.randint(1, 28))

			rental = Rental(aid, movie, client, rentDate, dueDate, returnedDate)
			rentalRepo.add(rental)

		return rentalRepo

	def run(self):
		clientRepo = self.clientsInitialize()
		movieRepo = self.moviesInitialize()
		rentalRepo = self.rentalInitialize(clientRepo, movieRepo)

		service = Services(clientRepo, movieRepo, rentalRepo)
		ui = UI(service)
		while True:
			try:
				ui.showMenu()
				value = ui.readOption()
				if value == 1:
					ui.printClientList()
				elif value == 2:
					ui.addClientUI()
				elif value == 3:
					ui.removeClientUI()
				elif value == 4:
					ui.updateClientUI()
				elif value == 5:
					ui.printMovieList()
				elif value == 6:
					ui.addMovieUI()
				elif value == 7:
					ui.removeMovieUI()
				elif value == 8:
					ui.updateMovieUI()
				elif value == 9:
					ui.printRentalList()
				elif value == 10:
					ui.rentMovieUI()
				elif value == 11:
					ui.returnMovieUI()
				elif value == 12:
					ui.searchClientsUI()
				elif value == 13:
					ui.searchMoviesUI()
				elif value == 14:
					ui.mostRentedUI()
				elif value == 15:
					ui.clientsWithMostRentedDaysUI()
				elif value == 16:
					ui.rentedMoviesUI()
				elif value == 17:
					ui.undo()
				elif value == 18:
					ui.redo()
				elif value == 0:
					return
			except ValueError:
				print ("Invalid syntax.")


runTests()
x = Main()
x.run()

