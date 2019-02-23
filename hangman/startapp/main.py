from UI.userinterface import UI
from Repository.repository_file import RepositoryFile
from Controller.controller import Controller

class main:
	def __init__(self):
		pass

	def run(self):

		repo = RepositoryFile("../sentences.txt")
		repo.readFromFile()
		controller = Controller(repo)
		ui = UI(controller)
		ui.showMenu()
		while True:
				value = input("Choose from the menu an instruction.")

				if value == '1':
					print("Insert a sentence: ")
					ui.addUI()

				if value == '2':
					ui.playGame()



start = main()
start.run()